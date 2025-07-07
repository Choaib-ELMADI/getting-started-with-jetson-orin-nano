import mysql.connector

connection = mysql.connector.connect(
    host="0.0.0.0", user="root", password="root", database="db_name"
)

if connection.is_connected():
    print("Connected to MySQL database!")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sensors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            sensor_name VARCHAR(50),
            value FLOAT
        );
    """
    )

    cursor.execute(
        "INSERT INTO sensors (sensor_name, value) VALUES (%s, %s)",
        ("Speed", 110),
    )
    connection.commit()

    cursor.execute("SELECT * FROM sensors;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
