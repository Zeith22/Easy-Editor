from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QPixmap
from PyQt5.QtWidgets import (QApplication, 
                            QWidget,
                            QVBoxLayout,
                            QHBoxLayout,
                            QPushButton,
                            QListWidget,
                            QLabel,
                            QFileDialog,)


app = QApplication([])

window=QWidget()
window.setFixedSize(800,800)
window.setWindowTitle('easy Editor')

filedialog = QFileDialog()

main_layout = QHBoxLayout()
v1_layout = QVBoxLayout()
v2_layout = QVBoxLayout()
h_layout = QHBoxLayout()

browse = QPushButton("Папка")
filelist = QListWidget()
imagelabel = QLabel('?')

left_btn = QPushButton('Вліво')
right_btn = QPushButton('Вправо')
mirror_btn = QPushButton('Зеркало')
sharpness_btn = QPushButton('Резкость')
wb_btn = QPushButton('Ч/Б')
v1_layout.addWidget(browse)
v1_layout.addWidget(filelist)

h_layout.addWidget(left_btn)
h_layout.addWidget(right_btn)
h_layout.addWidget(mirror_btn)
h_layout.addWidget(sharpness_btn)
h_layout.addWidget(wb_btn)

v2_layout.addWidget(imagelabel, alignment=Qt.AlignCenter)
v2_layout.addLayout(h_layout)

main_layout.addLayout(v1_layout)
main_layout.addLayout(v2_layout)

window.setLayout(main_layout)

window.show()
