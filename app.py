from flask import Flask
app=Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/") # 函式的裝飾 (Decorator) :以函式為基礎,提供附加的功能
def home():
    return "Hello 廢物! 今天吃什麼?!"
@app.route("/test")

def test():
    return "小威嫩嫩還在睡阿? 吃鍋貼好了!"
if __name__=="__main__": # 如果以主程式執行
    app.run() # 立刻啟動伺服器