# Med_Link
# MedLink

MedLink is a web-based application built using **Django** and **MySQL** for managing user authentication, product listings, shopping cart, payment functionality, and notifications. The application also integrates **Google Authentication** for easy login.

## Features

- **User Authentication**: Users can sign up, log in, and authenticate using Google OAuth.
- **Product Listing**: Users can view a catalog of available products.
- **Shopping Cart**: Users can add products to their cart, update quantities, or remove items.
- **Payment Integration**: Users can make payments through a secure integration (Stripe, PayPal, etc.).
- **Notifications**: Users can receive notifications regarding their order status or other updates.
- **MySQL Database**: All data (including user data, product information, and transaction data) is stored in a MySQL database.

## Technologies Used

- **Backend**: Django (Python)
- **Database**: MySQL
- **Authentication**: Google OAuth (using `django-allauth`)
- **Payment Integration**: Stripe / PayPal (You can mention your specific payment gateway here)
- **Notifications**: Django email notifications or real-time notifications using Django Channels
- **Frontend**: HTML, CSS (Custom design)
- **Version Control**: Git & GitHub

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- Google Developer Console account (for OAuth credentials)
- Git

### Steps to Set Up

1. **Clone the repository**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/medlink.git

   Create and activate a virtual environment
   python3 -m venv venv
   venv\Scripts\activate 

   ##Set up MySQL Database

###Create a MySQL database for your project:
CREATE DATABASE medkink;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medkink',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



### apply migrations 
python manage.py migrate

### Create a superuser
python manage.py createsuperuser


### Run the development server
python manage.py runserver


git commit -m "Update README.MD"

