import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

sensor_id = input("Enter sensor_id where temperature to be updated: ")
moisture_level = input("Enter changed moisture_level : ")

query = f"update soil_moisture_readings SET moisture_level={moisture_level} where sensor_id='{sensor_id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()