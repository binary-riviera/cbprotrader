from PyQt5.QtWidgets import QTabWidget, QWidget
from frames.past_orders_frame import PastOrdersFrame


class HistoryFrame(QTabWidget):
    def __init__(self):
        super().__init__()
        self.create_tabs()

    def create_tabs(self):
        past_orders = PastOrdersFrame()
        tab2 = QWidget()
        tab3 = QWidget()
        self.addTab(past_orders, past_orders.frame_name)
        self.addTab(tab2, "Bar")
        self.addTab(tab3, "Gloo")
