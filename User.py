import webbrowser

from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import *
from PySide6.QtNetwork import *
from PySide6.QtCore import *

class LoginWindow(QDialog):
    
    cookies = {}
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(400, 600)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.web_view = QWebEngineView(self)
        # self.web_view.iconChanged.connect(self.on_icon_changed)
        # self.web_view.titleChanged.connect(self.setWindowTitle)
        self.web_view.urlChanged.connect(self.on_url_changed)
        self.layout.addWidget(self.web_view)
        # 设置窗口标题
        self.setWindowTitle("登录")

        # 将中心窗口小部件设置为主窗口的中心窗口小部件
        
        self.web_view.load(QUrl("https://www.luogu.com.cn/auth/login"))
        self.setLayout(self.layout)
        self.setWindowModality(Qt.WindowModal)
                
        self.show()
    
    def on_url_changed(self, url: QUrl):
        # 当页面 URL 发生变化时，更新窗口标题
        if url.path() != "/auth/login":
            self.close()

class RegisterWindow(QDialog):
    
    cookies = {}
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(400, 600)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.web_view = QWebEngineView(self)
        # self.web_view.iconChanged.connect(self.on_icon_changed)
        # self.web_view.titleChanged.connect(self.setWindowTitle)
        self.web_view.urlChanged.connect(self.on_url_changed)
        self.layout.addWidget(self.web_view)
        # 设置窗口标题
        self.setWindowTitle("注册")

        # 将中心窗口小部件设置为主窗口的中心窗口小部件
        
        self.web_view.load(QUrl("https://www.luogu.com.cn/auth/register"))
        self.setLayout(self.layout)
        self.setWindowModality(Qt.WindowModal)
                
        self.show()
    
    def on_url_changed(self, url: QUrl):
        # 当页面 URL 发生变化时，更新窗口标题
        if url.path() != "/auth/register":
            self.close()
            