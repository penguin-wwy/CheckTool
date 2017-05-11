from PyQt5.QtWidgets import *

from Check import *
class Manager(QWidget):
    def __init__(self):
        super().__init__()
        self.checking = Check()
        self.checking.connect(self)

        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()

        self.create_check()
        self.file_one()
        self.file_two()
        self.show_value()

        self.main_layout.addWidget(self.check_box, 1)
        self.main_layout.addWidget(self.file_one_box, 1)
        self.main_layout.addWidget(self.file_two_box, 1)
        self.main_layout.addWidget(self.show_box, 4)

        self.resize(550, 530)
        self.center()
        self.setWindowTitle('CheckTool')
        self.setLayout(self.main_layout)
        self.show()

    def center(self):
        # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        qr = self.frameGeometry()
        # 获得屏幕中心
        cp = QDesktopWidget().availableGeometry().center()
        # 矩阵中心设置到屏幕中心
        qr.moveCenter(cp)
        # 移动应用窗口的左上方的点到qr矩形的左上方的点
        self.move(qr.topLeft())

    def file_one(self):
        self.file_one_box = QGroupBox()
        layout = QGridLayout()

        file_btn = QPushButton('选择文件(一)', self)
        layout.addWidget(file_btn, 1, 0)
        file_btn.clicked.connect(self.file_one_show)

        self.file_one_edit = QLineEdit()
        layout.addWidget(self.file_one_edit, 1, 1)

        out_btn = QPushButton('文件一输出', self)
        layout.addWidget(out_btn, 2, 0)
        out_btn.clicked.connect(self.file_one_out)

        self.file_one_box.setLayout(layout)

    def file_two(self):
        self.file_two_box = QGroupBox()
        layout = QGridLayout()

        file_btn = QPushButton('选择文件(二)', self)
        layout.addWidget(file_btn, 1, 0)
        file_btn.clicked.connect(self.file_two_show)

        self.file_two_edit = QLineEdit()
        layout.addWidget(self.file_two_edit, 1, 1)

        out_btn = QPushButton('文件二输出', self)
        layout.addWidget(out_btn, 2, 0)
        out_btn.clicked.connect(self.file_two_out)

        self.file_two_box.setLayout(layout)

    def create_check(self):
        self.check_box = QGroupBox()
        layout = QGridLayout()

        title = QLabel("校验模式选择")
        layout.addWidget(title, 1, 0)

        self.comb = QComboBox(self)
        self.comb.addItem('MD5')
        self.comb.addItem('SHA1')
        self.comb.addItem('SHA256')
        self.comb.addItem('SHA512')
        layout.addWidget(self.comb, 1, 1, 1, 3)

        check_btn = QPushButton('校验', self)
        layout.addWidget(check_btn, 2, 0)
        check_btn.clicked.connect(self.start_check)

        res = QLabel('Result : ')
        layout.addWidget(res, 2, 1)

        self.show_res = QLabel('')
        layout.addWidget(self.show_res, 2, 2)

        self.check_box.setLayout(layout)

    def show_value(self):
        self.show_box = QGroupBox()
        layout = QGridLayout()

        file_one = QLabel('文件一校验值')
        layout.addWidget(file_one, 1, 0)

        self.file_one_show = QTextEdit()
        layout.addWidget(self.file_one_show, 1, 1, 2, 1)

        file_two = QLabel('文件二校验值')
        layout.addWidget(file_two, 3, 0)

        self.file_two_show = QTextEdit()
        layout.addWidget(self.file_two_show, 3, 1, 4, 1)

        self.show_box.setLayout(layout)

    def file_one_show(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\penguin\Desktop')
        if filename[0]:
            self.file_one_edit.setText(filename[0])

    def file_two_show(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\penguin\Desktop')
        if filename[0]:
            self.file_two_edit.setText(filename[0])

    def file_one_out(self):
        res = self.checking.start_check([self.file_one_edit.text()], self.comb.currentText())
        self.file_one_show.setText(res[0][0])

    def file_two_out(self):
        res = self.checking.start_check([self.file_two_edit.text()], self.comb.currentText())
        self.file_two_show.setText(res[0][0])

    def start_check(self):
        #print(self.comb.currentText())
        res = self.checking.start_check([self.file_one_edit.text(), self.file_two_edit.text()],
                                        self.comb.currentText())
        self.file_one_show.setText(res[0][0])
        self.file_two_show.setText(res[0][1])
        if res[1] is True:
            self.show_res.setText('Right')
        else:
            self.show_res.setText('Wrong')