



from django.shortcuts import render
import mysql.connector as sql  # Import MySQL connector

def search_drugs(request):
    if request.method == "POST":
        # Get the search query from the form
        search_query = request.POST.get('search_query', '')
        
        if search_query:
            # Establish connection to the MySQL database
            m = sql.connect(host="localhost", user="root", passwd="moha_12345", database="medkink")
            cursor = m.cursor()
            
            # SQL query to search for drugs using LIKE for partial matches
            query = """
                SELECT id, name, category, description, price, link
                FROM Drugs 
                WHERE name LIKE %s OR category LIKE %s OR description LIKE %s
            """
            
            # The search value with '%' for partial matching
            search_value = f"%{search_query}%"
            
            # Execute the query with parameters
            cursor.execute(query, (search_value, search_value, search_value))
            
            # Fetch all matching results
            results = cursor.fetchall()
            
            # Prepare the results for rendering
            drugs = [{'id': row[0], 'name': row[1], 'category': row[2], 'description': row[3], 'price': row[4], 'link': row[5] } for row in results]
            
            # Close the database connection
            cursor.close()
            m.close()
            
            # Render the results in the template
            return render(request, 'drug_search_results.html', {'results': drugs, 'query': search_query})
        
        else:
            # If no search query was provided
            return render(request, 'drug_search_results.html', {'results': [], 'query': search_query})
    
    else:
        # If the request is not a POST, show the search form
        return render(request, 'drug_search.html')





