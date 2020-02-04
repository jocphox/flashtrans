import sys
from PyQt5 import QtWidgets
from PyQt5.Qt import QAction
from PyQt5.QtGui import *
from screenread import Ui_MainWindow
class ShowMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        # 调用父对象的设置方法，这才将所有的东西给传过来了
        self.setupUi(self)
        # 调用自身额外的一些操作，在QtDesigner中无法实现的操作在此处实现
        self.setup_UI()   #翻译
        #self.setTabActive()
        self.tabWidget.setCurrentIndex(0)
        edit2=QAction("Edit",self)
        self.menu_2.addAction(edit2)
        self.menu_2.triggered[QAction].connect(self.load1)
        edit = QAction("Edit", self)
        self.menu_3.addAction(edit)
        self.menu_3.triggered[QAction].connect(self.load2)


    def setup_UI(self):
        pass
    def loadimage(self,filepath):
        sqp=QPixmap(filepath)
        #print(sqp.size())
        self.label.setPixmap(sqp)
        self.label.resize(sqp.width(),sqp.height())
        self.resize(sqp.width()+10,sqp.height()+70)
    def setTabActive(self,number=0):
        self.tabWidget.setCurrentIndex(number)
    def loadoritext(self,oritext):
        self.textEdit_2.setText(oritext)
    def loadtartext(self,tartext):
        self.textEdit.setText(tartext)
    def labeldefault(self):
        self.label.setText("未获得")
    def upstatus(self,information):
        self.statusbar.showMessage(information)
    def load1(self):
        self.loadimage(r".\temp\ImageGrab_20200118_1003_835.png")
    def load2(self):
        self.loadimage(r".\temp\ImageGrab.png")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    showWin = ShowMainWindow()
    showWin.show()
    sys.exit(app.exec_())