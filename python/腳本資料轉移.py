# 方式一：透過 Python 操作 MSSQL 到 MySQL 資料轉移
# 優點：
# 靈活性高：可以根據需要進行更複雜的數據處理或自動化。
# 可重複性高：寫成腳本後，可以自動化定期執行資料同步。
# 需要的 Python 套件：
# pyodbc：用來連接 MSSQL。
# mysql-connector-python 或 PyMySQL：用來連接 MySQL。
# 你可以使用 pip 來安裝這些套件：

# pip install pyodbc mysql-connector-python pymysql


# 1：連接 MSSQL 資料庫

import pyodbc

# MSSQL 連接參數
mssql_connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=your_mssql_server;'
    'DATABASE=your_mssql_db;'
    'UID=your_username;'
    'PWD=your_password'
)

mssql_conn = pyodbc.connect(mssql_connection_string)
mssql_cursor = mssql_conn.cursor()

# 從 MSSQL 中提取資料
mssql_cursor.execute("SELECT * FROM your_table")
mssql_data = mssql_cursor.fetchall()

# 2：連接 MySQL 資料庫

import mysql.connector

# MySQL 連接參數
mysql_conn = mysql.connector.connect(
    host="10.96.196.36",
    user="NPSPO_User",
    password="Gaming@NPD",
    database="your_mysql_db"
)

mysql_cursor = mysql_conn.cursor()

# 創建目標表，如果尚未存在
create_table_query = """
CREATE TABLE IF NOT EXISTS your_table (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    value FLOAT
);
"""
mysql_cursor.execute(create_table_query)

#  3：插入資料到 MySQL

# 插入 MSSQL 資料到 MySQL
insert_query = "INSERT INTO your_table (id, name, value) VALUES (%s, %s, %s)"
for row in mssql_data:
    mysql_cursor.execute(insert_query, (row.id, row.name, row.value))

# 提交更改
mysql_conn.commit()

# 關閉連接
mysql_cursor.close()
mysql_conn.close()
mssql_cursor.close()
mssql_conn.close()

# 優化建議：
# 如果資料量大，考慮使用批量插入，例如 executemany()。
# 增量同步：在 MSSQL 中設置一個時間戳或使用自增 ID，只提取新增或更新的資料。



