import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QWidget


class Calculator(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(width, height)


        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)


        self.input_field = QLineEdit()
        self.input_field.setReadOnly(True)
        self.input_field.setFixedHeight(50)
        self.layout.addWidget(self.input_field)
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)
        self.create_buttons()
        self.current_expression = ""

    def create_buttons(self):
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), 'C': (3, 1), '=': (3, 2), '+': (3, 3),
        }

        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text)
            button.setFixedSize(60, 60)
            self.grid_layout.addWidget(button, pos[0], pos[1])
            button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == "C":
            self.current_expression = ""
        elif text == "=":
            try:
                self.current_expression = str(eval(self.current_expression))
            except Exception:
                self.current_expression = "Error"
        else:
            self.current_expression += text

        self.input_field.setText(self.current_expression)


app = QApplication(sys.argv)
window_width = int(input("Введите ширину окна: "))
window_height = int(input("Введите высоту окна: "))
calculator = Calculator(window_width, window_height)
calculator.show()
sys.exit(app.exec_())