#coding: utf8
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

PDFJS = 'file:///Users/guoruibiao/PycharmProjects/Paper-Manager/conf/web/viewer.html'
# PDFJS = 'file:///usr/share/pdf.js/web/viewer.html'
PDF = 'file:///Users/guoruibiao/PycharmProjects/Paper-Manager/1.pdf'
# PDF = 'file:///tmp/1.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        settings = self.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        # local_url= QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF))
        local_url= QtCore.QUrl.fromUserInput('%s' % (PDF))
        print(local_url)
        self.load(local_url)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())