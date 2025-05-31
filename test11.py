import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont

class WatermarkWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗体无边框、顶层、透明背景、鼠标穿透
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        # 设置布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # 第一行：固定文字
        self.label1 = QLabel("河西控制中心网管室")
        self.label1.setFont(QFont("Microsoft YaHei", 40, QFont.Bold))
        self.label1.setStyleSheet("color: rgba(255, 255, 255, 180);")
        layout.addWidget(self.label1)

        # 第二行：实时时间
        self.label2 = QLabel("")
        self.label2.setFont(QFont("Microsoft YaHei", 40, QFont.Bold))
        self.label2.setStyleSheet("color: rgba(255, 255, 255, 180);")
        layout.addWidget(self.label2)

        self.setLayout(layout)

        # 定时器更新时间
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

    def update_time(self):
        now = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.label2.setText(now)
        self.adjustSize()

        # 移动窗口到左下角
        screen = QApplication.primaryScreen().geometry()
        x = 30
        y = screen.height() - self.height() - 100
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WatermarkWindow()
    window.show()
    sys.exit(app.exec_())