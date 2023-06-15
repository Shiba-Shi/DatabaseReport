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
    SELECT c. 客戶ID, c. 客戶名稱
    FROM 客戶 c
    JOIN 銷售紀錄 o ON c. 客戶ID = o. 客戶ID
    WHERE o.消費時間 >= DATE_SUB(NOW(), INTERVAL 1 YEAR)
    GROUP BY c. 客戶ID, c. 客戶名稱
    ORDER BY SUM(o. 消費金額) DESC
    LIMIT 1;
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("客戶ID:", result[0])
            print("客戶名稱:", result[1])
    else:
        print("未找到符合的用戶")

finally:
    cursor.close()
    connection.close()