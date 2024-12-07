Railway Management System

This project is a Django-based web application designed for managing railway bookings and train schedules. It allows users to:

User Registration and Login: Users can create accounts, log in, and authenticate using tokens.
Train Management: Admins can add new trains to the system.
Seat Availability: Users can check the availability of seats between source and destination.
Booking Seats: Registered users can book seats on available trains.
Booking Details: Users can view their booking details.
The project utilizes Django Rest Framework for creating RESTful APIs and integrates with a MySQL database to store train and booking data.

Table of Contents
1. Prerequisites
2. Setup Instructions
3. Running the Project
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Prerequisites
Before setting up the project, ensure you have the following installed:

Python 3.8 or above
Django (latest stable version)
A virtual environment manager (e.g., venv, virtualenv, or conda)

2. Setup Instructions


Clone the Repository:

```
git clone <repository_url>
cd <repository_name>
```

Set Up a Virtual Environment:

```
python -m venv env
source env/bin/activate   # On Windows: .\env\Scripts\activate
```

Install Dependencies: Make sure you have the pip package manager installed, then run:

```
pip install -r requirements.txt
```

Apply Migrations: Run the following commands to set up the database:

```
python manage.py makemigrations
python manage.py migrate
```

Create a Superuser: Create an admin account for the Django admin panel:

```
python manage.py createsuperuser
```

3. Running the Project (Start the Development Server)

```
python manage.py runserver
```

Access the Application: Open your browser and visit:

Admin Panel: http://127.0.0.1:8000/admin/
