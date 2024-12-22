
from django.contrib.auth.decorators import login_required 
# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
import mysql.connector as sql

from django.shortcuts import render ,redirect

@login_required
def index(request):
    return render(request, 'home/index.html')


def index_2(request):
    # If the user is already logged in, redirect them to the home page directly
    if request.user.is_authenticated:
        return redirect('home/index.html')  # Replace 'index' with the name of your home page view
    # Otherwise, show the login page
    return render(request, "login_page.html")

# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect("/")

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
        
        # Get the stored hashed password from the database 
        stored_hashed_password = user[2]  

        # Use Django's check_password function to verify the entered password
        if check_password(pwd, stored_hashed_password):
            # Password is correct, redirect to home page
            return redirect('home')
        else:
            # Incorrect password, return to error page
            return render(request, 'error.html')

    return render(request, 'login_page.html')

