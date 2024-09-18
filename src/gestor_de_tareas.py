import uuid

class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__estado = 'pendiente'
        self.__id = uuid.uuid4()

    def completar(self):
        self.__estado = 'completada'

    def es_completada(self):
        return self.__estado == 'completada'

    def descripcion_coincide(self, descripcion):
        return self.__descripcion == descripcion

    def mostrar(self):
        return self.__descripcion

    def identificar(self):
        return self.__id

    def __eq__(self, otra):
        if isinstance(otra, Tarea):
            return self.__id == otra.__id
        return False

    def __repr__(self):
        return f"Tarea(id={self.__id!r}, descripcion={self.__descripcion!r}, estado={self.__estado!r})"

class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)
        return tarea.identificar()

    def buscar_tarea(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                return tarea.identificar()
        raise ValueError("Esa tarea no existe")

    def completar_tarea(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                if tarea.es_completada():
                    raise ValueError("Esa tarea ya fue completada")
                else:
                    tarea.completar()
                    return f"Tarea completada exitosamente"
        raise ValueError("Esa tarea no existe")

    def tarea_existe(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                return True
        return False

    def eliminar_tarea(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                self.__tareas.remove(tarea)
                return
        raise ValueError("Esa tarea no existe")

    def chequear_tarea_completada(self, tarea_id):
        for tarea in self.__tareas:
            if tarea.identificar() == tarea_id:
                return tarea.es_completada()

    def contar_tareas(self):
        return len(self.__tareas)

    def obtener_descripciones(self):
        return [tarea.mostrar() for tarea in self.__tareas]

    def obtener_identificadores(self):
        return [tarea.identificar() for tarea in self.__tareas]

    def obtener_tareas(self):
        return self.__tareas