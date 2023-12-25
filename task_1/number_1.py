from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('First App')
# window.move(900, 100)
# window.resize(500, 200)
window.show()

line = QHBoxLayout()
title = QLabel('Hello World!')
line.addWidget(title, alignment=Qt.AlignHCenter)
window.setLayout(line)

app.exec_()
