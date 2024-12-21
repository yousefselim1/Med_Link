# import requests
# from django.conf import settings
# from django.shortcuts import render, redirect

# # Helper function to get API credentials securely
# def get_paymob_credentials():
#     return settings.PAYMOB_API_KEY, settings.PAYMOB_INTEGRATION_ID

# # View to handle payment
# def initiate_payment(request):
#     api_key, integration_id = get_paymob_credentials()
#     # 1. Generate Auth Token
#     auth_response = requests.post(
#         'https://accept.paymob.com/api/auth/tokens',
#         json={"api_key": api_key}
#     )
#     auth_token = auth_response.json().get('token')
    
#     # 2. Create an Order
#     order_data = {
#         "auth_token": auth_token,
#         "delivery_needed": "false",
#         "amount_cents": "10000",  # Amount in cents (e.g., 100 EGP)
#         "currency": "EGP",
#         "items": []
#     }
#     order_response = requests.post(
#         'https://accept.paymob.com/api/ecommerce/orders',
#         json=order_data
#     )
#     order_id = order_response.json().get('id')
    
#     # 3. Request a Payment Key
#     payment_key_data = {
#         "auth_token": auth_token,
#         "amount_cents": "10000",
#         "expiration": 3600,  # 1 hour
#         "order_id": order_id,
#         "billing_data": {
#             "apartment": "NA", "email": "customer-email@example.com",
#             "floor": "NA", "first_name": "First", "street": "NA",
#             "building": "NA", "phone_number": "+201111111111",
#             "shipping_method": "PKG", "postal_code": "NA",
#             "city": "Cairo", "country": "EG", "last_name": "Last",
#             "state": "Cairo"
#         },
#         "currency": "EGP",
#         "integration_id": integration_id
#     }
#     payment_key_response = requests.post(
#         'https://accept.paymob.com/api/acceptance/payment_keys',
#         json=payment_key_data
#     )
#     payment_key = payment_key_response.json().get('token')

#     # Redirect to Paymob's payment page using the payment key
#     return redirect(f"https://accept.paymob.com/api/acceptance/iframes/{integration_id}?payment_token={payment_key}")

# # Adding the URL configuration
# from django.urls import path

# urlpatterns = [
#     path('pay/', initiate_payment, name='initiate_payment'),
# ]




from django.shortcuts import render
import mysql.connector as sql

def get_db_connection():
    return sql.connect(host="localhost", user="medkink_user", passwd="yourpassword", database="medkink")

def payment_view(request):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use session_id or a fallback if not present
    session_id = request.session.get('session_key', None)
    if not session_id:
        # Redirect to login or cart page if session ID is not found
        return render(request, 'login.html')  # or redirect to a page that handles empty carts or session issues

    # SQL query to select items from the ShoppingCart table using session_id
    cursor.execute("""
    SELECT d.name, d.price, sc.Quantity
    FROM ShoppingCart sc
    JOIN Drugs d ON sc.DrugID = d.id
    WHERE sc.SessionID = %s
    """, (session_id,))

    items = []
    total = 0
    for name, price, quantity in cursor.fetchall():
        total_item_price = price * quantity
        total += total_item_price
        items.append({
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': total_item_price
        })

    shipping = 20  # Assuming a flat shipping rate
    grand_total = total + shipping

    cursor.close()
    conn.close()

    context = {
        'items': items,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total
    }

    return render(request, 'payment/payment.html', context)




