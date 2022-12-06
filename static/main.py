import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from UI.Segmentation import Segmentation
from UI.OriginMainWindow import OriginMainWindow
from UI.Corridor import Corridor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
        self.set_menu_bar()

    def init(self):
        self.setWindowTitle('TJRD all in one')
        self.setFixedSize(820, 600)
        self.setWindowIcon(QIcon("/static/images/tongji.jpg"))

        # todo 开发时暂时用语义分割作为主界面
        self.origin_main_window = OriginMainWindow()
        self.setCentralWidget(self.origin_main_window)
        self.segmentationUI = Segmentation()
        self.corridorUI = Corridor()

    def set_menu_bar(self):
        # 创建顶部菜单栏。addMenu()函数创建一级，addAction()函数创建子菜单。
        self.origin = self.menuBar().addMenu('初始')
        self.count = QAction('账户', self)
        self.settings = QAction('设置', self)
        self.origin.addAction(self.count)
        self.origin.addAction(self.settings)
        self.count.triggered.connect(lambda: self.show_child_UI(self.origin_main_window))

        self.functions = self.menuBar().addMenu('工具箱')
        self.segmentation = QAction('语义分割', self)
        self.recognition = QAction('图像识别', self)
        self.corridor = QAction('廊带规划', self)
        self.functions.addAction(self.segmentation)
        self.functions.addAction(self.recognition)
        self.functions.addAction(self.corridor)
        # todo 当切到“设置”UI再切到“语义分割”UI时报错
        self.segmentation.triggered.connect(lambda: self.show_child_UI(self.segmentationUI))

        self.corridor.triggered.connect(lambda: self.show_child_UI(self.corridorUI))

    def show_child_UI(self, childUI):
        self.setCentralWidget(childUI)


if __name__ == "__main__":
    # sys.argv是继续接收命令行指令用的
    app = QApplication(sys.argv)
    main_window = MyWidget()
    main_window.show()
    sys.exit(app.exec())
