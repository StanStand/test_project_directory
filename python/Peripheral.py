# import pyodbc  # 用於連接 MSSQL 的庫
# import pymysql  # 用於連接 MySQL 的庫

# # MSSQL 資料庫連接參數
# def connect_to_mssql():
#     try:
#         connection = pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server};'
#             'SERVER=APZA001GOD;'
#             'DATABASE=ArmouryCrate_New_hive_Peripheral;'
#             'Trusted_Connection=yes;'
#         )
#         print("成功連接到 MSSQL 資料庫")
#         return connection
#     except Exception as e:
#         print(f"連接到 MSSQL 失敗：{e}")

# # MySQL 資料庫連接參數
# def connect_to_mysql():
#     try:
#         connection = pymysql.connect(
#             host='10.96.196.36',
#             user='NPSPO_User',
#             password='Gaming@NPD',
#             charset='utf8mb4',
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         print("成功連接到 MySQL 資料庫")
#         return connection
#     except Exception as e:
#         print(f"連接到 MySQL 失敗：{e}")

# # 從 MSSQL 提取資料的函數
# def fetch_data_from_mssql(query):
#     try:
#         with connect_to_mssql() as mssql_conn:
#             with mssql_conn.cursor() as cursor:
#                 cursor.execute(query)
#                 data = cursor.fetchall()
#                 print("成功提取資料")
#                 return data
#     except Exception as e:
#         print(f"提取資料失敗：{e}")

# # 創建 MySQL 資料表的函數
# def create_table_in_mysql(database_name, table_name):
#     try:
#         with connect_to_mysql() as mysql_conn:
#             with mysql_conn.cursor() as cursor:
#                 cursor.execute(f"USE {database_name};")
#                 create_table_query = f"""
#                 CREATE TABLE IF NOT EXISTS {table_name} (
#                     datetime_year INT NULL,
#                     datetime_quarter INT NULL,
#                     datetime_workweek INT NULL,
#                     territory VARCHAR(20) NULL,
#                     ipv4_country VARCHAR(20) NULL,
#                     bg VARCHAR(20) NULL,
#                     segmentation VARCHAR(50) NULL,
#                     model_name VARCHAR(200) NULL,
#                     latest_app_version VARCHAR(20) NULL,
#                     pid VARCHAR(4) NULL,
#                     peripherals_pid VARCHAR(50) NULL,
#                     mouse_seg VARCHAR(20) NULL,
#                     host_vendor VARCHAR(100) NULL,
#                     category VARCHAR(20) NULL,
#                     ac_ver VARCHAR(20) NULL,
#                     html VARCHAR(20) NULL,
#                     status VARCHAR(20) NULL,
#                     effects VARCHAR(20) NULL,
#                     guid_count INT NULL,
#                     dataworkweek VARCHAR(7) NULL
#                 );
#                 """
#                 cursor.execute(create_table_query)
#                 mysql_conn.commit()
#                 print("成功創建資料表")
#     except Exception as e:
#         print(f"創建資料表失敗：{e}")

# # 清空 MySQL 資料表的函數
# def clear_table(database_name, table_name):
#     try:
#         with connect_to_mysql() as mysql_conn:
#             with mysql_conn.cursor() as cursor:
#                 cursor.execute(f"USE {database_name};")
#                 cursor.execute(f"DELETE FROM {table_name};")
#                 mysql_conn.commit()
#                 print("成功清空資料表")
#     except Exception as e:
#         print(f"清空資料表失敗：{e}")

