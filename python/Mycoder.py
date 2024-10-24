# import requests
# from bs4 import BeautifulSoup
# import time
# from selenium import webdriver

# # 设定参数
# activity_id = 24  # 活动ID
# ticket_type = "adult"  # 票种类型 (成人/儿童)
# quantity = 2  # 购买数量

# # Facebook 应用的 App ID 和 App Secret
# app_id = "YOUR_APP_ID"
# app_secret = "YOUR_APP_SECRET"

# # Facebook 用户的 Access Token
# access_token = ""

# def get_access_token():
#     global access_token
#     auth_url = f"https://graph.facebook.com/oauth/access_token?client_id={app_id}&redirect_uri=https://www.tixcraft.com&scope=email&state=1234567890"
#     response = requests.get(auth_url)
#     data = response.json()
#     access_token = data["access_token"]

# def facebook_login():
#     global access_token
#     get_access_token()
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
#     payload = {"grant_type": "authorization_code", "code": "", "redirect_uri": ""}
#     response = requests.post("https://graph.facebook.com/v13.0/oauth/access_token", headers=headers, data=payload)
#     data = response.json()
#     access_token = data["access_token"]
#     return access_token

# def tixcraft_login(access_token):
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json",
#     }
#     payload = {"provider": "facebook"}
#     response = requests.post("https://api.tixcraft.com/v1/users/social-login", headers=headers, json=payload)
#     data = response.json()
#     token = data["token"]
#     return token

# def buy_ticket(token):
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json",
#     }
#     payload = {"activityId": activity_id, "ticketTypeId": ticket_type, "quantity": quantity}
#     response = requests.post("https://api.tixcraft.com/v1/orders", headers=headers, json=payload)
#     data = response.json()
#     order_id = data["orderId"]
#     return order_id

# access_token = facebook_login()
# token = tixcraft_login(access_token)
# order_id = buy_ticket(token)

# print("订单提交成功！", order_id)

##############################################################################################################################################################

# 資料處裡
# import pyodbc

# mssql_conn = pyodbc.connect (
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=APZA002BID;'
#     'UID=NPSPO_User;'
#     'PWD=Gaming@NPD;'
# )

# # 查詢DRIVER
# import pyodbc
# # 獲得已安装的 ODBC 驱动程序列表
# drivers = pyodbc.drivers()

# # print已安裝的驅動
# print("已安装的 ODBC 驅動：")
# for driver in drivers:
#     print(driver)


