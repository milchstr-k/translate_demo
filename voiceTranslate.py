# 语音翻译
import speech_recognition as sr
import textTranslate

 # 初始化语音识别器  
r = sr.Recognizer()

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
            translation = textTranslate.translator.translate(text, src='zh-cn', dest='en').text  
            print("翻译内容：", translation)  
            # engine.say(translation)  
            # engine.runAndWait() 
