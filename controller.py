
from flask import Flask
# request用于接收数据
from flask import request
import textTranslate as textTranslate
# 解决跨域问题
# from flask_cors import CORS


#  创建flask服务对象
app = Flask(__name__)
#  动态解决前端跨域问题
# CORS(app, supports_credentials=True)

#  指定请求路径、方法
@app.route('/log', methods=['GET'])
def reciveLog():
    #get请求数据获取 post请求数据获取request.form.get("log")
    data = request.args.get("log")
    return data

# 文本翻译文本接口
@app.route('/translateText', methods=['POST'])
def translateText():
    text = request.form.get("text")
    if type(text) != str:
        return "文本非字符串类型"
    if len(text) == 0:
        return "文本长度为0"
    data = textTranslate.translatorText(text, "zh-cn", "en")
    return data
    

if __name__== "__main__":
    #  指定端口号和地址
    app.run(port=1234)