# # 將資料插入到 MySQL 的函數
# def insert_data_into_mysql(database_name, table_name, rows):
#     try:
#         with connect_to_mysql() as mysql_conn:
#             with mysql_conn.cursor() as cursor:
#                 cursor.execute(f"USE {database_name};")
#                 insert_query = f"INSERT INTO {table_name} (datetime_year, datetime_quarter, datetime_workweek, territory, ipv4_country, bg, segmentation, model_name, latest_app_version, pid, peripherals_pid, mouse_seg, host_vendor, category, ac_ver, html, status, effects, guid_count, dataworkweek) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                
#                 # 構建要插入的資料列表
#                 data_to_insert = [
#                     (row.datetime_year, row.datetime_quarter, row.datetime_workweek, row.territory, row.ipv4_country, row.bg,
#                      row.segmentation, row.model_name, row.latest_app_version, row.pid, row.peripherals_pid,
#                      row.mouse_seg, row.host_vendor, row.category, row.ac_ver, row.html, row.status, row.effects,
#                      row.guid_count, row.dataworkweek)
#                     for row in rows
#                 ]
                
#                 cursor.executemany(insert_query, data_to_insert)
#                 mysql_conn.commit()
#                 print("成功插入資料")
#     except Exception as e:
#         print(f"插入資料失敗：{e}")

# # 主程式：從 MSSQL 提取資料，創建 MySQL 表，並插入資料
# def migrate_data(mssql_query, mysql_database, mysql_table):
#     try:
#         rows = fetch_data_from_mssql(mssql_query)
#         create_table_in_mysql(mysql_database, mysql_table)
#         clear_table(mysql_database, mysql_table)
#         insert_data_into_mysql(mysql_database, mysql_table, rows)
#         print("已完成資料遷移")
#     except Exception as e:
#         print(f"資料遷移失敗：{e}")

# # 執行資料遷移的邏輯
# mssql_query = "SELECT * FROM UI_Mouse_Lighting_All;"  # MSSQL 查詢語句
# mysql_database = "stan01"  # MySQL 資料庫名稱
# mysql_table = "Peripheral"  # MySQL 資料表名稱
# migrate_data(mssql_query, mysql_database, mysql_table)  # 執行資料遷移


# import pyodbc
# import pymysql

# # MSSQL 資料庫連接參數
# def connect_to_mssql():
#     try:
#         connection = pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server};'
#             'SERVER=APZA001GOD;'
#             'DATABASE=ArmouryCrate_New_hive_Peripheral;'
#             'Trusted_Connection=yes;'
#         )
#         print("成功連接到 MSSQL 資料庫")
#         return connection
#     except Exception as e:
#         print(f"連接到 MSSQL 失敗：{e}")

# # MySQL 資料庫連接參數
# def connect_to_mysql():
#     try:
#         connection = pymysql.connect(
#             host='10.96.196.36',
#             user='NPSPO_User',
#             password='Gaming@NPD',
#             charset='utf8mb4',
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         print("成功連接到 MySQL 資料庫")
#         return connection
#     except Exception as e:
#         print(f"連接到 MySQL 失敗：{e}")

# # 從 MSSQL 提取資料的函數
# def fetch_data_from_mssql(query):
#     try:
#         print("正在連接到 MSSQL 資料庫...")
#         with connect_to_mssql() as mssql_conn:
#             with mssql_conn.cursor() as cursor:
#                 print("正在執行查詢...")
#                 cursor.execute(query)
#                 data = cursor.fetchall()
#                 print("成功提取資料，行數：", len(data))
                
#                 # 打印出第一行來檢查結構
#                 if data:
#                     print("第一行資料：", data[0])
                
#                 return data
#     except Exception as e:
#         print(f"提取資料失敗：{e}")

