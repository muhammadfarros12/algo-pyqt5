from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('Third App')
window.resize(300, 300)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

layout_vertical = QVBoxLayout()
layout_horizontal1 = QHBoxLayout()
layout_horizontal2 = QHBoxLayout()
layout_horizontal3 = QHBoxLayout()

layout_horizontal1.addWidget(button1, alignment=Qt.AlignLeft)
layout_horizontal1.addWidget(button2, alignment=Qt.AlignRight)
layout_horizontal2.addWidget(button3, alignment=Qt.AlignCenter)
layout_horizontal3.addWidget(button4, alignment=Qt.AlignLeft)
layout_horizontal3.addWidget(button5, alignment=Qt.AlignRight)

layout_vertical.addLayout(layout_horizontal1)
layout_vertical.addLayout(layout_horizontal2)
layout_vertical.addLayout(layout_horizontal3)

window.setLayout(layout_vertical)

window.show()
app.exec_()
