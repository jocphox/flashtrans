
# getclipdate
# save the clipdate
# if text, save it out; trans or not
# if pic, ocr it or not; then trans or not

# close_all; close_ocr; close_trans; collect_only_text; collect_only_img; collect_only; force_clean;
# collect_close; auto_show;total_memory;
# collect_then_ocr; collect_then_trans; collect_then_ocr_then_trans;
# ocrNow! ; transNow!

from bdtrans import bdtrans
import time
import sys
from UIshow import ShowMainWindow
from PyQt5 import QtWidgets
from baiduapi2 import BaiduAPI
from PIL import ImageGrab, Image #pip install
app = QtWidgets.QApplication([])
clipboard=app.clipboard()
showWin = ShowMainWindow()
baiduapi=BaiduAPI(r'baiduAPIPassword.ini')
clipboard.clear()
def on_clipboard_change():
    time_start = time.time()
    data = clipboard.mimeData()
    if data.hasText():
        ocrtext=data.text()
        showWin.loadoritext(ocrtext)
        finaltext=ocrtext
        showWin.loadtartext(finaltext)
        showWin.labeldefault()
    elif data.hasImage():
        im = ImageGrab.grabclipboard()
        filename = r"./temp/ImageGrab" + '.png'
        im.save(filename)
        ocrtext = baiduapi.pic2text(filename)
        finaltext = "\n\n".join(list(map(bdtrans, ocrtext.split("\n"))))
        showWin.loadimage(filename)
        showWin.loadoritext(ocrtext)
        showWin.loadtartext(finaltext)
        showWin.upstatus(("你可以继续截图了。总耗时: {:.4} 秒。".format(str(time.time() - time_start))))
clipboard.dataChanged.connect(on_clipboard_change)
showWin.show()
sys.exit(app.exec_())
