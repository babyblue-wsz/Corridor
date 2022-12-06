from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QGridLayout, QFileDialog, QGroupBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Segmentation(QWidget):
    def __init__(self):
        super(Segmentation, self).__init__()
        self.init()
        self.init_layers()

    def init(self):
        self.setFixedWidth(800)
        self.setFixedHeight(300)

    def init_layers(self):
        # 设置整体为一个竖直层
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 设置上中下三个网格层
        top_layout = QGridLayout()
        main_layout.addLayout(top_layout)
        middle_layout = QGridLayout()
        main_layout.addLayout(middle_layout)
        bottom_layout = QGridLayout()
        main_layout.addLayout(bottom_layout)

        # top层用来放两个按钮
        top_layout.setAlignment(Qt.AlignLeft)
        select_image_btn = QPushButton('选择单张图片')
        top_layout.addWidget(select_image_btn, 0, 0)
        select_image_btn.setFixedWidth(100)
        select_image_btn.clicked.connect(self.open_single_file)

        select_images_btn = QPushButton('选择文件夹')
        top_layout.addWidget(select_images_btn, 0, 1)
        select_images_btn.setFixedWidth(100)
        select_images_btn.clicked.connect(self.open_folder)

        # middle层用来放两个QGroupBox，分别放输入图片和输出图片的显示
        input_groupbox = QGroupBox()
        input_groupbox.setTitle('原始图像输入')
        middle_layout.addWidget(input_groupbox, 0, 0)
        input_layout = QVBoxLayout()
        self.input_image = QLabel()
        input_layout.addWidget(self.input_image)
        self.input_image.setFixedWidth(400)
        input_groupbox.setLayout(input_layout)

        output_groupbox = QGroupBox()
        output_groupbox.setTitle('图像输出')
        middle_layout.addWidget(output_groupbox, 0, 1)
        output_layout = QVBoxLayout()
        self.output_image = QLabel()
        output_layout.addWidget(self.output_image)
        self.output_image.setFixedWidth(400)
        output_groupbox.setLayout(output_layout)

    def open_single_file(self):
        file_path = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要上传的图片",  # 标题
            r"d:\\data",  # 起始目录
            "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        file_path = file_path[0]
        self.input_image.setPixmap(QPixmap(file_path))
        # 图片大小与label适应，否则图片可能显示不全
        self.input_image.setScaledContents(True)

    def open_folder(self):
        file_paths = QFileDialog.getExistingDirectory(
            self,  # 父窗口对象
            "选择你要上传的图片",  # 标题
        )
