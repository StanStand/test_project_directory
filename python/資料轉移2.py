# import pyodbc  # 用於連接 MSSQL 的庫
# import pymysql  # 用於連接 MySQL 的庫

# # MSSQL 資料庫連接參數
# mssql_conn = pyodbc.connect(
#     'DRIVER={SQL Server};'  # 使用 SQL Server 驅動程式
#     'SERVER=你的_mssql_伺服器;'  # MSSQL 伺服器的地址
#     'DATABASE=你的_mssql_資料庫;'  # MSSQL 中的資料庫名稱
#     'UID=你的_mssql_使用者名;'  # 用戶名稱
#     'PWD=你的_mssql_密碼;'  # 密碼
# )

# # MySQL 資料庫連接參數
# mysql_conn = pymysql.connect(
#     host='10.96.196.36',  # MySQL 伺服器的 IP 地址
#     user='NPSPO_User',  # MySQL 的用戶名稱
#     password='Gaming@NPD',  # MySQL 的密碼
#     charset='utf8mb4',  # 字元集設定
#     cursorclass=pymysql.cursors.DictCursor  # 設定游標為字典型別，方便處理資料行
# )

# # 從 MSSQL 提取資料的函數
# def fetch_data_from_mssql(query):
#     cursor = mssql_conn.cursor()  # 使用 MSSQL 連接建立游標
#     cursor.execute(query)  # 執行傳入的 SQL 查詢
#     rows = cursor.fetchall()  # 獲取所有查詢結果，返回一個資料列列表
#     cursor.close()  # 關閉游標
#     return rows  # 返回查詢結果

# # 創建 MySQL 資料庫和資料表的函數
# def create_database_and_table(database_name, table_name):
#     with mysql_conn.cursor() as cursor:  # 使用 MySQL 連接建立游標
#         # 創建資料庫，如果不存在的話
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
#         cursor.execute(f"USE {database_name};")  # 切換到指定的資料庫
        
#         # 創建資料表，假設結構固定
#         create_table_query = f"""
#         CREATE TABLE IF NOT EXISTS {table_name} (
#             id INT AUTO_INCREMENT PRIMARY KEY,  # 自動增量的主鍵
#             metric_name VARCHAR(255),  # 資料名稱欄位
#             metric_value DECIMAL(10, 2),  # 數值欄位，最多 10 位數字，其中 2 位小數
#             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  # 更新時間，預設為當前時間
#         );
#         """
#         cursor.execute(create_table_query)  # 執行創建資料表的 SQL 語句
#     mysql_conn.commit()  # 提交變更，以確保資料庫中已創建資料庫和表

# # 將資料插入到 MySQL 的函數
# def insert_data_into_mysql(database_name, table_name, rows):
#     with mysql_conn.cursor() as cursor:  # 使用 MySQL 連接建立游標
#         cursor.execute(f"USE {database_name};")  # 切換到指定的資料庫
#         for row in rows:  # 遍歷從 MSSQL 獲取的每一行資料
#             # 構建插入語句的參數佔位符和欄位名稱
#             placeholders = ', '.join(['%s'] * len(row))  # 生成 %s 佔位符
#             columns = ', '.join(row.keys())  # 將資料行的欄位名轉換為用逗號分隔的字串
#             # 構建 INSERT INTO 語句
#             sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
#             cursor.execute(sql, list(row.values()))  # 執行 SQL，並將資料插入
#     mysql_conn.commit()  # 提交事務，以確保資料寫入 MySQL

# # 主程式：從 MSSQL 提取資料，創建 MySQL 資料庫和表，並插入資料
# def migrate_data(mssql_query, mysql_database, mysql_table):
#     # 從 MSSQL 提取資料
#     rows = fetch_data_from_mssql(mssql_query)
    
#     # 創建 MySQL 資料庫和表
#     create_database_and_table(mysql_database, mysql_table)
    
#     # 插入資料到 MySQL
#     insert_data_into_mysql(mysql_database, mysql_table, rows)

# # 執行資料遷移的邏輯
# mssql_query = "SELECT * FROM 你的_mssql_表"  # 指定 MSSQL 查詢語句
# mysql_database = "_Myasus"  # 指定 MySQL 資料庫名稱
# mysql_table = "data_quality_metrics"  # 指定 MySQL 資料表名稱
# migrate_data(mssql_query, mysql_database, mysql_table)  # 開始資料遷移

# # 關閉連接
# mssql_conn.close()  # 關閉 MSSQL 連接
# mysql_conn.close()  # 關閉 MySQL 連接


