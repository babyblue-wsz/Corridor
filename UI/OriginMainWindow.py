from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class OriginMainWindow(QWidget):
    def __init__(self):
        super(OriginMainWindow, self).__init__()
        self.init()
        self.init_layers()

    def init(self):
        self.setFixedWidth(400)
        self.setFixedHeight(300)

    def init_layers(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        top_layout = QGridLayout()
        main_layout.addLayout(top_layout)

        login_label = QLabel('用户登录')
        top_layout.addWidget(login_label, 0, 0)

        username_label = QLabel('用户名')
        top_layout.addWidget(username_label, 1, 0)
        username_input = QLineEdit()
        username_input.setPlaceholderText("请输入用户名")
        top_layout.addWidget(username_input, 1, 1)

        passwords_label = QLabel('密码')
        top_layout.addWidget(passwords_label, 2, 0)
        passwords_input = QLineEdit()
        passwords_input.setPlaceholderText("请输入密码")
        top_layout.addWidget(passwords_input, 2, 1)

        login_btn = QPushButton('登录')
        top_layout.addWidget(login_btn,  3, 0)
