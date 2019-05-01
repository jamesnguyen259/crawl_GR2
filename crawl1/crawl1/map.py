import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jamesnguyen96",
    database="hanoitravel"
    )
mycursor = mydb.cursor(buffered=True)
for count in range(1340, 3490):
    query1 = "SELECT id, image_url FROM restaurants WHERE id = %s"
    mycursor.execute(query1, (count,))
    result = mycursor.fetchone()
    temp = result[1].replace("https://diadiem.co","")
    query2 = "UPDATE restaurants SET image_url = %s WHERE id = %s"
    mycursor.execute(query2, (temp, result[0]))
    mydb.commit()
    print("Item updated!")

