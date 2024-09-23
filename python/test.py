# 1. 基本的 try-except 結構
try:
    # 嘗試執行的代碼
    x = 10 / 0  # 這裡會產生 ZeroDivisionError
except ZeroDivisionError:
    print("除以零的錯誤！")

# 2. 捕捉特定類型的錯誤
try:
    number = int("abc")  # 嘗試將字符串轉換為整數
except ValueError:
    print("這不是一個有效的數字")

# 3. 捕捉所有異常
try:
    # 嘗試執行的代碼
    x = 10 / 0
except Exception as e:
    print(f"出現錯誤: {e}")

# 4. 使用 finally 塊
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("文件未找到！")
finally:
    print("無論如何，這行代碼都會執行")
    try:
        file.close()
    except NameError:
        # 如果文件未打開，file 變數未定義
        pass

# 5. 使用 else 塊
try:
    result = 10 / 2
except ZeroDivisionError:
    print("除以零的錯誤！")
else:
    print("沒有錯誤，結果是:", result)

# 6. 手動引發錯誤 raise
try:
    x = -1
    if x < 0:
        raise ValueError("負數不是有效的輸入")
except ValueError as e:
    print(e)
finally:
    print("執行完畢，清理工作已完成")
