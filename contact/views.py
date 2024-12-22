from django.shortcuts import render

from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib.auth.decorators import login_required

# View for the contact form
def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_phone = request.POST.get('contact_phone', '')  # Optional
        contact_email = request.POST.get('contact_email', '')
        message = request.POST.get('message')

        # Assuming user is logged in, fetch the user id from session or request.user
        user_id = request.user.id if request.user.is_authenticated else None

        # Connect to the MySQL database
        m = sql.connect(host="localhost", user="medkink_user", passwd="yourpassword", database="medkink")
        cursor = m.cursor()

        # Insert the contact message into the database
        c = """INSERT INTO EmergencyContacts (user_id, contact_name, contact_phone, contact_email, message) 
               VALUES (%s, %s, %s, %s, %s)"""
        
        cursor.execute(c, (user_id, contact_name, contact_phone, contact_email, message))
        m.commit()
        
        cursor.close()
        m.close()

        # Redirect the user to a confirmation page or the home page after submission
        return redirect('contact_success')

    return render(request, 'contact/contact.html')

# Confirmation page after message submission
def contact_success(request):
    return render(request, 'contact/contact_success.html')
