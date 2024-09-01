import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.interfaz import Ui_MainWindow
from modelo_tareas import ModeloDeTareas
from gestor_de_tareas import GestorDeTareas

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gestor = GestorDeTareas()
        self.modelo = ModeloDeTareas(self.gestor)

        self.ui.listView.setModel(self.modelo)

        self.ui.pushButton_3.clicked.connect(self.agregar_tarea)
        self.ui.pushButton_2.clicked.connect(self.completar_tarea)
        self.ui.pushButton_4.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        descripcion = self.ui.lineEdit.text().strip()
        if descripcion:
            try:
                self.modelo.agregar_tarea(descripcion)
                self.ui.lineEdit.clear()
            except ValueError as e:
                QMessageBox.warning(self, "Advertencia", str(e))
        else:
            QMessageBox.warning(self, "Advertencia", "La descripción de la tarea no puede estar vacía.")

    def completar_tarea(self):
        index = self.ui.listView.currentIndex()
        if index.isValid():
            self.modelo.completar_tarea(index)

    def eliminar_tarea(self):
        index = self.ui.listView.currentIndex()
        if index.isValid():
            self.modelo.eliminar_tarea(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())