from PyQt5.QtWidgets import QApplication
from baiduapi2 import BaiduAPI
from bdtrans import bdtrans
import pyperclip
import time
import tkinter

app = QApplication([])
clipboard=app.clipboard()
clipboard.clear()
baiduapi=BaiduAPI(r'C:/dart/download/baiduAPIPassword.ini')
root=tkinter.Tk()
root.attributes("-toolwindow", 1)
root.wm_attributes('-topmost',1)
txt = tkinter.Text(root)
txt.pack()
def on_clipboard_change():
    data = clipboard.mimeData()
    time_start=time.time()
    global txt
    if data.hasText():
        txt.delete(0.0,"end")
        text=data.text()
        finaltext = "\n\n".join(list(map(bdtrans, text.split("\n"))))
        txt.insert("insert",finaltext)
    elif data.hasImage():
        im = data.imageData()
        filename = r'C:/dart/download/ImageGrab.png'
        im.save(filename)
        ocrtext = baiduapi.pic2text(filename)
        finaltext = "\n\n".join(list(map(bdtrans, ocrtext.split("\n"))))
        txt.delete(0.0, tkinter.END)
        txt.insert("insert", finaltext)
        print("总耗时: {:.4} 秒。".format(str(time.time() - time_start)))
clipboard.dataChanged.connect(on_clipboard_change)
def readabout(filepath):
    with open(filepath, 'r', encoding='UTF-8') as ft:
        return "\n".join(ft.readlines())

txt.insert("insert",readabout(r'C:/dart/download/about.txt'))
root.mainloop()
app.exec_()