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
- [Running the Application](#running-the-application)
  - [1. Initialize/Populate the Database](#1-initializepopulate-the-database)
  - [2. Start the Flask Development Server](#2-start-the-flask-development-server)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides a basic functional e-commerce storefront. It allows users to browse products, view product details, add items to a shopping cart, and see the total in their cart. The product data is stored in a SQLite database, managed by Flask-SQLAlchemy. The application emphasizes clarity and simplicity, making it a good starting point for understanding Flask web applications.

## Features

* **Product Catalog:** Display a list of available products on the homepage.
* **Product Details:** Dedicated page for each product with more information.
* **Shopping Cart:** Users can add products to a session-based shopping cart.
* **Cart Management:** View items in the cart and their total price.
* **Database Integration:** Products are stored persistently using SQLite and SQLAlchemy.
* **Static File Serving:** Serves static assets like CSS, JavaScript, and images.
* **Flash Messages:** Provides user feedback for actions (e.g., "Item added to cart!").

## Technologies Used

* **Backend Framework:** Flask (Python)
* **Database ORM:** Flask-SQLAlchemy
* **Database:** SQLite
* **Web Forms:** Flask-WTF
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
git clone <https://github.com/ASH-100703/e-commerce>
cd ecommerce_project
