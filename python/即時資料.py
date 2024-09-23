import twstock as t
import pandas as p

stock = t.realtime.get('00763U')
print(stock['success'])

# 将获取到的股票信息转换为 DataFrame
result = p.DataFrame(stock).T.iloc[1:3]

# 更正 'cloumns' 为 'columns'
result.columns = ['股票代碼', '地區', '股票名稱', '公司全名', '現在時間', '新成交價', '成交量', '累積成交量', '最佳5檔賣出價', '最佳5檔賣出量', '最佳5檔賣出量', '最佳5檔買進量', '開盤價', '最高價', '最低價']

# 输出 DataFrame 的内容
print(result)
