from django.contrib.auth.hashers import make_password
from django.shortcuts import render
import mysql.connector as sql

# Define your global variables for user data
fn = ''
ln = ''
s = ''
em = ''
pwd = ''
us = ''
ad = ''
ph = ''
ro = ''
id = ''

# Create your views here.
def signupaction(request):
    global us, fn, ln, s, em, pwd, ad, ph, ro, id
    if request.method == "POST":
        m = sql.connect(host="localhost", user="medkink_user", passwd="yourpassword", database="medkink")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "user_name":
                us = value
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "phone":
                ph = value
            if key == "address":
                ad = value
            if key == "role":
                ro = value

        # Hash the password before saving it
        hashed_password = make_password(pwd)

        # Modify the query to exclude the 'id' field, since it is auto-incremented
        c = """INSERT INTO users (username, first_name, last_name, email, password, phone_number, address, role) 
               VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            us, fn, ln, em, hashed_password, ph, ad, ro)

        # Execute the SQL query and commit the transaction
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')