import pyodbc  # 用於連接 MSSQL 的庫
import pymysql  # 用於連接 MySQL 的庫

# MSSQL 資料庫連接參數
def connect_to_mssql():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=APZA001GOD;'
            'DATABASE=ArmouryCrate_New_hive;'
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
                return data
    except Exception as e:
        print(f"提取資料失敗：{e}")

# 創建 MySQL 資料庫和資料表的函數
def create_database_and_table(database_name, table_name):
    try:
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT PRIMARY KEY,  -- 將此行改為不自動增量
                    newver VARCHAR(255),
                    osbuild VARCHAR(255),
                    windows VARCHAR(255),
                    new_osbuild VARCHAR(255),
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
                cursor.execute(f"DELETE FROM {table_name};")  # 清空資料表
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
                insert_query = f"INSERT INTO {table_name} (id, newver, osbuild, windows, new_osbuild) VALUES (%s, %s, %s, %s, %s)"
                
                # 構建要插入的資料列表，手動生成 id 值
                data_to_insert = [
                    (index + 1, row.newver, row.osbuild, row.windows, row.new_osbuild) 
                    for index, row in enumerate(rows)
                ]
                
                cursor.executemany(insert_query, data_to_insert)
                mysql_conn.commit()
                print("成功插入資料")
    except Exception as e:
        print(f"插入資料失敗：{e}")

# 主程式：從 MSSQL 提取資料，創建 MySQL 資料庫和表，並插入資料
def migrate_data(mssql_query, mysql_database, mysql_table):
    try:
        rows = fetch_data_from_mssql(mssql_query)
        create_database_and_table(mysql_database, mysql_table)
        clear_table(mysql_database, mysql_table)  # 清空目標表
        insert_data_into_mysql(mysql_database, mysql_table, rows)
        print("已完成資料遷移")
    except Exception as e:
        print(f"資料遷移失敗：{e}")

# 執行資料遷移的邏輯
mssql_query = "SELECT newver, osbuild, windows, new_osbuild FROM SwInfo_76_Osversion_Build;"
mysql_database = "stan01"
mysql_table = "_Myasus"
migrate_data(mssql_query, mysql_database, mysql_table)



# # 自行替換的內容參數
# MSSQL 伺服器參數：

# 伺服器名稱:


# 'SERVER=APZA001GOD;'
# 替換成你的 MSSQL 伺服器名稱。
# 資料庫名稱:


# 'DATABASE=ArmouryCrate_New_hive;'
# 替換成你要連接的 MSSQL 資料庫名稱。
# MySQL 伺服器參數：

# MySQL 伺服器 IP 地址:


# host='10.96.196.36',
# 替換成你的 MySQL 伺服器 IP 地址。
# 使用者名稱:


# user='NPSPO_User',
# 替換成你的 MySQL 使用者名稱。
# 密碼:


# password='Gaming@NPD',
# 替換成你的 MySQL 密碼。
# MySQL 資料庫和資料表名稱：

# MySQL 資料庫名稱:


# mysql_database = "stan01"
# 替換成你希望使用的 MySQL 資料庫名稱。
# MySQL 資料表名稱:


# mysql_table = "_Myasus"
# 替換成你希望創建或使用的 MySQL 資料表名稱。
# MSSQL 查詢語句：

# 查詢語句:

# mssql_query = "SELECT newver, osbuild, windows, new_osbuild FROM SwInfo_76_Osversion_Build;"
# 替換成你想要執行的 MSSQL 查詢語句。
# 數據庫和表的創建：

# 新表的名稱（在 create_database_and_table 函數內）:

# create_table_query = f"""
# CREATE TABLE IF NOT EXISTS {table_name} (
#     id INT PRIMARY KEY,  -- 將此行改為不自動增量
#     ...
# );
# """
# 根據需要替換 table_name。
# 整體程式碼片段中所有相關內容的列出：
# MSSQL 伺服器名稱和資料庫：


# 'SERVER=APZA001GOD;'  # 替換為 MSSQL 伺服器名稱
# 'DATABASE=ArmouryCrate_New_hive;'  # 替換為 MSSQL 資料庫名稱
# MySQL 伺服器資訊：


# host='10.96.196.36',  # 替換為 MySQL 伺服器 IP 地址
# user='NPSPO_User',  # 替換為 MySQL 使用者名稱
# password='Gaming@NPD',  # 替換為 MySQL 密碼
# MySQL 資料庫和資料表名稱：


# mysql_database = "stan01"  # 替換為 MySQL 資料庫名稱
# mysql_table = "_Myasus"  # 替換為 MySQL 資料表名稱
# MSSQL 查詢語句：


