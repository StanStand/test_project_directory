import time
import subprocess
import json
from datetime import datetime
import mysql.connector  # type: ignore

# 配置 MySQL 连接
db_config = {
    'host': '10.96.196.36',
    'port': 3306,
    'user': 'NPSPO_User',
    'password': 'Gaming@NPD',
    'database': 'stan01'
}

def perform_speedtest():
    """执行 Speedtest 测试并返回下载速度、上传速度和延迟"""
    try:
        result = subprocess.run(['speedtest-cli', '--json'], capture_output=True, text=True)
        speedtest_data = json.loads(result.stdout)
        download_speed = speedtest_data['download'] / 1_000_000  # 转换为 Mbps
        upload_speed = speedtest_data['upload'] / 1_000_000  # 转换为 Mbps
        ping = speedtest_data['ping']
        return download_speed, upload_speed, ping
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"Speedtest error: {e}")
        return None, None, None

def insert_data(timestamp, download_speed, upload_speed, ping):
    """将数据插入到 MySQL 数据库"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO speedtest_results (timestamp, download_speed, upload_speed, ping)
        VALUES (%s, %s, %s, %s)
        """
        data = (timestamp, download_speed, upload_speed, ping)
        cursor.execute(insert_query, data)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"数据库错误: {err}")
    finally:
        cursor.close()
        conn.close()

def main():
    """主函数，定期执行 Speedtest 并更新数据库"""
    while True:
        print("开始 Speedtest...")
        download_speed, upload_speed, ping = perform_speedtest()
        if download_speed is not None:
            timestamp = datetime.now()
            insert_data(timestamp, download_speed, upload_speed, ping)
            print(f"数据已插入数据库: {timestamp}")
            print(f"下载速度: {download_speed:.2f} Mbps")
            print(f"上传速度: {upload_speed:.2f} Mbps")
            print(f"延迟: {ping:.2f} ms")
        else:
            print("无法获取 Speedtest 数据")
        
        # 每隔 1 分钟更新一次
        time.sleep(60)

if __name__ == "__main__":
    main()

# import mysql.connector

# # 配置 MySQL 连接
# db_config = {
#     'host': '10.96.196.36',
#     'port': 3306,
#     'user': 'NPSPO_User',
#     'password': 'Gaming@NPD',
#     'database': 'stan01'
# }

# # 连接到 MySQL
# try:
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()

#     # 检查表是否存在
#     cursor.execute("SHOW TABLES LIKE 'speedtest_results';")
#     result = cursor.fetchone()
#     if result:
#         print("表 'speedtest_results' 存在。")
#     else:
#         print("表 'speedtest_results' 不存在。")
    
#     # 检查表结构
#     cursor.execute("DESCRIBE speedtest_results;")
#     structure = cursor.fetchall()
#     print("表结构：")
#     for row in structure:
#         print(row)

# except mysql.connector.Error as err:
#     print(f"数据库错误: {err}")

# finally:
#     if conn.is_connected():
#         cursor.close()
#         conn.close()

# import mysql.connector
# from datetime import datetime

# # 配置 MySQL 连接
# db_config = {
#     'host': '10.96.196.36',
#     'port': 3306,
#     'user': 'NPSPO_User',
#     'password': 'Gaming@NPD',
#     'database': 'stan01'
# }

# def insert_data(timestamp, download_speed, upload_speed, ping):
#     """将数据插入到 MySQL 数据库"""
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#         insert_query = """
#         INSERT INTO speedtest_results (timestamp, download_speed, upload_speed, ping)
#         VALUES (%s, %s, %s, %s)
#         """
#         data = (timestamp, download_speed, upload_speed, ping)
#         cursor.execute(insert_query, data)
#         conn.commit()
#         print("数据插入成功")
#     except mysql.connector.Error as err:
#         print(f"数据库错误: {err}")
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def main():
#     timestamp = datetime.now()
#     download_speed = 50.0  # 替换为实际值
#     upload_speed = 10.0    # 替换为实际值
#     ping = 20.0            # 替换为实际值
#     insert_data(timestamp, download_speed, upload_speed, ping)

# if __name__ == "__main__":
#     main()
