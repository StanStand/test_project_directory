# import pyodbc
# import pymysql

# # 參數設定
# mssql_server = 'APZA002GOD'
# mssql_database = 'GamingPortalTest'
# mssql_user = 'NPSPO_User'
# mssql_password = 'Gaming@NPD'

# mysql_host = '10.96.196.36'
# mysql_user = 'NPSPO_User'
# mysql_password = 'Gaming@NPD'
# mysql_db = 'Nicola'
# table_name = "Consumer_Portal_Dashboard_Summary"
# limit = 1000

# # 連接到 MSSQL 資料庫
# try:
#     mssql_conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         f'SERVER={mssql_server};'
#         f'DATABASE={mssql_database};'
#         f'UID={mssql_user};'
#         f'PWD={mssql_password};'
#     )
#     print("成功連接到 MSSQL 資料庫")
# except Exception as e:
#     print("連接 MSSQL 資料庫時發生錯誤：", e)

# # 使用 mssql_conn.cursor() 操作 MSSQL 資料庫
# mssql_cursor = mssql_conn.cursor()
# mssql_query = f"SELECT TOP {limit} * FROM {table_name};"
# mssql_cursor.execute(mssql_query)
# rows = mssql_cursor.fetchall()

# num_rows = len(rows)
# print(f"提取了 {num_rows} 筆資料")
# print("前 5 筆資料如下：")
# for n, row in enumerate(rows[:5], start=1):
#     print(f'第 {n} 筆資料為: {row}')

# # 連接到 MySQL 資料庫
# try:
#     mysql_conn = pymysql.connect(
#         host=mysql_host,
#         user=mysql_user,
#         password=mysql_password,
#         db=mysql_db,
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print("成功連接到 MySQL 資料庫")
# except Exception as e:
#     print("連接 MySQL 資料庫時發生錯誤：", e)

# mysql_cursor = mysql_conn.cursor()

# # 創建 MySQL 資料表
# create_table_query = f"""
# CREATE TABLE IF NOT EXISTS {table_name} (
#     record_id INT AUTO_INCREMENT PRIMARY KEY,  -- 自增主键
#     MainItem VARCHAR(100),                     -- 其他字段
#     SubItems VARCHAR(100),
#     `set` VARCHAR(100),
#     TabName VARCHAR(100),
#     DataScope VARCHAR(100),
#     Address VARCHAR(300),
#     DashboardUploaded VARCHAR(50),
#     DashboardUpdating VARCHAR(50),
#     Archive VARCHAR(100),
#     DBServer VARCHAR(100),
#     DBName VARCHAR(200),
#     DBTableName TEXT,
#     WorkbookName VARCHAR(200),
#     AutoExtractToken VARCHAR(2000),
#     Freq VARCHAR(100),
#     UpdateTime DATE,
#     PlannerOwner VARCHAR(100),
#     SWOwner VARCHAR(50),
#     TabHide VARCHAR(50),
#     plannerBK_1 VARCHAR(200),
#     PlannerBK_2 VARCHAR(200)
# );
# """
# mysql_cursor.execute(create_table_query)
# print(f"成功創建資料表 {table_name}")

# # 清空 MySQL 資料表中的所有資料
# clear_table_query = f"TRUNCATE TABLE {table_name};"
# mysql_cursor.execute(clear_table_query)
# mysql_conn.commit()
# print(f"成功清空 {table_name} 資料表中的所有資料")

# # 將 MSSQL 提取的資料轉換成 MySQL 格式的 tuple
# data_to_insert = []
# for row in rows:
#     # 將每一行數據轉換成元組，並添加到列表中
#     data_to_insert.append((  # 添加数据到列表
#         row.MainItem,
#         row.SubItems,
#         row.set,
#         row.TabName,
#         row.DataScope,
#         row.Address,
#         row.DashboardUploaded,
#         row.DashboardUpdating,
#         row.Archive,
#         row.DBServer,
#         row.DBName,
#         row.DBTableName,
#         row.WorkbookName,
#         row.AutoExtractToken,
#         row.Freq,
#         row.UpdateTime,
#         row.PlannerOwner,
#         row.SWOwner,
#         row.TabHide,
#         row.plannerBK_1,
#         row.PlannerBK_2
#     ))


# # 插入資料
# for data in data_to_insert:
#     try:
#         # 插入資料的 SQL 查詢，使用 ON DUPLICATE KEY UPDATE
#         insert_query = f"""
# INSERT INTO {table_name} (
#     MainItem, SubItems, `set`, TabName, DataScope, Address, 
#     DashboardUploaded, DashboardUpdating, Archive, DBServer, DBName, 
#     DBTableName, WorkbookName, AutoExtractToken, Freq, UpdateTime, 
#     PlannerOwner, SWOwner, TabHide, plannerBK_1, PlannerBK_2
# ) 
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# ON DUPLICATE KEY UPDATE 
#     SubItems = VALUES(SubItems),
#     `set` = VALUES(`set`),
#     TabName = VALUES(TabName),
#     DataScope = VALUES(DataScope),
#     Address = VALUES(Address),
#     DashboardUploaded = VALUES(DashboardUploaded),
#     DashboardUpdating = VALUES(DashboardUpdating),
#     Archive = VALUES(Archive),
#     DBServer = VALUES(DBServer),
#     DBName = VALUES(DBName),
#     DBTableName = VALUES(DBTableName),
#     WorkbookName = VALUES(WorkbookName),
#     AutoExtractToken = VALUES(AutoExtractToken),
#     Freq = VALUES(Freq),
#     UpdateTime = VALUES(UpdateTime),
#     PlannerOwner = VALUES(PlannerOwner),
#     SWOwner = VALUES(SWOwner),
#     TabHide = VALUES(TabHide),
#     plannerBK_1 = VALUES(plannerBK_1),
#     PlannerBK_2 = VALUES(PlannerBK_2);
# """

