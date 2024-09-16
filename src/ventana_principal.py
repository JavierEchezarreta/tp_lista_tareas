from ui.interfaz import Ui_ventana_principal
from gestor_de_tareas import GestorDeTareas
from modelo_tareas import ModeloDeTareas
from PySide6.QtWidgets import QMainWindow, QMessageBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ventana_principal()
        self.ui.setupUi(self)

        self.gestor = GestorDeTareas()
        self.modelo = ModeloDeTareas(self.gestor)

        self.ui.lista.setModel(self.modelo)

        self.ui.boton_agregar.clicked.connect(self.agregar_tarea)
        self.ui.boton_completar.clicked.connect(self.completar_tarea)
        self.ui.boton_eliminar.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        descripcion = self.ui.ingresar_tarea_line_edit.text().strip()
        if descripcion:
            try:
                self.modelo.agregar_tarea(descripcion)
                self.ui.ingresar_tarea_line_edit.clear()
            except ValueError as e:
                QMessageBox.warning(self, "Advertencia", str(e))
        else:
            QMessageBox.warning(self, "Advertencia", "La descripción de la tarea no puede estar vacía.")

    def completar_tarea(self):
        index = self.ui.lista.currentIndex()
        if index.isValid():
            self.modelo.completar_tarea(index)

    def eliminar_tarea(self):
        index = self.ui.lista.currentIndex()
        if index.isValid():
            self.modelo.eliminar_tarea(index)