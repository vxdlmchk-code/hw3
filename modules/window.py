from PyQt6.QtWidgets import QMainWindow, QFrame, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from modules.app import app 


main_window = QMainWindow()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW  = 800

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

frame_0 = QFrame(parent=main_window)
frame_0.setStyleSheet("background-color: #2b2b2b;")
frame_0.setFixedSize(1024, 800)
vertical_layout = QVBoxLayout()
frame_0.setLayout(vertical_layout)


counter_value = 0


counter_label = QLabel("0")
counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
counter_label.setStyleSheet("font-size: 60px; color: white;")
vertical_layout.addWidget(counter_label)

button_plus = QPushButton("+")
button_minus = QPushButton("-")
button_reset = QPushButton("reset")

vertical_layout.addWidget(button_plus)
vertical_layout.addWidget(button_minus)
vertical_layout.addWidget(button_reset)

def increment_counter():
    global counter_value
    counter_value += 1
    counter_label.setText(str(counter_value))

def decrement_counter():
    global counter_value
    counter_value -= 1
    counter_label.setText(str(counter_value))

def reset_counter():
    global counter_value
    counter_value = 0
    counter_label.setText(str(counter_value))

button_plus.clicked.connect(increment_counter)
button_minus.clicked.connect(decrement_counter)
button_reset.clicked.connect(reset_counter)

main_window.setCentralWidget(frame_0)
main_window.show()