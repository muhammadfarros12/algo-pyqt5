from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle('Second App')
window.show()

line = QVBoxLayout()
button = QPushButton('Secret Button')
line.addWidget(button, alignment=Qt.AlignCenter)

window.setLayout(line)


def fun_title():
    text = QLabel('You\'r a miracle')
    line.addWidget(text, alignment=Qt.AlignCenter)
    window.setLayout(line)


button.clicked.connect(fun_title)
app.exec_()


