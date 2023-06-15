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
    SELECT p. 產品ID, p. 產品名稱, SUM(od. 產品數量* od. 產品單件價格) AS total_sales
    FROM 產品 p
    JOIN 銷售明細 od ON p. 產品ID = od. 產品ID
    JOIN 銷售紀錄 o ON od. 銷售ID = o. 銷售紀錄ID
    WHERE o. 消費時間>= DATE_SUB(NOW(), INTERVAL 1 YEAR)
    GROUP BY p. 產品ID, p. 產品名稱
    ORDER BY total_sales DESC
    LIMIT 2;
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("產品ID:", result[0])
            print("產品名稱:", result[1])
            print("銷售金額:", result[2])
            print()
    else:
        print("未找到符合的產品")

finally:
    cursor.close()
    connection.close()