# mssql_query = "SELECT newver, osbuild, windows, new_osbuild FROM SwInfo_76_Osversion_Build;"  # 替換為你的 MSSQL 查詢
# 新建表的 SQL 語句：

# sql

# CREATE TABLE IF NOT EXISTS {table_name} (  # 替換為新表名稱
#     id INT PRIMARY KEY,  # 不自動增量
#     ...
# );



# import pyodbc
# import mysql.connector
# import pandas as pd
# from sqlalchemy import create_engine
# from tqdm import tqdm
# import logging

# # 初始化日志
# logging.basicConfig(level=logging.INFO)

# def connect_to_mssql():
#     try:
#         connection = pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server};'
#             'SERVER=APZA001GOD;'
#             'DATABASE=ArmouryCrate_New_hive;'
#             'Trusted_Connection=yes;'
#         )
#         logging.info("成功連接到 MSSQL 資料庫")
#         return connection
#     except Exception as e:
#         logging.error(f"連接到 MSSQL 失敗：{e}")

# def connect_to_mysql():
#     try:
#         connection = mysql.connector.connect(
#             host='10.96.196.36',
#             user='NPSPO_User',
#             password='Gaming@NPD',
#             database='stan01',
#             charset='utf8mb4'
#         )
#         logging.info("成功連接到 MySQL 資料庫")
#         return connection
#     except Exception as e:
#         logging.error(f"連接到 MySQL 失敗：{e}")

# def create_mysql_engine():
#     engine = create_engine('mysql+mysqlconnector://NPSPO_User:Gaming%40NPD@10.96.196.36:3306/stan01')
#     return engine

# def fetch_mssql_data(query):
#     conn = connect_to_mssql()
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# def fetch_mysql_data(table_name):
#     conn = connect_to_mysql()
#     query = f"SELECT newver FROM {table_name}"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# def upsert_data_to_mysql(df, table_name, engine):
#     temp_table = f"{table_name}_temp"
#     df.to_sql(name=temp_table, con=engine, if_exists='replace', index=False, chunksize=1000)

#     conn = engine.connect()
#     trans = conn.begin()
#     try:
#         columns = df.columns.tolist()
#         update_columns = [f"{col}=VALUES({col})" for col in columns if col != 'newver']
#         insert_sql = f"""
#         INSERT INTO {table_name} ({', '.join(columns)})
#         SELECT {', '.join(columns)} FROM {temp_table}
#         ON DUPLICATE KEY UPDATE {', '.join(update_columns)}
#         """
#         conn.execute(insert_sql)
#         trans.commit()
#         logging.info("資料成功插入或更新到 MySQL")
#     except Exception as e:
#         trans.rollback()
#         logging.error(f"Upsert 操作失敗：{e}")
#     finally:
#         conn.close()
#         with engine.connect() as conn:
#             conn.execute(f"DROP TABLE IF EXISTS {temp_table}")

# def delete_missing_records(mssql_ids, table_name, engine):
#     mssql_id_set = set(mssql_ids)
#     mysql_ids = fetch_mysql_data(table_name)['newver'].tolist()
#     mysql_id_set = set(mysql_ids)
#     ids_to_delete = mysql_id_set - mssql_id_set

#     if ids_to_delete:
#         conn = engine.connect()
#         trans = conn.begin()
#         try:
#             batch_size = 1000
#             ids_to_delete = list(ids_to_delete)
#             for i in tqdm(range(0, len(ids_to_delete), batch_size), desc="Deleting records"):
#                 batch_ids = ids_to_delete[i:i + batch_size]
#                 placeholders = ','.join(['%s'] * len(batch_ids))
#                 delete_sql = f"DELETE FROM {table_name} WHERE newver IN ({placeholders})"
#                 conn.execute(delete_sql, batch_ids)
#             trans.commit()
#             logging.info(f"成功刪除 {len(ids_to_delete)} 條記錄")
#         except Exception as e:
#             trans.rollback()
#             logging.error(f"刪除操作失敗：{e}")
#         finally:
#             conn.close()
#     else:
#         logging.info("沒有需要刪除的記錄")

# def sync_data():
#     query = """
#     SELECT TOP (1000) 
#         [newver], 
#         [osbuild], 
#         [windows], 
#         [new_osbuild] 
#     FROM [ArmouryCrate_New_hive].[dbo].[SwInfo_76_Osversion_Build]
#     """
#     logging.info("從 MSSQL 獲取資料...")
#     mssql_data = fetch_mssql_data(query)
#     logging.info(f"獲取到 {len(mssql_data)} 條記錄")
#     engine = create_mysql_engine()
#     logging.info("同步刪除操作...")
#     delete_missing_records(mssql_data['newver'], "_Myasus", engine)
#     logging.info("執行批量 upsert 操作...")
#     upsert_data_to_mysql(mssql_data, "_Myasus", engine)
#     logging.info("資料同步完成")

