import mysql.connector

# Create connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="200ms11@sql.",
    database="online_food_delivery"
)

print("Connected Successfully!")

# Create cursor
cursor = db.cursor()

# Execute query
cursor.execute("SHOW TABLES")

# Fetch results
for table in cursor:
    print(table)

# Close connection
cursor.close()
db.close()