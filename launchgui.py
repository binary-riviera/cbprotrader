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
from frames.history_frame import HistoryFrame


class CoinbaseProTrader(QWidget):
    def __init__(self):
        super().__init__()
        self.create_panes()

    def create_panes(self):
        self.title = "Coinbase Pro Trader"

        # TODO: change these to be derived from system variables
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        hbox = QHBoxLayout()

        # history and planned trade frame (all tables or lists)
        top_left_frame = HistoryFrame()
        # top_left_frame.setFrameShape(QFrame.StyledPanel)
        # top_left_frame.setStyleSheet("background-color:blue")

        # chart frame
        top_right_frame = QFrame()
        # top_right_frame.setStyleSheet("background-color:green")

        # config frame
        bottom_left_frame = QFrame()
        # bottom_left_frame.setStyleSheet("background-color:purple")

        # trade and model frame
        bottom_right_frame = QFrame()
        # bottom_right_frame.setStyleSheet("background-color:red")

        # TODO: change all ratios to be derived from config file
        left_pane_splitter = QSplitter(Qt.Vertical)
        left_pane_splitter.addWidget(top_left_frame)
        left_pane_splitter.addWidget(bottom_left_frame)
        left_pane_splitter.setSizes([400, 200])

        right_pane_splitter = QSplitter(Qt.Vertical)
        right_pane_splitter.addWidget(top_right_frame)
        right_pane_splitter.addWidget(bottom_right_frame)
        right_pane_splitter.setSizes([400, 200])

        left_right_pane_splitter = QSplitter(Qt.Horizontal)
        left_right_pane_splitter.addWidget(left_pane_splitter)
        left_right_pane_splitter.addWidget(right_pane_splitter)
        left_right_pane_splitter.setSizes([200, 600])

        hbox.addWidget(left_right_pane_splitter)

        self.setLayout(hbox)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.showMaximized()


def start_interface():
    app = QApplication(sys.argv)
    t = CoinbaseProTrader()
    sys.exit(app.exec_())
