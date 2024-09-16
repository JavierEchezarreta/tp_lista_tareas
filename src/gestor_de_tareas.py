class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__estado = 'pendiente'

    def completar(self):
        self.__estado = 'completada'

    def es_completada(self):
        return self.__estado == 'completada'

    def descripcion_coincide(self, descripcion):
        return self.__descripcion == descripcion

    def mostrar(self):
        return self.__descripcion

class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        if any(tarea.descripcion_coincide(descripcion) for tarea in self.__tareas):
            raise ValueError("La tarea ya existe.")
        self.__tareas.append(Tarea(descripcion))

    def buscar_tarea(self, descripcion):
        for tarea in self.__tareas:
            if tarea.descripcion_coincide(descripcion):
                return tarea
        raise ValueError("Esa tarea no existe")

    def completar_tarea(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        tarea.completar()

    def chequear_tarea(self, descripcion):
        if self.buscar_tarea(descripcion):
            return True
        else:
            return False

    def eliminar_tarea(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        self.__tareas.remove(tarea)

    def chequear_tarea_completada(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        return tarea.es_completada()

    def contar_tareas(self):
        return len(self.__tareas)

    def obtener_descripciones(self):
        return [tarea.mostrar() for tarea in self.__tareas]

    def obtener_tareas(self):
        return self.__tareas