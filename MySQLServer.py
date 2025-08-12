import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "willtotes",
        password = "Ntha201030!",
        database = "alx_book_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx book_store' created successfully!")

except mysql.connector.Error as er:
    print(f"Error: {er}")

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        