# # 創建 MySQL 資料庫和資料表的函數
# def create_database_and_table(database_name, table_name):
#     try:
#         with connect_to_mysql() as mysql_conn:
#             with mysql_conn.cursor() as cursor:
#                 cursor.execute(f"USE {database_name};")
#                 create_table_query = f"""
#                 CREATE TABLE IF NOT EXISTS {table_name} (
#                     datetime_year INT,
#                     datetime_quarter INT,
#                     datetime_workweek INT,
#                     territory VARCHAR(20),
#                     ipv4_country VARCHAR(20),
#                     bg VARCHAR(20),
#                     segmentation VARCHAR(50),
#                     model_name VARCHAR(200),
#                     latest_app_version VARCHAR(20),
#                     pid VARCHAR(4),
#                     peripherals_pid VARCHAR(50),
#                     mouse_seg VARCHAR(20),
#                     host_vendor VARCHAR(100),
#                     category VARCHAR(20),
#                     ac_ver VARCHAR(20),
#                     html VARCHAR(20),
#                     status VARCHAR(20),
#                     effects VARCHAR(20),
#                     guid_count INT,
#                     dataworkweek VARCHAR(7)
#                 );
#                 """
#                 cursor.execute(create_table_query)
#                 mysql_conn.commit()
#                 print("成功創建資料表")
#     except Exception as e:
#         print(f"創建資料表失敗：{e}")

# # 清空 MySQL 資料表的函數，使用 TRUNCATE TABLE
# def clear_table(database_name, table_name):
#     try:
#         with connect_to_mysql() as mysql_conn:
#             with mysql_conn.cursor() as cursor:
#                 cursor.execute(f"USE {database_name};")
#                 cursor.execute(f"TRUNCATE TABLE {table_name};")
#                 mysql_conn.commit()
#                 print("成功清空資料表")
#     except Exception as e:
#         print(f"清空資料表失敗：{e}")

# # 插入資料到 MySQL 的函數
# def insert_data_into_mysql(database_name, table_name, rows):
#     try:
#         if rows is None or len(rows) == 0:
#             print("沒有資料可插入")
#             return
#         with connect_to_mysql() as mysql_conn:
#             with mysql_conn.cursor() as cursor:
#                 cursor.execute(f"USE {database_name};")
#                 insert_query = f"""
#                 INSERT INTO {table_name} (
#                     datetime_year, datetime_quarter, datetime_workweek,
#                     territory, ipv4_country, bg, segmentation, model_name,
#                     latest_app_version, pid, peripherals_pid, mouse_seg, 
#                     host_vendor, category, ac_ver, html, status, effects, 
#                     guid_count, dataworkweek
#                 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
#                 """
#                 # 假設提取到的資料為列表格式而非字典
#                 data_to_insert = [
#                     (
#                         row[0], row[1], row[2], row[3], row[4], row[5], row[6],
#                         row[7], row[8], row[9], row[10], row[11], row[12],
#                         row[13], row[14], row[15], row[16], row[17], row[18], row[19]
#                     ) for row in rows
#                 ]
#                 cursor.executemany(insert_query, data_to_insert)
#                 mysql_conn.commit()
#                 print(f"成功插入 {len(data_to_insert)} 行資料")
#     except Exception as e:
#         print(f"插入資料失敗：{e}")
        
# # 主程式
# def migrate_data(mssql_query, mysql_database, mysql_table):
#     try:
#         print("正在提取資料...")
#         rows = fetch_data_from_mssql(mssql_query)
#         if rows:
#             create_database_and_table(mysql_database, mysql_table)
#             clear_table(mysql_database, mysql_table)
#             insert_data_into_mysql(mysql_database, mysql_table, rows)
#         print("已完成資料遷移")
#     except Exception as e:
#         print(f"資料遷移失敗：{e}")

# # 執行資料遷移
# mssql_query = "SELECT TOP 100 * FROM dbo.UI_Mouse_Lighting_All;"
# mysql_database = "stan01"
# mysql_table = "UI_Mouse_Lighting_All"
# migrate_data(mssql_query, mysql_database, mysql_table)


import pyodbc
import pymysql

# MSSQL 資料庫連接參數
def connect_to_mssql():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=APZA001GOD;'
            'DATABASE=ArmouryCrate_New_hive_Peripheral;'
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

