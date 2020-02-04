from PyQt5.QtWidgets import QApplication
from baiduapi2 import BaiduAPI
from bdtrans import bdtrans
import time
app = QApplication([])
clipboard=app.clipboard()
clipboard.clear()
baiduapi=BaiduAPI()
print("start monitor")
def on_clipboard_change():
    data = clipboard.mimeData()
    time_start=time.time()
    if data.hasText():
        text=data.text()
        print(text)
        finaltext = "\n\n".join(list(map(bdtrans, text.split("\n"))))
        print(finaltext)
        print("start monitor")
    elif data.hasImage():
        im = data.imageData()
        filename = r'C:/dart/download/ImageGrab.png'
        im.save(filename)
        ocrtext = baiduapi.pic2text(filename)
        finaltext = "\n\n".join(list(map(bdtrans, ocrtext.split("\n"))))
        print(finaltext)
        print("总耗时: {:.4} 秒。".format(str(time.time() - time_start)))
        print("start monitor")
clipboard.dataChanged.connect(on_clipboard_change)
app.exec_()