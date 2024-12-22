from django.shortcuts import render
import mysql.connector as sql

def products(request):
    # Establish connection to the MySQL database
    m = sql.connect(host="localhost", user="medkink_user", passwd="yourpassword", database="medkink")
    cursor = m.cursor()

    # SQL query to select all products
    query = "SELECT id, name, category, description, price, link FROM Drugs"
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch all products
    results = cursor.fetchall()
    
    # Prepare the products for rendering
    products = [{'id': row[0], 'name': row[1], 'category': row[2], 'description': row[3], 'price': row[4], 'link': row[5]} for row in results]
    
    # Close the database connection
    cursor.close()
    m.close()

    # Render the products in the template
    return render(request, 'products/products.html', {'products': products})
