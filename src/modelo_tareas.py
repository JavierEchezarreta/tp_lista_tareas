from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from gestor_tareas import GestorDeTareas
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.interfaz import Ui_ventana_principal

class ModeloDeTareas(QAbstractListModel):
    def __init__(self, gestor: GestorDeTareas):
        super().__init__()
        self.__gestor = gestor

    def rowCount(self, parent=QModelIndex()):
        return self.__gestor.contar_tareas()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= self.rowCount():
            return None

        tarea = self.__gestor.obtener_tareas()[index.row()]

        if role == Qt.DisplayRole:
            return tarea.mostrar()

        elif role == Qt.FontRole and tarea.es_completada():
            font = QFont()
            font.setStrikeOut(True)
            return font

        return None

    def agregar_tarea(self, descripcion):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__gestor.agregar_tarea(descripcion)
        self.endInsertRows()

    def completar_tarea(self, index):
        if not index.isValid():
            return
        identificadores = self.__gestor.obtener_identificadores()[index.row()]
        self.__gestor.completar_tarea(identificadores)
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.FontRole])

    def eliminar_tarea(self, index):
        if not index.isValid():
            return
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        identificadores = self.__gestor.obtener_identificadores()[index.row()]
        self.__gestor.eliminar_tarea(identificadores)
        self.endRemoveRows()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_ventana_principal()
        self.__ui.setupUi(self)

        self.__gestor = GestorDeTareas()
        self.__modelo = ModeloDeTareas(self.__gestor)

        self.__ui.lista.setModel(self.__modelo)

        self.__ui.boton_agregar.clicked.connect(self.agregar_tarea)
        self.__ui.boton_completar.clicked.connect(self.completar_tarea)
        self.__ui.boton_eliminar.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        descripcion = self.__ui.ingresar_tarea_line_edit.text().strip()
        if descripcion:
            try:
                self.__modelo.agregar_tarea(descripcion)
                self.__ui.ingresar_tarea_line_edit.clear()
            except ValueError as e:
                QMessageBox.warning(self, "Advertencia", str(e))
        else:
            QMessageBox.warning(self, "Advertencia", "La descripción de la tarea no puede estar vacía")

    def completar_tarea(self):
        index = self.__ui.lista.currentIndex()
        if index.isValid():
            try:
                self.__modelo.completar_tarea(index)
            except ValueError as e:
                QMessageBox.warning(self, "Advertencia", "Esa tarea ya fue completada")

    def eliminar_tarea(self):
        index = self.__ui.lista.currentIndex()
        if index.isValid():
            self.__modelo.eliminar_tarea(index)