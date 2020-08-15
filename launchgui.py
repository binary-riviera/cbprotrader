import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFrame,
    QSplitter,
    QApplication,
    QLineEdit,
)


class CoinbaseProTrader(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Coinbase Pro Trader"

        # TODO: change these to be derived from system variables
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        hbox = QHBoxLayout()

        top_left_frame = QFrame()
        top_left_frame.setFrameShape(QFrame.StyledPanel)
        top_left_frame.setStyleSheet("background-color:blue")

        top_right_frame = QFrame()
        top_right_frame.setStyleSheet("background-color:green")

        bottom_left_frame = QFrame()
        bottom_left_frame.setStyleSheet("background-color:purple")

        bottom_right_frame = QFrame()
        bottom_right_frame.setStyleSheet("background-color:red")

        left_pane_splitter = QSplitter(Qt.Vertical)
        left_pane_splitter.addWidget(top_left_frame)
        left_pane_splitter.addWidget(bottom_left_frame)
        left_pane_splitter.setSizes([200, 200])

        right_pane_splitter = QSplitter(Qt.Vertical)
        right_pane_splitter.addWidget(top_right_frame)
        right_pane_splitter.addWidget(bottom_right_frame)
        right_pane_splitter.setSizes([200, 200])

        left_right_pane_splitter = QSplitter(Qt.Horizontal)
        left_right_pane_splitter.addWidget(left_pane_splitter)
        left_right_pane_splitter.addWidget(right_pane_splitter)
        left_right_pane_splitter.setSizes([200, 200])

        hbox.addWidget(left_right_pane_splitter)

        self.setLayout(hbox)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.showMaximized()


def start_interface():
    app = QApplication(sys.argv)
    t = CoinbaseProTrader()
    sys.exit(app.exec_())
