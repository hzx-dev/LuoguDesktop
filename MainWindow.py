import sys
import webbrowser

from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import *
from PySide6.QtNetwork import *
from PySide6.QtCore import *

import User
import Problem
from CustomWebView import *

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.show()
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1280, 720)

        # 创建一个 QWebEngineView 组件
        self.web_view = CustomWebEngineView(self)
        # self.web_view.page().setUrlRequestInterceptor(self.intercept_request)
        self.web_view.iconChanged.connect(self.on_icon_changed)
        self.web_view.titleChanged.connect(self.setWindowTitle)
        self.web_view.urlChanged.connect(self.on_url_changed)
        self.web_view.change_create_window(self.create_new_window)

        # 设置窗口标题
        self.setWindowTitle("LuoguDesktop")

        # 将中心窗口小部件设置为主窗口的中心窗口小部件
        self.setCentralWidget(self.web_view)
        
        self.load_url("https://www.luogu.com.cn/")

    def load_url(self, url):
        # 加载指定的 URL
        self.web_view.load(url)
        
    def on_icon_changed(self, icon):
        # 当页面图标发生变化时，更新窗口图标
        self.setWindowIcon(icon)
    
    def on_url_changed(self, url: QUrl):
        # 当页面 URL 发生变化时，更新窗口标题
        print(url)
        if ("luogu.com" not in url.host()):
            webbrowser.open(url.toString())
            self.web_view.back()
        if (url.path() == "/auth/login"):
            self.web_view.back()
            self.do_login()
            self.web_view.reload()
        elif (url.path() == "/auth/register"):
            self.web_view.back()
            self.do_reg()
            self.web_view.reload()
        elif ("/problem" in url.path()):
            self.web_view.back()
            self.problem_view = Problem.ProblemView(url.path().split('/')[-1])
            self.problem_view.show()

    def do_login(self):
        login_window = User.LoginWindow(self)
        login_window.exec()
    
    def do_reg(self):
        login_window = User.RegisterWindow(self)
        login_window.exec()
    
    def intercept_request(self, info: QWebEngineUrlRequestInfo):
        print(info)
        
    def create_new_window(self, type):
        self.new_window_main = BrowserWindow()
        return self.new_window_main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec())

