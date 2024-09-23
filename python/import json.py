import json
import mysql.connector

# 读取 JSON 文件
with open('C:\\Users\\stan_liao\\Downloads\\speedtest_results.json', 'r') as file:
    data = json.load(file)

# 连接到 MySQL 数据库
conn = mysql.connector.connect(
    host='localhost',          # 或者使用服务器的 IP 地址，如果 MySQL 运行在远程服务器上
    user='NPSPO_User',         # MySQL 用户名
    password='Gaming@NPD',     # MySQL 密码
    database='stan_test'       # 数据库名称
)

# 创建一个游标对象
cursor = conn.cursor()

# 插入数据到 MySQL 表
cursor.execute("""
    INSERT INTO speedtest_results (id, timestamp, ping_latency, ping_jitter, download_bandwidth, upload_bandwidth, isp, server_name, server_location, server_country, external_ip)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (
    data['result']['id'],
    data['timestamp'],
    data['ping']['latency'],
    data['ping']['jitter'],
    data['download']['bandwidth'],
    data['upload']['bandwidth'],
    data['isp'],
    data['server']['name'],
    data['server']['location'],
    data['server']['country'],
    data['interface']['externalIp']
))

# 提交事务
conn.commit()

# 关闭连接
cursor.close()
conn.close()
