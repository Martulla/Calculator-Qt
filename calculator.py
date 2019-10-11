from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.interface()

    def interface(self):
        label_1 = QLabel('Number_1:', self)
        label_2 = QLabel('Number_2:', self)
        label_3 = QLabel('Result:', self)

        label_layout = QGridLayout()
        label_layout.addWidget(label_1, 0, 0)
        label_layout.addWidget(label_2, 0, 1)
        label_layout.addWidget(label_3, 0, 2)

        self.number1edt = QLineEdit()
        self.number2edt = QLineEdit()
        self.resultedt = QLineEdit()

        self.resultedt.readonly = True
        self.resultedt.setToolTip('Enter <b>number</b> and select an operation...')

        label_layout.addWidget(self.number1edt, 1, 0)
        label_layout.addWidget(self.number2edt, 1, 1)
        label_layout.addWidget(self.resultedt, 1, 2)

        add_btn = QPushButton('&Addition', self)
        sub_btn = QPushButton('&Subtraction', self)
        multi_btn = QPushButton('&Multiplication', self)
        div_btn = QPushButton('&Diversion', self)
        end_btn = QPushButton('&End', self)
        end_btn.resize(end_btn.sizeHint())

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(add_btn)
        layout_btn.addWidget(sub_btn)
        layout_btn.addWidget(multi_btn)
        layout_btn.addWidget(div_btn)

        label_layout.addLayout(layout_btn, 2, 0, 1, 3)
        label_layout.addWidget(end_btn, 3, 0, 1, 3)

        self.setLayout(label_layout)

        end_btn.clicked.connect(self.end)

        add_btn.clicked.connect(self.action)
        sub_btn.clicked.connect(self.action)
        multi_btn.clicked.connect(self.action)
        div_btn.clicked.connect(self.action)

        self.number1edt.setFocus()

        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle('Simple Calculator')
        self.show()

    def end(self):
        self.close()

    def closeEvent(self, event):

        res = QMessageBox.question(
            self, 'Message',
            "Are sure it is the end?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if res == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def action(self):
        app_sender = self.sender()

        try:
            number1 = float(self.number1edt.text())
            number2 = float(self.number2edt.text())
            result = ''

            if app_sender.text() == '&Addition':
                result = number1 + number2
            elif app_sender.text() == '&Subtraction':
                result = number1 - number2
            elif app_sender.text() == '&Multiplication':
                result = number1 * number2
            else:
                try:
                    result = round(number1/number2, 2)
                except ZeroDivisionError:
                    QMessageBox.critical(self, "Error!!!", "Cannot be divided by zero")
                    return

            self.resultedt.setText(str(result))

        except ValueError:
            QMessageBox.warning(self, "Error", "Wrong data", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
