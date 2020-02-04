import time
import sys
import os
import re
import bdtrans
import random
import time
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip  # 引入模块

def cppv(toLang='zh'):
    finaltext = ""
    tmp_value="" # 初始化（应该也可以没有这一行，感觉意义不大。但是对recent_value的初始化是必须的）
    while True:
        tmp_value = pyperclip.paste() 			# 读取剪切板复制的内容
        try:
            if tmp_value != finaltext and tmp_value != 'trans_result':				 #如果检测到剪切板内容有改动，那么就进入文本的修改              
                time_start=time.time()
                text = str.strip(tmp_value)     
                if toLang=='en':
                    print("...in translation...")
                    # finaltext = "\n\n".join(list(map(bdtrans.bdtransen, text.split("\n"))))
                    finaltext=text + str(random.randint(0,100))
                else:
                    print("...翻译中...")
                    # finaltext = "\n\n".join(list(map(bdtrans.bdtranscn, text.split("\n"))))
                    finaltext = text + str(random.randint(0, 100))
                print(text)
                print(finaltext)
                if type(finaltext) != "NoneType":  
                    pyperclip.copy(finaltext)							#将修改后的文本写入系统剪切板中
                #recent_value=tmp_value
                print("总耗时: {:.4} 秒。".format(str(time.time() - time_start)))
            time.sleep(0.01)
        except:  # 如果有ctrl+c，那么就退出这个程序。  （不过好像并没有用。无伤大雅）
            pass
if __name__ == '__main__':
    cppv('en')