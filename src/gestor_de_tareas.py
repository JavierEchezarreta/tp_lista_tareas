class Tarea:
    def __init__(self, descripcion):
        self._descripcion = descripcion
        self._estado = 'pendiente'

    def completar(self):
        self._estado = 'completada'

    def es_completada(self):
        return self._estado == 'completada'

    def descripcion_coincide(self, descripcion):
        return self._descripcion == descripcion


class GestorDeTareas:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, descripcion):
        self._tareas.append(Tarea(descripcion))

    def buscar_tarea(self, descripcion):
        for tarea in self._tareas:
            if tarea.descripcion_coincide(descripcion):
                return tarea
        raise ValueError("Esa tarea no existe")

    def completar_tarea(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        tarea.completar()

    def eliminar_tarea(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        self._tareas.remove(tarea)

    def tarea_completada(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        return tarea.es_completada()