#         mysql_cursor.execute(insert_query, data)  # 逐条执行插入查询
#     except Exception as e:
#         print("插入資料時發生錯誤：", e, "數據:", data)

# mysql_conn.commit()
# print(f"成功插入 {len(data_to_insert)} 筆資料")

# # 確保所有連接和游標都被正確關閉
# mssql_cursor.close()
# mssql_conn.close()
# mysql_cursor.close()
# mysql_conn.close()
# print("所有連接已關閉")


import pyodbc
import pymysql

# 參數設定
mssql_server = 'APZA002GOD'
mssql_database = 'GamingPortalTest'
mssql_user = 'NPSPO_User'
mssql_password = 'Gaming@NPD'

mysql_host = '10.96.196.36'
mysql_user = 'NPSPO_User'
mysql_password = 'Gaming@NPD'
mysql_db = 'Nicola'
table_name = "Consumer_Portal_Dashboard_Summary"
limit = 1000

# 連接到 MSSQL 資料庫
try:
    mssql_conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={mssql_server};'
        f'DATABASE={mssql_database};'
        f'UID={mssql_user};'
        f'PWD={mssql_password};'
    )
    print("成功連接到 MSSQL 資料庫")
except Exception as e:
    print("連接 MSSQL 資料庫時發生錯誤：", e)

# 使用 mssql_conn.cursor() 操作 MSSQL 資料庫
mssql_cursor = mssql_conn.cursor()
mssql_query = f"SELECT TOP {limit} * FROM {table_name};"
mssql_cursor.execute(mssql_query)
rows = mssql_cursor.fetchall()

num_rows = len(rows)
print(f"提取了 {num_rows} 筆資料")
print("前 5 筆資料如下：")
for n, row in enumerate(rows[:5], start=1):
    print(f'第 {n} 筆資料為: {row}')

# 連接到 MySQL 資料庫
try:
    mysql_conn = pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        db=mysql_db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("成功連接到 MySQL 資料庫")
except Exception as e:
    print("連接 MySQL 資料庫時發生錯誤：", e)

mysql_cursor = mysql_conn.cursor()

# 創建 MySQL 資料表 (不設置主鍵和自增字段)
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    MainItem VARCHAR(100),                     
    SubItems VARCHAR(100),
    `set` VARCHAR(100),
    TabName VARCHAR(100),
    DataScope VARCHAR(100),
    Address VARCHAR(300),
    DashboardUploaded VARCHAR(50),
    DashboardUpdating VARCHAR(50),
    Archive VARCHAR(100),
    DBServer VARCHAR(100),
    DBName VARCHAR(200),
    DBTableName TEXT,
    WorkbookName VARCHAR(200),
    AutoExtractToken VARCHAR(2000),
    Freq VARCHAR(100),
    UpdateTime DATE,
    PlannerOwner VARCHAR(100),
    SWOwner VARCHAR(50),
    TabHide VARCHAR(50),
    plannerBK_1 VARCHAR(200),
    PlannerBK_2 VARCHAR(200)
);
"""
mysql_cursor.execute(create_table_query)
print(f"成功創建資料表 {table_name}")

# 清空 MySQL 資料表中的所有資料
clear_table_query = f"TRUNCATE TABLE {table_name};"
mysql_cursor.execute(clear_table_query)
mysql_conn.commit()
print(f"成功清空 {table_name} 資料表中的所有資料")

# 將 MSSQL 提取的資料轉換成 MySQL 格式的 tuple
data_to_insert = []
for row in rows:
    data_to_insert.append((
        row.MainItem,
        row.SubItems,
        row.set,
        row.TabName,
        row.DataScope,
        row.Address,
        row.DashboardUploaded,
        row.DashboardUpdating,
        row.Archive,
        row.DBServer,
        row.DBName,
        row.DBTableName,
        row.WorkbookName,
        row.AutoExtractToken,
        row.Freq,
        row.UpdateTime,
        row.PlannerOwner,
        row.SWOwner,
        row.TabHide,
        row.plannerBK_1,
        row.PlannerBK_2
    ))

# 插入資料到 MySQL (不使用 ON DUPLICATE KEY UPDATE，也不使用主鍵)
insert_query = f"""
INSERT INTO {table_name} (
    MainItem, SubItems, `set`, TabName, DataScope, Address, 
    DashboardUploaded, DashboardUpdating, Archive, DBServer, DBName, 
    DBTableName, WorkbookName, AutoExtractToken, Freq, UpdateTime, 
    PlannerOwner, SWOwner, TabHide, plannerBK_1, PlannerBK_2
) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
try:
    mysql_cursor.executemany(insert_query, data_to_insert)
    mysql_conn.commit()
    print(f"成功插入 {len(data_to_insert)} 筆資料")
except Exception as e:
    print("插入資料時發生錯誤：", e)

# 確保所有連接和游標都被正確關閉
mssql_cursor.close()
mssql_conn.close()
mysql_cursor.close()
mysql_conn.close()
print("所有連接已關閉")

