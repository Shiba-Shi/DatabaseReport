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
    SELECT p. 交易ID, p. 追蹤號
    FROM 產品狀態 p
    WHERE p. 包裹狀態 = 'Delayed';
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("交易ID:", result[0])
            print("追蹤號:", result[1])
            print()
    else:
        print("未找到符合的產品")

finally:
    cursor.close()
    connection.close()