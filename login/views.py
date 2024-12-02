from django.shortcuts import render
from django.contrib.auth.hashers import check_password
import mysql.connector as sql

# Global variables for email and password

def loginaction(request):
    global em, pwd
    if request.method == "POST":
        # Connect to the MySQL database
        m = sql.connect(host="localhost", user="medkink_user", passwd="yourpassword", database='medkink')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        # Query to fetch the user by email
        c = "SELECT * FROM users WHERE email = %s"
        cursor.execute(c, (em,))
        user = cursor.fetchone()

        # If no user is found, return to error page
        if user is None:
            return render(request, 'error.html')
        
        # Get the stored hashed password from the database (index 2 for password)
        stored_hashed_password = user[2]  # Assuming the password is at index 2

        # Use Django's check_password function to verify the entered password
        if check_password(pwd, stored_hashed_password):
            # Password is correct, redirect to welcome page
            return render(request, "welcome.html")
        else:
            # Incorrect password, return to error page
            return render(request, 'error.html')

    return render(request, 'login_page.html')



