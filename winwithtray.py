
from PyQt5.QtWidgets import QAction,QActionGroup,QMenu,QSystemTrayIcon,QApplication,QWidget,qApp
from PyQt5.QtGui import QIcon
import configparser
import os.path

def Acts(obj,cbb=True,*arg):
    #为了减少代码量，一次性生成多个Action并附在对象背后
    if len(arg) != 0:
        acts=[]
        for i in range(len(arg)):
            act = QAction(arg[i], obj)
            obj.addAction(act)
            act.setVisible(True)
            act.setCheckable(cbb)
            act.setText(arg[i])
            acts.append(act)
        return acts

def GetCheck(act):
    #为了后续的批量处理，使用map 函数；注意；
    # 如果没有false状态的return，总是出现bug，以后要形成习惯，保证必须有返回。
    if act.isChecked()==True:
        return act.text()
    else:
        return ""


class TrayIcon(QSystemTrayIcon):
    sfun,strans=('functionStatus','translationStatus')
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()
        self.show()

        self.config=configparser.ConfigParser()
        if os.path.exists('config.ini'):
            self.config.read('config.ini')
        else:
            self.config.add_section('currentStatus')
            self.config.set('currentStatus','functionStatus','直译')
            self.config.set('currentStatus','translationStatus','中译英')
            self.config.write(open('config.ini', 'w'))
        self.loadStatus()

    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()

        self.funs=Acts(self.menu,True,"译图","阅图","直译")
        self.menu.addSeparator()
        self.qActions=QActionGroup(self)
        list(map(self.qActions.addAction,self.funs))
        self.menu.addSeparator()
        self.trans = Acts(self.menu, True,"翻译选项", "中译英", "英译中")
        self.qActions2=QActionGroup(self)
        list(map(self.qActions2.addAction,self.trans))
        self.trans[0].setEnabled(False)
        self.menu.addSeparator()
        self.reads = Acts(self.menu, False,"历史存档", "关于", "帮助")
        self.menu.addSeparator()
        self.quitAction = QAction("退出", self, triggered=self.quit)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)
        self.qActions.triggered.connect(self.getStatus)
        self.qActions2.triggered.connect(self.getStatus)
        self.reads[0].triggered.connect(lambda: print("历史存档"))
        self.reads[1].triggered.connect(lambda: print("关于"))
        self.reads[2].triggered.connect(lambda: print("帮助"))

    def other(self):
        self.activated.connect(self.iconClied)
        #把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)
        #把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("ico.ico"))
        self.icon = self.MessageIcon()
        #设置图标

    def getStatus(self):
        sfun="".join(list(map(GetCheck,self.children()[0].actions())))
        strans = "".join(list(map(GetCheck, self.children()[1].actions())))
        self.config.set('currentStatus', 'functionStatus', sfun)
        self.config.set('currentStatus', 'translationStatus', strans)
        self.config.write(open('config.ini', 'w'))

    def loadStatus(self):
        funstatus=self.config.get('currentStatus','functionStatus')
        transtatus = self.config.get('currentStatus', 'translationStatus')
        self.funs[self.statusMap(funstatus)].setChecked(True)
        self.trans[self.statusMap(transtatus)].setChecked(True)
        sfun=funstatus
        strans=transtatus

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()

    def statusMap(self,status):
        if status=="直译" or status=="中译英":
            return 2
        elif status=='译图':
            return 0
        else:
            return 1

    def mClied(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def quit(self):
        qApp.quit()
        sys.exit()

class WindowWithTray(QWidget):
    def __init__(self, parent=None):
        super(WindowWithTray, self).__init__(parent)
        self.ti = TrayIcon(self)
        self.ti.show()
    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = WindowWithTray()
    sys.exit(app.exec_())