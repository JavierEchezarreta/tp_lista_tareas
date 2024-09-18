from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from gestor_de_tareas import GestorDeTareas
from PySide6.QtGui import QFont

class ModeloDeTareas(QAbstractListModel):
    def __init__(self, gestor: GestorDeTareas):
        super().__init__()
        self._gestor = gestor

    def rowCount(self, parent=QModelIndex()):
        return self._gestor.contar_tareas()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= self.rowCount():
            return None

        tarea = self._gestor.obtener_tareas()[index.row()]

        if role == Qt.DisplayRole:
            return tarea.mostrar()

        elif role == Qt.FontRole and tarea.es_completada():
            font = QFont()
            font.setStrikeOut(True)
            return font

        return None

    def agregar_tarea(self, descripcion):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._gestor.agregar_tarea(descripcion)
        self.endInsertRows()

    def completar_tarea(self, index):
        if not index.isValid():
            return
        identificadores = self._gestor.obtener_identificadores()[index.row()]
        self._gestor.completar_tarea(identificadores)
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.FontRole])

    def eliminar_tarea(self, index):
        if not index.isValid():
            return
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        identificadores = self._gestor.obtener_identificadores()[index.row()]
        self._gestor.eliminar_tarea(identificadores)
        self.endRemoveRows()