# import mysql connector
import mysql.connector
import time
from datetime import datetime


connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "students",
    use_pure = True
)


id = int(input("Enter id : "))
temp = float (input("Enter temp : "))
humidity = float(input("Enter humidity : "))
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
timestamp = formatted_time

query = f"insert into sensor_readings values({id}, '{temp}', '{humidity}', '{timestamp}');"


cursor = connection.cursor()


cursor.execute(query)


connection.commit()


cursor.close()


connection.close()