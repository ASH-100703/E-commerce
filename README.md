# 📦 E-commerce Shop (Flask)

A simple and lightweight e-commerce application built with Flask, Python, and SQLAlchemy. This project serves as a foundational example demonstrating core web development concepts, including a basic product catalog, shopping cart functionality, and database integration.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Environment Variables](#set-environment-variables)
- [Running the Application](#running-the-application)
  - [1. Initialize/Populate the Database](#1-initializepopulate-the-database)
  - [2. Start the Flask Development Server](#2-start-the-flask-development-server)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides a basic functional e-commerce storefront. It allows users to browse products, view product details, add items to a shopping cart, and proceed to a checkout process. The product data is stored in a SQLite database, managed by Flask-SQLAlchemy. The application emphasizes clarity and simplicity, making it a good starting point for understanding Flask web applications.

## Features

* **Product Catalog:** Display a list of available products on the homepage.
* **Product Details:** Dedicated page for each product with more information.
* **Shopping Cart:** Users can add products to a session-based shopping cart and manage quantities.
* **Cart Management:** View items in the cart, adjust quantities, and see their total price.
* **Checkout Process:** A simple form to simulate placing an order.
* **Database Integration:** Products are stored persistently using SQLite and Flask-SQLAlchemy.
* **Static File Serving:** Serves static assets like CSS, JavaScript, and images (e.g., product images from `static/images/`).
* **Flash Messages:** Provides user feedback for actions (e.g., "Item added to cart!").

## Technologies Used

* **Backend Framework:** Flask
* **Database ORM:** Flask-SQLAlchemy
* **Database:** SQLite
* **Web Forms:** Flask-WTF
* **Environment Variables:** python-dotenv
* **HTML Sanitization:** Bleach
* **Templating Engine:** Jinja2
* **Frontend:** HTML, CSS, JavaScript (basic)

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.7+ (Recommended: Python 3.10+)
* `pip` (Python package installer)

### Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone [https://github.com/ASH-100703/e-commerce.git](https://github.com/ASH-100703/e-commerce.git)
cd e-commerce
```
### Create a virtual environment
python -m venv venv

### Activate the virtual environment
#### On Windows:
```bash
.\venv\Scripts\activate
```
#### On macOS/Linux:
``` bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Enviornment Variables
This project uses environment variables for sensitive information like the SECRET_KEY.
Create a file named .env in the root directory of your project (the same directory as app.py).
Add your secret key to this file:

***SECRET_KEY=your_very_secret_random_string_here***

Replace your_very_secret_random_string_here with a long, random string. You can generate one in Python using import secrets; secrets.token_hex(16)

## Enjoy your simple and basic E-commerce app now !!! 
