# 定義可以印出任何訊息的函式
def say(msg):
    print(msg)

# 呼叫上方定義的函式
say("你好")
say("Hi")

# 定義一個可以做加法的函式
def add(n1, n2):
    result = n1 + n2
    print(result)

# 呼叫上方定義的函式
add(3, 4)
add(7, 8)

# 定義一個可以做乘法的函式
# 如果函式內部程式碼有 return，遇到 return 會結束函式執行
def multiply(n1, n2):
    print(n1 * n2)
    return n1 * n2

# 呼叫函式並將結果加總
value = multiply(3, 4) + multiply(10, 5)  # (3*4)+(10*5)
print(value)

# 程式包裝範例：計算1到max之間的總和
def calculate(max_value):
    total_sum = 0
    for n in range(1, max_value + 1):
        total_sum += n
    print(total_sum)

# 呼叫函式，並傳入不同的最大值
calculate(10)  # 計算1到10的總和
calculate(20)  # 計算1到20的總和

# 定義函式 power，設置 exponent 的預設值為 0
def power(base, exp=0):
    return base ** exp

# 呼叫函式，使用自訂參數
result1 = power(3, 2)  # 計算 3 的 2 次方
print(result1)         # 輸出: 9

# 呼叫函式，使用預設值
result2 = power(4)     # 計算 4 的 0 次方 (預設值)
print(result2)         # 輸出: 1

# 使用參數名稱對應來呼叫函式
def divide(n1, n2):
    print(n1 / n2)

# 呼叫函式，傳入不同的參數順序
divide(2, 4)          # 2除以4
divide(n2=2, n1=4)    # 4除以2

# 無限/不定參數範例：計算平均值
def avg(*ns):
    total_sum = 0
    for n in ns:
        total_sum += n
    print(total_sum / len(ns))  # 計算平均值

# 呼叫函式，傳入不同數量的參數
avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)

# 定義多個函式範例
def greet(): 
    print("嗨，大家好")

def greet_with_name(name):
    print(f"嗨，{name}你好")

def greet_with_name_and_age(name, age):
    print(f"嗨，{name}，今天是你{age}歲生日")

# 呼叫不同版本的問候函式
greet()
greet_with_name("小恩")
greet_with_name_and_age("小恩", 22)

# 計算總金額，使用全域變數和區域變數
discount = 0.9
def total_amount(price, shipping_fee = 50):
    return int(price * discount + shipping_fee)
    print("此行會被忽略")
# 呼叫函式並顯示總金額
print(f"總金額為{total_amount(price=1000, shipping_fee = 80)}元")