# 創建 MySQL 資料庫和資料表的函數
def create_database_and_table(database_name, table_name):
    try:
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    datetime_year INT,
                    datetime_quarter INT,
                    datetime_workweek INT,
                    territory VARCHAR(20),
                    ipv4_country VARCHAR(20),
                    bg VARCHAR(20),
                    segmentation VARCHAR(50),
                    model_name VARCHAR(200),
                    latest_app_version VARCHAR(20),
                    pid VARCHAR(4),
                    peripherals_pid VARCHAR(50),
                    mouse_seg VARCHAR(20),
                    host_vendor VARCHAR(100),
                    category VARCHAR(20),
                    ac_ver VARCHAR(20),
                    html VARCHAR(20),
                    status VARCHAR(20),
                    effects VARCHAR(20),
                    guid_count INT,
                    dataworkweek VARCHAR(7)
                );
                """
                cursor.execute(create_table_query)
                mysql_conn.commit()
                print("成功創建資料表")
    except Exception as e:
        print(f"創建資料表失敗：{e}")

# 清空 MySQL 資料表的函數，使用 TRUNCATE TABLE
def clear_table(database_name, table_name):
    try:
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                cursor.execute(f"TRUNCATE TABLE {table_name};")
                mysql_conn.commit()
                print("成功清空資料表")
    except Exception as e:
        print(f"清空資料表失敗：{e}")

# 從 MSSQL 分批提取資料的函數
def fetch_batch_from_mssql(query, offset, batch_size):
    try:
        print(f"正在從第 {offset} 筆資料開始提取，批次大小為 {batch_size}")
        with connect_to_mssql() as mssql_conn:
            with mssql_conn.cursor() as cursor:
                # 修改查詢語句，添加 ORDER BY 和 OFFSET
                paginated_query = query + f" ORDER BY [datetime_year] OFFSET {offset} ROWS FETCH NEXT {batch_size} ROWS ONLY;"
                cursor.execute(paginated_query)
                data = cursor.fetchall()
                print(f"成功提取 {len(data)} 筆資料")
                return data
    except Exception as e:
        print(f"提取資料失敗：{e}")
        return []


# 插入資料到 MySQL 的函數
def insert_data_into_mysql(database_name, table_name, rows):
    try:
        if rows is None or len(rows) == 0:
            print("沒有資料可插入")
            return
        with connect_to_mysql() as mysql_conn:
            with mysql_conn.cursor() as cursor:
                cursor.execute(f"USE {database_name};")
                insert_query = f"""
                INSERT INTO {table_name} (
                    datetime_year, datetime_quarter, datetime_workweek,
                    territory, ipv4_country, bg, segmentation, model_name,
                    latest_app_version, pid, peripherals_pid, mouse_seg, 
                    host_vendor, category, ac_ver, html, status, effects, 
                    guid_count, dataworkweek
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                data_to_insert = [
                    (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                        row[7], row[8], row[9], row[10], row[11], row[12],
                        row[13], row[14], row[15], row[16], row[17], row[18], row[19]
                    ) for row in rows
                ]
                cursor.executemany(insert_query, data_to_insert)
                mysql_conn.commit()
                print(f"成功插入 {len(data_to_insert)} 行資料")
    except Exception as e:
        print(f"插入資料失敗：{e}")

# 主程式：分批提取和插入資料
def migrate_data_in_batches(mssql_query, mysql_database, mysql_table, batch_size=1000000):
    offset = 0
    while True:
        rows = fetch_batch_from_mssql(mssql_query, offset, batch_size)
        if not rows:
            print("資料提取完成")
            break
        insert_data_into_mysql(mysql_database, mysql_table, rows)
        offset += batch_size

# 執行資料遷移
mssql_query = "SELECT * FROM dbo.UI_Mouse_Lighting_All"  # 不加 TOP，這樣可以提取所有資料
mysql_database = "stan01"
mysql_table = "UI_Mouse_Lighting_All"
create_database_and_table(mysql_database, mysql_table)
clear_table(mysql_database, mysql_table)
migrate_data_in_batches(mssql_query, mysql_database, mysql_table)