# if __name__ == "__main__":
#     sync_data()


import pyodbc
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, text
from tqdm import tqdm
import logging

# 初始化日志
logging.basicConfig(level=logging.INFO)

def connect_to_mssql():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=APZA001GOD;'
            'DATABASE=ArmouryCrate_New_hive;'
            'Trusted_Connection=yes;'
        )
        logging.info("成功連接到 MSSQL 資料庫")
        return connection
    except Exception as e:
        logging.error(f"連接到 MSSQL 失敗：{e}")

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='10.96.196.36',
            user='NPSPO_User',
            password='Gaming@NPD',
            database='stan01',
            charset='utf8mb4'
        )
        logging.info("成功連接到 MySQL 資料庫")
        return connection
    except Exception as e:
        logging.error(f"連接到 MySQL 失敗：{e}")

def create_mysql_engine():
    engine = create_engine('mysql+mysqlconnector://NPSPO_User:Gaming%40NPD@10.96.196.36:3306/stan01')
    return engine

def fetch_mssql_data(query):
    conn = connect_to_mssql()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def fetch_mysql_data(table_name):
    conn = connect_to_mysql()
    query = f"SELECT newver FROM {table_name}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def upsert_data_to_mysql(df, table_name, engine):
    temp_table = f"{table_name}_temp"
    df.to_sql(name=temp_table, con=engine, if_exists='replace', index=False, chunksize=1000)

    conn = engine.connect()
    trans = conn.begin()
    try:
        columns = df.columns.tolist()
        update_columns = [f"{col}=VALUES({col})" for col in columns if col != 'newver']
        insert_sql = f"""
        INSERT INTO {table_name} ({', '.join(columns)})
        SELECT {', '.join(columns)} FROM {temp_table}
        ON DUPLICATE KEY UPDATE {', '.join(update_columns)}
        """
        conn.execute(text(insert_sql))  # 使用 text() 包装 SQL 语句
        trans.commit()
        logging.info("資料成功插入或更新到 MySQL")
    except Exception as e:
        trans.rollback()
        logging.error(f"Upsert 操作失敗：{e}")
    finally:
        conn.close()
        # 使用 text() 包装 DROP TABLE 语句
        with engine.connect() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS {temp_table}"))

def delete_missing_records(mssql_ids, table_name, engine):
    mssql_id_set = set(mssql_ids)
    mysql_ids = fetch_mysql_data(table_name)['newver'].tolist()
    mysql_id_set = set(mysql_ids)
    ids_to_delete = mysql_id_set - mssql_id_set

    if ids_to_delete:
        conn = engine.connect()
        trans = conn.begin()
        try:
            batch_size = 1000
            ids_to_delete = list(ids_to_delete)
            for i in tqdm(range(0, len(ids_to_delete), batch_size), desc="Deleting records"):
                batch_ids = ids_to_delete[i:i + batch_size]
                placeholders = ','.join(['%s'] * len(batch_ids))
                delete_sql = f"DELETE FROM {table_name} WHERE newver IN ({placeholders})"
                conn.execute(text(delete_sql), batch_ids)  # 使用 text() 包装 DELETE 语句
            trans.commit()
            logging.info(f"成功刪除 {len(ids_to_delete)} 條記錄")
        except Exception as e:
            trans.rollback()
            logging.error(f"刪除操作失敗：{e}")
        finally:
            conn.close()
    else:
        logging.info("沒有需要刪除的記錄")

def sync_data():
    query = """
    SELECT TOP (1000) 
        [newver], 
        [osbuild], 
        [windows], 
        [new_osbuild] 
    FROM [ArmouryCrate_New_hive].[dbo].[SwInfo_76_Osversion_Build]
    """
    logging.info("從 MSSQL 獲取資料...")
    mssql_data = fetch_mssql_data(query)
    logging.info(f"獲取到 {len(mssql_data)} 條記錄")
    engine = create_mysql_engine()
    logging.info("同步刪除操作...")
    delete_missing_records(mssql_data['newver'], "_Myasus", engine)
    logging.info("執行批量 upsert 操作...")
    upsert_data_to_mysql(mssql_data, "_Myasus", engine)
    logging.info("資料同步完成")

if __name__ == "__main__":
    sync_data()
