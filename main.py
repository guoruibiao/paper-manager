# coding: utf8

import os
import sys
import fitz
import shutil
from PyQt5.QtGui import QIcon, QCursor, QImage, QPixmap, QTransform
from PyQt5.QtCore import QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox
from PyQt5.QtCore import QStringListModel, QPoint
from PyQt5 import QtWebEngineWidgets
from ui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self._window_autoresize()
        self._replace_label_to_webview()

        # 初始化组件内容
        self._init_models()

        # 绑定各种事件
        self._bind_actions()

    def _init_models(self):
        self.listModel = QStringListModel()
        self.treeView.setModel(self.listModel)

        self.listModel.setStringList([
            "/tmp/1.pdf",
            "/tmp/2-andsadsadasdsadsadsadasdsadsd.pdf",
            "/tmp/语义相似度计算.pdf",
            "/tmp/Usin g Informatio n Conten t t o Evaluat e Semanti c Similarit y i n aTaxonom.pdf",
            "/tmp/5.pdf",
        ])
        pass

    def _bind_actions(self):
        # PDF 区域加上选中文本
        # self.label.page().selectionChanged.connect(self._selected)
        self.label.selectionChanged.connect(self._selected)

        # 笔记区事件响应
        self.textEdit.textChanged.connect(self._text_changed)

        # 树点击事件
        self.treeView.clicked.connect(self._tree_clicked)

    def _tree_clicked(self, item):
        print(item.row())
        self.statusbar.showMessage("当前点击到了第{}个元素".format(item.row()+1))

    def _text_changed(self):
        text = self.textEdit.toPlainText()
        print(text)


    def _selected(self):
        text = self.label.selectedText()
        print(text)
        self.textBrowser_3.setText(text)

    def _window_autoresize(self):
        # 自适应
        desktop = QApplication.desktop()
        screen = desktop.screenGeometry()
        self.resize(screen.width(), screen.height())

    def _replace_label_to_webview(self):
        rect = self.label.geometry()
        print(rect)
        self.label = QtWebEngineWidgets.QWebEngineView(self.scrollAreaWidgetContents)
        self.label.setGeometry(rect)
        settings = self.label.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        # settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        PDF = 'file:///Users/guoruibiao/PycharmProjects/Paper-Manager/1.pdf'
        self.label.load(QtCore.QUrl.fromUserInput(PDF))
        self.label.setObjectName("PDF Viewer")

    def loadpdf(self):
        filename = "1.pdf"
        doc = fitz.open(filename)
        page_one = doc.loadPage(0)
        # 将第一页转换为Pixmap
        page_pixmap = page_one.getPixmap()
        # 将Pixmap转换为QImage
        image_format = QImage.Format_RGBA8888 if page_pixmap.alpha else QImage.Format_RGB888
        page_image = QImage(page_pixmap.samples, page_pixmap.width,
                            page_pixmap.height, page_pixmap.stride, image_format)
        width = page_image.width()
        height = page_image.height()
        # QImage 转为QPixmap
        pix = QPixmap.fromImage(page_image)
        trans = QTransform()
        new = pix.transformed(trans)
        self.label.setScaledContents(True)
        self.label.setPixmap(new)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.setWindowTitle("泰戈尔的论文管理器")
    win.show()
    sys.exit(app.exec_())
