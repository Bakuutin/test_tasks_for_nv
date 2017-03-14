# Original Task

Create django class-based view to export a CSV file with a large number of rows (at least two million).

Requred row format:

    customer.id;customer.first_name;customer.last_name;email.address;phone.number
    
*Note: Since the `Customer` model has one-to-many relationships with `Email` and `Phone` models, there can be several rows with duplicate fields from the customer `"customer.id; customer.first_name; customer.last_name"`, but different `"email.address; Phone.number"`.*

To prepare the data (more than two million customers), you should develop a stored procedure or function on `PL/Python` or `PL/pgSQL`.

Platform requirements: Linux, Python 3.4+, Django 1.9+, PostgreSQL 9.4+

# How To Deploy

    pip install -Ur requirements.txt
    psql -c "CREATE DATABASE nv WITH ENCODING 'UTF8'"
    touch nv/settings/local.py
