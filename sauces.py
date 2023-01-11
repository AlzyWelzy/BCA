import json
import os
import sys
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Number Extractor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.folder_path = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a label for displaying the selected folder path
        self.folder_path_label = QLabel(self)
        self.folder_path_label.setText("No folder selected.")

        # Create a button for opening the folder selection dialog
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.clicked.connect(self.open_folder_dialog)

        # Create a button to extract numbers
        self.extract_button = QPushButton("Extract Numbers", self)
        self.extract_button.clicked.connect(self.extract_numbers)
        self.extract_button.setDisabled(True)

        # Create a horizontal layout to hold the label and button
        self.browse_layout = QHBoxLayout()
        self.browse_layout.addWidget(self.folder_path_label)
        self.browse_layout.addWidget(self.browse_button)

        # Create a button to save the numbers in json and txt formats
        self.save_json_button = QPushButton("Save as JSON", self)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a label for displaying the selected folder path
        self.folder_path_label = QLabel(self)
        self.folder_path_label.setText("No folder selected.")

        # Create a button for opening the folder selection dialog
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.clicked.connect(self.open_folder_dialog)

        # Create a button to extract numbers
        self.extract_button = QPushButton("Extract Numbers", self)
        self.extract_button.clicked.connect(self.extract_numbers)
        self.extract_button.setDisabled(True)

        # Create a horizontal layout to hold the label and button
        self.browse_layout = QHBoxLayout()
        self.browse_layout.addWidget(self.folder_path_label)
        self.browse_layout.addWidget(self.browse_button)

        # Create a button to save the numbers in json and txt formats
        self.save_json_button = QPushButton("Save as JSON", self)

        # Create a button to save the numbers in json and txt formats
        self.save_json_button = QPushButton("Save as JSON", self)
        self.save_json_button.clicked.connect(self.save_json)
        self.save_json_button.setDisabled(True)

        self.save_txt_button = QPushButton("Save as TXT", self)
        self.save_txt_button.clicked.connect(self.save_txt)
        self.save_txt_button.setDisabled(True)

        self.save_layout = QHBoxLayout()
        self.save_layout.addWidget(self.save_json_button)
        self.save_layout.addWidget(self.save_txt_button)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addLayout(self.browse_layout)
        self.main_layout.addWidget(self.extract_button)
        self.main_layout.addLayout(self.save_layout)

    def open_folder_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.folder_path = str(QFileDialog.getExistingDirectory(
            self, "Select Folder", options=options))
        self.folder_path_label.setText(self.folder_path)
        self.extract_button.setEnabled(True)

        def extract_numbers(self):
            folders = [f for f in os.listdir(self.folder_path) if os.path.isdir(
                os.path.join(self.folder_path, f))]
            self.numbers = []
            for folder in folders:
                match = re.search(r'\[(\d+)\]', folder)
                if match:
                    self.numbers.append(int(match.group(1)))
            self.save_json_button.setEnabled(True)
            self.save_txt_button.setEnabled(True)
            print("Numbers Extracted:", self.numbers)

    def extract_numbers(self):
        folders = [f for f in os.listdir(self.folder_path) if os.path.isdir(
            os.path.join(self.folder_path, f))]
        self.numbers = []
        for folder in folders:
            match = re.search(r'\[(\d+)\]', folder)
            if match:
                self.numbers.append(int(match.group(1)))
        self.save_json_button.setEnabled(True)
        self.save_txt_button.setEnabled(True)
        print("Numbers Extracted:", self.numbers)

    def save_json(self):
        with open("sauces.json", "w") as f:
            json.dump(self.numbers, f)

    def save_txt(self):
        with open("sauces.txt", "w") as f:
            f.write(str(self.numbers))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
