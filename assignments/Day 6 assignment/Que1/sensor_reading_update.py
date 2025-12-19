import mysql.connector as myc

connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_application",
    use_pure=True
)

temperature=int(input("Enter Temperature compare: "))

query="SELECT * FROM sensor_readings";
query1="SELECT * FROM sensor_readings WHERE temperature <25";

cursor=connection.cursor()

cursor.execute(query)

readings=cursor.fetchall()

print(readings)

cursor.execute(query1)

filtered_readings = cursor.fetchall()

print(filtered_readings)

cursor.close()

connection.close()