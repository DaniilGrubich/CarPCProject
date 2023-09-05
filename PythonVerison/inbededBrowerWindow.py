from threading import Thread

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

def run_qt_app():
    app = QApplication([])
    view = QWebEngineView()

    # Set the window flags to remove the title bar.
    view.setWindowFlags(Qt.FramelessWindowHint)

    url = QUrl("http://127.0.0.1:5000")
    # url = QUrl("http://127.0.0.1:5500/FrontEnd/")

    view.setUrl(url)
    view.showMaximized()  # Makes the window start maximized


    # Enter the application's main loop
    app.exec_()

def launchBrowser():
    qt_thread = Thread(target=run_qt_app)
    qt_thread.start()
