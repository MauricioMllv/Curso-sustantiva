import psycopg2 

conexion = psycopg2.connect(
    user='admin',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='Millavil'
)

print(conexion)
