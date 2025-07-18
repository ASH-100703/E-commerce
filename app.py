from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ash#100703@e-commerce'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Product(db.Model):
id = db.Column(db.Integer , primary_key=True)
name = db.Column(db.String(100), nullable=False)
price = db.Column(db.Float, nullabe=False)
image_url = db.Column(db.String(200), nullable=False, default = 'https://via.placeholder.com/150')
description = db.Column(db.Text, nullable=True)
def __repr__(self:
             return f"Product('{self.name}', '{self.price}')"

# Routes
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
   
    if 'cart' not in request.session: 
        request.session['cart'] = [] 
    request.session['cart'].append(product.id) 
    flash(f'{product.name} added to cart!', 'success')
    return redirect(url_for('home')) 


@app.route('/cart')
def cart():
    
    cart_items = [] 
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
   
    with app.app_context():
        db.create_all()

        # Adding some dummy products 
        if Product.query.count() == 0:
            product1 = Product(name='Vintage T-Shirt', price=25.00, image_url='https://via.placeholder.com/150/FF0000/FFFFFF?text=T-Shirt', description='A classic vintage t-shirt.')
            product2 = Product(name='Stylish Jeans', price=50.00, image_url='https://via.placeholder.com/150/0000FF/FFFFFF?text=Jeans', description='Comfortable and stylish denim jeans.')
            product3 = Product(name='Leather Boots', price=80.00, image_url='https://via.placeholder.com/150/00FF00/FFFFFF?text=Boots', description='Durable leather boots for all occasions.')
            db.session.add_all([product1, product2, product3])
            db.session.commit()

    app.run(debug=True)
