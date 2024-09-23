import mysql.connector
print("mysql.connector has been installed successfully.")
from datetime import datetime

# 連接到 MySQL 資料庫
conn = mysql.connector.connect(
    host='10.96.196.36',
    user='NPSPO_User',
    password='Gaming@NPD',
    database='stan_test'
)
cursor = conn.cursor()

# Speedtest 結果數據
data = {
    "id": "312b6ceb-1d62-442b-861f-5afce40599c9",
    "timestamp": datetime.utcnow(),
    "ping_jitter": 1.333,
    "ping_latency": 4.019,
    "ping_low": 3.961,
    "ping_high": 6.614,
    "download_bandwidth": 2001524,
    "download_bytes": 30743504,
    "download_elapsed": 15004,
    "download_latency_iqm": 221.150,
    "download_latency_low": 5.367,
    "download_latency_high": 677.479,
    "download_latency_jitter": 70.992,
    "upload_bandwidth": 1884830,
    "upload_bytes": 26691834,
    "upload_elapsed": 14991,
    "upload_latency_iqm": 874.181,
    "upload_latency_low": 5.135,
    "upload_latency_high": 2444.526,
    "upload_latency_jitter": 107.735,
    "isp": "New Century InfoComm Tech Co.",
    "internal_ip": "10.96.153.0",
    "external_ip": "118.163.80.132",
    "mac_addr": "14:5A:FC:90:8A:27",
    "vpn": False,
    "server_id": 3967,
    "server_host": "tpv3-1.speedtest.idv.tw",
    "server_port": 8080,
    "server_name": "Chief Telecom",
    "server_location": "Taipei",
    "server_country": "Taiwan",
    "server_ip": "210.61.132.17",
    "result_url": "https://www.speedtest.net/result/c/312b6ceb-1d62-442b-861f-5afce40599c9"
}

# 插入數據
query = """
INSERT INTO speedtest_results (
    id, timestamp, ping_jitter, ping_latency, ping_low, ping_high, 
    download_bandwidth, download_bytes, download_elapsed, 
    download_latency_iqm, download_latency_low, download_latency_high, 
    download_latency_jitter, upload_bandwidth, upload_bytes, 
    upload_elapsed, upload_latency_iqm, upload_latency_low, 
    upload_latency_high, upload_latency_jitter, isp, internal_ip, 
    external_ip, mac_addr, vpn, server_id, server_host, server_port, 
    server_name, server_location, server_country, server_ip, result_url
) VALUES (
    %(id)s, %(timestamp)s, %(ping_jitter)s, %(ping_latency)s, %(ping_low)s, %(ping_high)s, 
    %(download_bandwidth)s, %(download_bytes)s, %(download_elapsed)s, 
    %(download_latency_iqm)s, %(download_latency_low)s, %(download_latency_high)s, 
    %(download_latency_jitter)s, %(upload_bandwidth)s, %(upload_bytes)s, 
    %(upload_elapsed)s, %(upload_latency_iqm)s, %(upload_latency_low)s, 
    %(upload_latency_high)s, %(upload_latency_jitter)s, %(isp)s, %(internal_ip)s, 
    %(external_ip)s, %(mac_addr)s, %(vpn)s, %(server_id)s, %(server_host)s, %(server_port)s, 
    %(server_name)s, %(server_location)s, %(server_country)s, %(server_ip)s, %(result_url)s
)
"""
cursor.execute(query, data)
conn.commit()

# 關閉連接
cursor.close()
conn.close()
