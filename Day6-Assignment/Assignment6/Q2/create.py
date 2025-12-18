import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

sensor_id = str(input("Enter sensor_id : "))
moisture_level = float(input("Enter moisture_level : "))
data_time =input("Enter data_time : ")

query = f"insert into soil_moisture_readings values('{sensor_id}', {moisture_level}, '{data_time}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()