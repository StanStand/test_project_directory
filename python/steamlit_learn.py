import streamlit as st
import numpy as np

st.title('您好')
st.write("我是一個字串內容")
k=999
st.write(k)

dataframe = np.random.randn(10,20)
st.write(dataframe)
k
dataframe

#網頁標題
st.markdown("這是一個示範Streamlit網頁")
st.markdown('''
            :red[Streamlit] :orange[can] :green[write] :blue[text] :gray[pretty] :gray[pretty] :rainbow[colors].''')
# 主標題
st.title("歡迎回來")
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# 標頭
st.header("這是一個標頭", divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

#圖片說明
st.caption('這是一張圖片拉')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# 顯示程式碼  
st.code('print("你好")')

code = '''def hello():
    print("Hello, Streamlit")'''
st.code(code, line_numbers=True)
st.code(code, language="python")

# 文字 
st.text('這裡是我我輸入的文字內容')

# 數學 LaTex 表達式
st.latex(r"e^{i\pi} + 1 = 0")

st.latex(r'''
a + ar a r^2 + a + r^3 + \cdots + a r^{n-1}) = 
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

# 分隔線
st.divider()
st.write("慘了，我被夾在分隔線中了!")
st.divider()

#添加中文註解
st.write("希望以上這些有助於建立令人印象深刻的Streamlit網頁!")