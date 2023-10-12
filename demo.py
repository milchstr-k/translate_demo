# pip install Translator -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install googletrans==4.0.0-rc1
# pip install langid -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install SpeechRecognition -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install PyAudio -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install pocketsphinx -i https://pypi.tuna.tsinghua.edu.cn/simple
from googletrans import Translator
import speech_recognition as sr
#import pyttsx3   # 语音合成库


translator = Translator()
 # 初始化语音识别器  
r = sr.Recognizer()
# 初始化语音合成器  
# engine = pyttsx3.init()  
    
# 语种检测
def languageDetection():
    return

# 文本翻译
def translatorText(text: str, src: str, dest: str):
    translated = translator.translate(text, src=src, dest=dest)
    print(translated.text)
    return translated.text
    # # src为源语言，dest为目标语言，通过googletrans.LANGUAGES查看语言简写
    # translated = translator.translate('hello, world!', src='en', dest='zh-cn')
    # print(translated.text)
    # translated = translator.translate('Hello, where is your hometown from!', src='en', dest='zh-cn')
    # print(translated.text)
    # translated = translator.translate('你好，你老家哪里的!', src='zh-cn', dest='en')
    # print(translated.text)
 
# 语音翻译 pip install SpeechRecognition
def voiceTranslate():

    # 循环接收语音输入，并输出翻译后的语音  
    with sr.Microphone() as source:
        print("请开始说话")
        while True:
            audio = r.listen(source)
            text = r.recognize_google(audio, language="cmn-Hans-CN", show_all=False)
            
            print("输入内容：", text)
            print("类型：", type(text))
            if text == "结束":
                break
            translation = translator.translate(text, src='zh-cn', dest='en').text  
            print("翻译内容：", translation)  
            # engine.say(translation)  
            # engine.runAndWait() 

