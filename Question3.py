import mariadb

user_setting = {
    "user" : "411077017",
    "password" : "411077017",
    "host" : "140.127.74.226",
    "database" : "411077017"
}

connection = mariadb.connect(**user_setting)
try:
    cursor = connection.cursor()
    sql = """
    SELECT p. 產品ID, p. 產品名稱
    FROM 產品 p
    JOIN 門市庫存 i ON i. 產品ID = p. 產品ID
    JOIN 實體門市 s ON i. 門市 = s. 店家名稱
    WHERE i. 產品數量 = 0
    AND s. 縣市 = '高雄市'
    GROUP BY p. 產品ID
    HAVING COUNT(i. 門市) = ( 
        SELECT COUNT(s. 店家名稱)
        FROM 實體門市 s
        WHERE s. 縣市 = '高雄市'
    );
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("產品ID:", result[0])
            print("產品名稱:", result[1])
            print()
    else:
        print("未找到符合的產品")

finally:
    cursor.close()
    connection.close()