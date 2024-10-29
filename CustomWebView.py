from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import *
from PySide6.QtNetwork import *
from PySide6.QtCore import *

class CustomWebEngineView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)
        
    def createWindow(self, QWebEnginePage_WebWindowType):
        return self
