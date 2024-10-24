import pyodbc  # 用於連接 MSSQL 的庫
import pymysql  # 用於連接 MySQL 的庫

# MSSQL 資料庫連接參數
def connect_to_mssql():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=APZA001GOD;'
            'DATABASE=NPS_2;'
            'Trusted_Connection=yes;'
        )
        print("成功連接到 MSSQL 資料庫")
        return connection
    except Exception as e:
        print(f"連接到 MSSQL 失敗：{e}")

# MySQL 資料庫連接參數
def connect_to_mysql():
    try:
        connection = pymysql.connect(
            host='10.96.196.36',
            user='NPSPO_User',
            password='Gaming@NPD',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("成功連接到 MySQL 資料庫")
        return connection
    except Exception as e:
        print(f"連接到 MySQL 失敗：{e}")

# 從 MSSQL 提取資料的函數
def fetch_data_from_mssql(query):
    try:
        with connect_to_mssql() as mssql_conn:
            with mssql_conn.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()
                print("成功提取資料")
                for row in data:
                    print(row)  
                return data
    except Exception as e:
        print(f"提取資料失敗：{e}")

# 創建 MySQL 資料表的函數
def create_table_in_mysql(database_name, table_name):
    try:
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT NOT NULL,
                    user_id INT NOT NULL,
                    Segmentation VARCHAR(255),
                    Segmentation_2 VARCHAR(255),
                    Prject_Year INT,
                    Model_Name VARCHAR(255),
                    answer_time DATE,
                    Territory VARCHAR(100),
                    Country VARCHAR(100),
                    Score INT,
                    VOC_original TEXT,
                    VOC_trans TEXT,
                    len INT,
                    len_range VARCHAR(7) NOT NULL,
                    is_En VARCHAR(5),
                    AsusSurvey_ID INT
                );
                """
                cursor.execute(create_table_query)
                mysql_conn.commit()
                print("成功創建資料表")
    except Exception as e:
        print(f"創建資料表失敗：{e}")

# 清空 MySQL 資料表的函數
def clear_table(database_name, table_name):
    try:
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                cursor.execute(f"DELETE FROM {table_name};")
                mysql_conn.commit()
                print("成功清空資料表")
    except Exception as e:
        print(f"清空資料表失敗：{e}")

# 將資料插入到 MySQL 的函數
def insert_data_into_mysql(database_name, table_name, rows):
    try:
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                insert_query = f"INSERT INTO {table_name} (id, user_id, Segmentation, Segmentation_2, Prject_Year, Model_Name, answer_time, Territory, Country, Score, VOC_original, VOC_trans, len, len_range, is_En, AsusSurvey_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                
                data_to_insert = [
                    (row.id, row.user_id, row.Segmentation, row.Segmentation_2, row.Prject_Year, row.Model_Name, row.answer_time, row.Territory, row.Country, row.Score, row.VOC_original, row.VOC_trans, row.len, row.len_range, row.is_En, row.AsusSurvey_ID) 
                    for row in rows
                ]
                
                cursor.executemany(insert_query, data_to_insert)
                mysql_conn.commit()
                print("成功插入資料")
    except Exception as e:
        print(f"插入資料失敗：{e}")

# 主程式：從 MSSQL 提取資料，創建 MySQL 資料表，並插入資料
def migrate_data(mssql_table, mysql_database, mysql_table):
    try:
        mssql_query = f"SELECT * FROM {mssql_table};"  # 查詢 MSSQL 表的所有資料
        rows = fetch_data_from_mssql(mssql_query)  # 提取 MSSQL 資料
        create_table_in_mysql(mysql_database, mysql_table)  # 創建 MySQL 資料表
        clear_table(mysql_database, mysql_table)  # 清空目標表
        insert_data_into_mysql(mysql_database, mysql_table, rows)  # 插入資料
        print("已完成資料遷移")
    except Exception as e:
        print(f"資料遷移失敗：{e}")

# 執行資料遷移的參數
mssql_table = "nps_2024_focus"  # MSSQL 資料表名稱
mysql_database = "stan01"  # MySQL 資料庫名稱
mysql_table = "NPS"  # MySQL 資料表名稱
migrate_data(mssql_table, mysql_database, mysql_table)  # 執行資料遷移
