from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, \
    QTableWidget, QTableWidgetItem
from PySide2.QtGui import QFont
from Algoritmos.Poo.Back import Creator_metods, Usuario
import pandas as pd
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analisis y diseño de algoritmos")
        self.setStyleSheet("background-color: #ffffff;")

        layout = QVBoxLayout()

        self.label1 = QLabel("Algoritmo de ordering:")
        self.label1.setFont(QFont("Arial", 12))
        self.label1.setStyleSheet("color: #333;")
        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("1 - BubbleSort")
        self.comboBox1.addItem("2 - BucketSort")
        self.comboBox1.addItem("3 - CountingSort")
        self.comboBox1.addItem("4 - HeapSort")
        self.comboBox1.addItem("5 - InsertionSort")
        self.comboBox1.addItem("6 - MergeSort")
        self.comboBox1.addItem("7 - QuickSort")
        self.comboBox1.addItem("8 - RadixSort")
        self.comboBox1.addItem("9 - SelectionSort")
        self.comboBox1.setFont(QFont("Arial", 12))
        layout.addWidget(self.label1)
        layout.addWidget(self.comboBox1)

        self.label2 = QLabel("Seleccione la columna:")
        self.label2.setFont(QFont("Arial", 12))
        self.label2.setStyleSheet("color: #333;")
        self.comboBox2 = QComboBox()
        self.comboBox2.addItem("mujeres")
        self.comboBox2.addItem("hombres")
        self.comboBox2.addItem("edad")
        self.comboBox2.setFont(QFont("Arial", 12))
        layout.addWidget(self.label2)
        layout.addWidget(self.comboBox2)

        self.button_sort = QPushButton("Información Ordenada")
        self.button_sort.setFont(QFont("Arial", 12))
        self.button_sort.setStyleSheet(
            "background-color: green; color: white; border: none; padding: 10px 24px; cursor: pointer; "
            "border-radius: 5px;")
        layout.addWidget(self.button_sort)

        self.button_unordered = QPushButton("Información sin Ordenar")
        self.button_unordered.setFont(QFont("Arial", 12))
        self.button_unordered.setStyleSheet(
            "background-color: blue; color: white; border: none; padding: 10px 24px; cursor: pointer; "
            "border-radius: 5px;")
        layout.addWidget(self.button_unordered)

        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.table)

        self.label3 = QLabel("Mensaje:")
        self.label3.setFont(QFont("Arial", 12))
        self.label3.setStyleSheet("color: #333;")
        layout.addWidget(self.label3)
        self.lineEdit3 = QLabel()
        self.lineEdit3.setFont(QFont("Arial", 12))
        self.lineEdit3.setStyleSheet("color: #333;")
        layout.addWidget(self.lineEdit3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.button_sort.clicked.connect(self.show_sorted)
        self.button_unordered.clicked.connect(self.show_unsorted)

    def show_sorted(self):

        select_method = self.comboBox1.currentText()
        metodo_elegido = int(select_method.split(" - ")[0])

        colum = self.comboBox2.currentText()

        route = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

        data = requests.get(route)
        data_json = data.json()
        data_df = pd.json_normalize(data_json)

        metodo_nombre = select_method.split(" - ")[1]
        metodo = Usuario.Usuario.get_method(metodo_elegido)
        if metodo is not None:
            creator = Creator_metods.Creator()

            ordering = data_df[colum].astype(int)
            array_sorted = creator.ordenar(metodo_elegido, ordering, colum)[0]

            data_df[colum] = array_sorted
            data_df.sort_values(by=colum, inplace=True)

            self.show_table(data_df,
                            Message=f"Se mostró la información ordenada de la colum '{colum}' utilizando el "
                                    f"método {metodo_nombre}.")

    def show_unsorted(self):
        colums = ["edad", "hombres", "mujeres"]

        route = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

        data = requests.get(route)
        data_json = data.json()
        data_df = pd.json_normalize(data_json)

        self.show_table(data_df[colums], Message="Se mostró la información sin ordenar de todas las columnas.")

    def show_table(self, df, Message):

        self.table.clear()
        self.table.setColumnCount(len(df.columns))
        self.table.setRowCount(len(df))
        self.table.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.table.setItem(i, j, item)
        self.lineEdit3.setText(Message)
