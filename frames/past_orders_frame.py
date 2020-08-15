from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from cbpro.history import get_order_history


class PastOrdersFrame(QTableWidget):
    def __init__(self):
        super().__init__()
        self.frame_name = "Orders"
        self.fill_order_rows()

    def fill_order_rows(self):
        get_order_history()

        self.setRowCount(4)
        self.setColumnCount(2)

        self.setItem(0, 0, QTableWidgetItem("Name"))
        self.setItem(0, 1, QTableWidgetItem("City"))
        self.setItem(1, 0, QTableWidgetItem("Aloysius"))
        self.setItem(1, 1, QTableWidgetItem("Indore"))
        self.setItem(2, 0, QTableWidgetItem("Alan"))
        self.setItem(2, 1, QTableWidgetItem("Bhopal"))
        self.setItem(3, 0, QTableWidgetItem("Arnavi"))
        self.setItem(3, 1, QTableWidgetItem("Mandsaur"))

