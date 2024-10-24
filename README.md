# Django-Assesment

Create a Django API with django rest framework

- [x]  users with custom roles - admin, coach, agent, football player
- [x]  sign up and social sign up (google, facebook)
- [x]  login and social login
- [x]  password reset



## Overview

This is a Django REST API for managing user roles and authentication, including registration, login, and password reset functionalities. The API supports custom user roles: **admin**, **coach**, **agent**, and **football player**. It also implements social authentication using Google and Facebook.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Running the Application](#running-the-application)

## Features

- User registration and login with custom roles
- Social login with Google and Facebook
- Password reset functionality
- RESTful API architecture

## Technologies Used

- **Django**: A high-level Python web framework
- **Django REST Framework**: Toolkit for building Web APIs
- **dj-rest-auth**: Authentication and registration endpoints
- **django-allauth**: Integrated social authentication
- **SQLite**: Lightweight database for development

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/django-assessment.git
   cd django-assessment
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Environment Variables

Create a file named `.env` using the provided `env.template` file and fill in the required values:

```bash
# Example of .env file
export DJANGO_ALLOWED_HOSTS="* localhost 127.0.0.1 [::1]"
export DJANGO_SECRET_KEY='your_django_secret_key'
export GOOGLE_CLIENT_ID='your-google-client-id'
export GOOGLE_CLIENT_SECRET='your-google-client-secret'
export FACEBOOK_CLIENT_ID='your-facebook-client-id'
export FACEBOOK_CLIENT_SECRET='your-facebook-client-secret'
```

and source your environment variables to make sure they are loaded correctly. You can do this by running the following command in your terminal
```bash
source .env
```

## API Endpoints

### Registration

- **POST** `/auth/registration/`
- Request body:
  ```json
  {
    "username": "user",
    "email": "user@example.com",
    "password": "yourpassword",
    "role": "football_player"  // Example role
  }
  ```

### Login

- **POST** `/auth/login/`
- Request body:
  ```json
  {
    "username": "user",
    "password": "yourpassword"
  }
  ```

### Password Reset

- **POST** `/auth/password/reset/`
- Request body:
  ```json
  {
    "email": "user@example.com"
  }
  ```

### Social Authentication

- **GET** `/auth/social/login/google/`
- **GET** `/auth/social/login/facebook/`

## Testing with Postman

A Postman collection is provided to help you test the API endpoints easily. You can import the collection file (`postman_collection.json`) into Postman to explore the API.

## Running the Application

To run the development server, use the following command:

```bash
python manage.py runserver
```

You can access the API at `http://127.0.0.1:8000/`.
