# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# import mysql.connector as sql

# # Helper function to establish database connection
# def get_db_connection():
#     return sql.connect(host="localhost", user="medkink_user", passwd="yourpassword", database="medkink")

# from django.shortcuts import render, redirect
# import mysql.connector as sql

# def add_to_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('productId')
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         # Assuming you have some user identification, e.g., via session
#         user_id = request.session.get('user_id')

#         # Check if the cart exists in the session
#         if 'cart' not in request.session:
#             request.session['cart'] = {}

#         # Check if the item is already in the cart
#         if product_id in request.session['cart']:
#             request.session['cart'][product_id] += 1  # Increment the quantity
#         else:
#             request.session['cart'][product_id] = 1  # Add new item to the cart

#         request.session.modified = True

#         return redirect('view_cart')  # Redirect to a view that displays the cart
#     else:
#         return render(request, 'products.html')  # Redirect back to products page if not a POST request



# def view_cart(request):
#     cart_items = request.session.get('cart', {})
#     products = []
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     for product_id, quantity in cart_items.items():
#         cursor.execute('SELECT name, price FROM Drugs WHERE id = %s', (product_id,))
#         product = cursor.fetchone()
#         if product:
#             products.append({
#                 'name': product[0],
#                 'price': product[1],
#                 'quantity': quantity
#             })

#     return render(request, 'cart/cart.html', {'products': products})


# def remove_from_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('productId')

#         # Check if the item exists in the cart and remove it
#         if 'cart' in request.session and product_id in request.session['cart']:
#             del request.session['cart'][product_id]  # Remove the item from the cart
#             request.session.modified = True  # Notify Django that the session has been modified

#         return redirect('view_cart')
#     else:
#         return redirect('view_cart')  # Redirect to the cart view if not a POST request


# def update_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('productId')
#         quantity = int(request.POST.get('quantity'))

#         # Check if the item exists in the cart and update its quantity
#         if 'cart' in request.session and product_id in request.session['cart']:
#             if quantity > 0:
#                 request.session['cart'][product_id]['quantity'] = quantity  # Update the quantity
#             else:
#                 # If the quantity is zero or less, remove the item from the cart
#                 del request.session['cart'][product_id]

#             request.session.modified = True  # Notify Django that the session has been modified

#         return redirect('view_cart')
#     else:
#         return redirect('view_cart')  # Redirect to the cart view if not a POST request



from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required 
# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
import mysql.connector as sql

# Assuming login view
def login(request):
    # Perform authentication
    user_id = request.user.authenticate_user(request)
    if user_id:
        request.session['user_id'] = user_id  # Set user ID in session
        return redirect('home')
    else:
        return render(request, 'login.html', {'error': 'Invalid credentials'})


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import mysql.connector as sql

from django.shortcuts import render, redirect
import mysql.connector as sql

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import mysql.connector as sql
import uuid

def get_db_connection():
    return sql.connect(host="localhost", user="root", passwd="moha_12345", database="medkink")

import uuid

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        quantity = int(request.POST.get('quantity', 1))
        session_id = request.session.session_key or str(uuid.uuid4())  # Generate a new session key if none exist

        conn = get_db_connection()
        cursor = conn.cursor()

        # Ensure session key is set in the session
        request.session['session_key'] = session_id

        # Insert or update the item in the database
        cursor.execute("""
            INSERT INTO ShoppingCart (SessionID, DrugID, Quantity) VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE Quantity = Quantity + VALUES(Quantity)
        """, (session_id, product_id, quantity))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect('view_cart')
    else:
        return render(request, 'products.html')


    

def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        print("Removing product ID:", product_id)  # Debug print

        conn = get_db_connection()
        cursor = conn.cursor()
        session_id = request.session.get('session_key', None)

        if not session_id:
            print("Session ID not found.")  # Debug print
            return HttpResponseRedirect(reverse('view_cart'))

        cursor.execute("DELETE FROM ShoppingCart WHERE SessionID = %s AND DrugID = %s", (session_id, product_id))
        conn.commit()
        cursor.close()
        conn.close()

        return HttpResponseRedirect(reverse('view_cart'))
    else:
        return HttpResponseRedirect(reverse('view_cart'))


def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        quantity = int(request.POST.get('quantity'))
        conn = get_db_connection()
        cursor = conn.cursor()
        session_id = request.session.get('session_key')

        if quantity > 0:
            cursor.execute("UPDATE ShoppingCart SET Quantity = %s WHERE SessionID = %s AND DrugID = %s", (quantity, session_id, product_id))
        else:
            cursor.execute("DELETE FROM ShoppingCart WHERE SessionID = %s AND DrugID = %s", (session_id, product_id))

        conn.commit()
        cursor.close()
        conn.close()

        return HttpResponseRedirect(reverse('view_cart'))
    else:
        return HttpResponseRedirect(reverse('view_cart'))

def view_cart(request):
    session_id = request.session.get('session_key')
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT d.name, d.price, sc.Quantity
        FROM ShoppingCart sc
        JOIN Drugs d ON sc.DrugID = d.id
        WHERE sc.SessionID = %s
    """, (session_id,))

    products = [{
        'name': product[0],
        'price': product[1],
        'quantity': product[2]
    } for product in cursor.fetchall()]

    cursor.close()
    conn.close()

    return render(request, 'cart/cart.html', {'products': products})

