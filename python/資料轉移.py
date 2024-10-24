# MSSQL 到 MySQL 的轉移範例

import pyodbc
import pymysql

# MSSQL 資料庫連接參數
mssql_conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=你的＿mssq_伺服器;'
    'UID=你的使用者名稱;'
    'PWD=你的密碼'
)
# MySQL 資料庫連接的參數

mysql_conn = pymysql.connect(
    host='10.96.196.36',
    user='NPSPO_User',
    password='Gaming@NPD',
    database='你建立好的業務名稱的資料庫 例如 _Myasus',
    charset='utf8mb4',
    cursorclass='pymysql.cursors.DictCursor'

# charset='utf8mb4'：這指定了連接 MySQL 時使用的字元集。utf8mb4 是 UTF-8 的一個變體，它允許存儲完整的 Unicode 字元，包括表情符號和其他特殊符號。utf8mb4 是一種推薦使用的字元集，因為它相較於 utf8 能存儲更多種類的字元。

# cursorclass=pymysql.cursors.DictCursor：這個參數指定了要使用的游標類型。DictCursor 會將查詢結果返回為字典格式，而不是默認的元組格式。這樣你可以通過鍵值對的方式來訪問查詢結果，像這樣：row['column_name']，而不是使用索引來存取。

# 這兩個參數能讓資料庫連接更具靈活性和兼容性，特別是在處理 Unicode 字符以及需要容易讀取的查詢結果時。
)

def fetch_data_from_mssql(query):
    cursor = mssql_conn.cursor()  # 使用 MSSQL 連接建立游標
    cursor.execute(query)  # 執行傳入的 SQL 查詢
    rows = cursor.fetchall()  # 獲取所有查詢結果
    cursor.close()  # 關閉游標
    return rows  # 返回查詢結果作為資料列列表
    return rows

def insert_data_into_mysql(rows, table):
    with mysql_conn.cursor() as cursor:  # 使用 MySQL 連接建立游標
        for row in rows:  # 遍歷每一行資料
            # 構建插入語句的參數佔位符和欄位名稱
            placeholders = ', '.join(['%s'] * len(row))  # %s 是 SQL 中的佔位符
            columns = ', '.join(row.keys())  # 將字典的鍵（即欄位名）轉換為用逗號分隔的字串
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"  # 構建插入 SQL 語句
            cursor.execute(sql, list(row.values()))  # 執行 SQL，並將資料插入
    mysql_conn.commit()  # 提交事務，確保資料寫入 MySQL


def migrate_data(mssql_query, mysql_table):
    rows = fetch_data_form_mssql(mssql_query)
    insert_data_into_mysql(rows, mysql_table)
    
# 執行資料轉移
mssql_query = "SELECT * FROM 你的mssql表"
mysql_table = "你mysql的表"
migrate_data(mssql_query, mysql_table)

# 關閉連接
mysql_conn.clsoe
mssql_conn.close
