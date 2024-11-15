import sys
import webbrowser

from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import *
from PySide6.QtNetwork import *
from PySide6.QtCore import *

import User
import CustomWebView

class ProblemView(QWidget):
    def __init__(self, problem_id="P0001"):
        super().__init__()
        
        self.show()
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1280, 720)
        
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 创建一个 QWebEngineView 组件
        self.web_view = CustomWebView.CustomWebEngineView(self)
        self.web_view.iconChanged.connect(self.on_icon_changed)
        self.web_view.titleChanged.connect(self.setWindowTitle)
        self.web_view.urlChanged.connect(self.on_url_changed)

        # 设置窗口标题
        self.setWindowTitle("Problem View")

        # 将中心窗口小部件设置为主窗口的中心窗口小部件
        # self.setCentralWidget(self.web_view)
        self.layout.addWidget(self.web_view)
        
        self.setLayout(self.layout)

        
        self.load_url(f"https://www.luogu.com.cn/problem/{problem_id}")

    def load_url(self, url):
        # 加载指定的 URL
        self.web_view.load(url)
        
    def on_icon_changed(self, icon):
        # 当页面图标发生变化时，更新窗口图标
        self.setWindowIcon(icon)
    
    def on_url_changed(self, url: QUrl):
        # 当页面 URL 发生变化时，更新窗口标题
        print(url.path())
        if (url.host() != "www.luogu.com.cn" and url.host() != "www.luogu.com"):
            webbrowser.open(url.toString())
            self.web_view.back()
        elif (url.path() == "/auth/login"):
            self.web_view.back()
            self.do_login()
            self.web_view.reload()
        elif (url.path() == "/auth/register"):
            self.web_view.back()
            self.do_reg()
            self.web_view.reload()
        # elif ("/problem" not in url.path()):
        #     self.web_view.back()
        #     self.close()
            
    def do_login(self):
        login_window = User.LoginWindow(self)
        login_window.exec()
    
    def do_reg(self):
        login_window = User.RegisterWindow(self)
        login_window.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProblemView()
    sys.exit(app.exec())

