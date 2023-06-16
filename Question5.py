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
    sql1 = """
    SELECT c. 客戶ID, c. 客戶名稱, c. 聯絡電話, c. 聯絡信箱
    FROM 客戶 c
    JOIN 銷售紀錄 o ON c. 客戶ID = o. 客戶ID
    JOIN 產品狀態 p ON o. 銷售紀錄ID = p. 交易ID
    WHERE p. 追蹤號= '123456';
    """

    cursor.execute(sql1)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("客戶ID:", result[0])
            print("客戶名稱:", result[1])
            print("聯絡電話:", result[2])
            print("聯絡信箱:", result[3])
            print()
    else:
        print("未找到符合的用戶")

    sql2 = """
    SELECT od. 產品ID, p. 產品名稱, od. 產品數量
    FROM 銷售明細 od
    JOIN 產品 p ON od. 產品ID= p. 產品ID
    JOIN 產品狀態 pck ON od. 銷售ID= pck. 交易ID
    WHERE pck. 追蹤號 = '123456';
    """
    
    cursor.execute(sql2)
    results = cursor.fetchall()
    for result in results:
        print("產品ID:", result[0])
        print("產品名稱:", result[1])
        print("產品數量:", result[2])
        print()
    
    
    sql4 = ("""
    INSERT INTO 產品狀態 (交易ID, 追蹤號, 包裹狀態, 當前狀態)
    VALUES ('001817', 123457, '運送中', '未送達');
    """)
    cursor.execute(sql4)
    print("已創建替換商品的新包裹")

finally:
    cursor.close()
    connection.close()