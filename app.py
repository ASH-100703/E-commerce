from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from datetime import datetime
import os
import secrets
from dotenv import load_dotenv
import bleach

app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"

    def save_image(self, image):
        if image:
            filename = secrets.token_hex(8) + '.' + image.filename.split('.')[-1]
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            self.image_url = filename
            return True
        return False

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    items = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Product')

    def validate_price(self, price):
        try:
            value = float(price.data)
            if value <= 0:
                raise ValueError('Price must be positive.')
        except (ValueError, TypeError):
            raise ValidationError('Price must be a valid number greater than 0.')

class CheckoutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = TextAreaField('Address', validators=[DataRequired()])
    submit = SubmitField('Place Order')

@app.context_processor
def inject_cart_count():
    cart = session.get('cart', {})
    count = sum(cart.values()) if cart else 0
    return dict(cart_count=count)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    session['cart'] = cart
    session.modified = True
    flash(f'{product.name} added to cart!', 'success')
    return redirect(url_for('home'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        cart.pop(pid, None)
        session['cart'] = cart
        session.modified = True
    if cart:
        return redirect(url_for('cart'))
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_items = []
    total_price = 0.0
    for product_id_str, quantity in cart.items():
        product = Product.query.get(int(product_id_str))
        if product:
            cart_items.append({'product': product, 'quantity': quantity})
            total_price += product.price * quantity
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/increase_quantity/<int:product_id>', methods=['GET'])
def increase_quantity(product_id):
    cart = session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        cart[pid] += 1
        session['cart'] = cart
        session.modified = True
    return redirect(url_for('cart'))

@app.route('/decrease_quantity/<int:product_id>', methods=['GET'])
def decrease_quantity(product_id):
    cart = session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        if cart[pid] > 1:
            cart[pid] -= 1
        else:
            cart.pop(pid)
        session['cart'] = cart
        session.modified = True
    return redirect(url_for('cart'))

@app.route('/update_quantity/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    try:
        new_quantity = int(request.form.get('quantity'))
        if new_quantity < 1:
            raise ValueError()
    except (ValueError, TypeError):
        flash("Invalid quantity.", "warning")
        return redirect(url_for('cart'))
    cart = session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        cart[pid] = new_quantity
        session['cart'] = cart
        session.modified = True
    flash("Quantity updated.", 'info')
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    if form.validate_on_submit():
        cart = session.get('cart', {})
        if not cart:
            flash("Your cart is empty.", "warning")
            return redirect(url_for('cart'))
        cart_items = []
        total_price = 0.0
        for product_id_str, quantity in cart.items():
            product = Product.query.get(int(product_id_str))
            if product:
                cart_items.append({'name': product.name, 'quantity': quantity, 'price': product.price})
                total_price += product.price * quantity
        order = Order(
            name=bleach.clean(form.name.data),
            email=bleach.clean(form.email.data),
            address=bleach.clean(form.address.data),
            total_price=total_price,
            items=cart_items
        )
        db.session.add(order)
        db.session.commit()
        session.pop('cart', None)
        session.modified = True
        flash(f"Thank you {bleach.clean(form.name.data)}, your order has been placed!", "success")
        return redirect(url_for('thank_you'))
    # flash(None)
    return render_template('checkout.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    with app.app_context():
        db.create_all()
        if Product.query.count() == 0:
            product1 = Product(name='Vintage T-Shirt', price=25.00, image_url='tshirt.jpg', description='A classic vintage t-shirt.')
            product2 = Product(name='Stylish Jeans', price=50.00, image_url='jeans.jpg', description='Comfortable and stylish denim jeans.')
            product3 = Product(name='Leather Boots', price=80.00, image_url='boots.jpg', description='Durable leather boots for all occasions.')
            db.session.add_all([product1, product2, product3])
            db.session.commit()
    app.run(debug=True)
