class Tarea:
    def __init__(self, descripcion):
        if not descripcion.strip():
            raise ValueError("No se puede agregar un tarea sin descripcion")
        self.__descripcion = descripcion
        self.__estado = 'pendiente'
        self.__id = id(self)

    def completar(self):
        self.__estado = 'completada'

    def es_completada(self):
        return self.__estado == 'completada'

    def mostrar(self):
        return self.__descripcion

    def identificar(self):
        return self.__id

class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)
        return tarea.identificar()

    def completar_tarea(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                if tarea.es_completada():
                    raise ValueError("Esa tarea ya fue completada")
                else:
                    tarea.completar()
                    return f"Tarea completada exitosamente"
        raise ValueError("Esa tarea no existe")

    def eliminar_tarea(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                self.__tareas.remove(tarea)
                return
        raise ValueError("Esa tarea no existe")

    def tareas_pendientes(self):
        return len([tarea for tarea in self.__tareas if not tarea.es_completada()])

    def tareas_completadas(self):
        return len([tarea for tarea in self.__tareas if tarea.es_completada()])

    def contar_tareas(self):
        return len(self.__tareas)

    def obtener_identificadores(self):
        return [tarea.identificar() for tarea in self.__tareas]

    def obtener_tareas(self):
        return self.__tareas