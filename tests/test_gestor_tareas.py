import pytest
from src.gestor_tareas import GestorDeTareas

@pytest.fixture
def gestor():
    return GestorDeTareas()

def test_agregar_tarea(gestor):

    gestor.agregar_tarea("tarea_1")
    assert gestor.contar_tareas() == 1

def test_agregar_mas_de_una_tarea(gestor):

    gestor.agregar_tarea("tarea_1")
    gestor.agregar_tarea("tarea_2")
    gestor.agregar_tarea("tarea_3")
    assert gestor.contar_tareas() == 3

def test_agregar_tarea_vacia(gestor):

    with pytest.raises(ValueError):
        gestor.agregar_tarea("")
        gestor.agregar_tarea(" ")

def test_completar_tarea(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    gestor.completar_tarea(tarea_1)
    assert gestor.tareas_completadas() == 1

def test_completar_tarea_ya_completada(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    gestor.completar_tarea(tarea_1)
    with pytest.raises(ValueError):
        gestor.completar_tarea(tarea_1)

def test_chequear_cambios_estado_de_las_tareas(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    assert gestor.tareas_pendientes() == 1
    gestor.completar_tarea(tarea_1)
    assert gestor.tareas_completadas() == 1
    gestor.eliminar_tarea(tarea_1)
    assert gestor.tareas_pendientes() == 0
    assert gestor.tareas_completadas() == 0

def test_eliminar_tarea(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    gestor.eliminar_tarea(tarea_1)
    assert gestor.contar_tareas() == 0

def test_ids_unicos(gestor):
    gestor.agregar_tarea("tarea_1")
    gestor.agregar_tarea("tarea_2")
    gestor.agregar_tarea("tarea_3")
    ids = gestor.obtener_identificadores()
    assert len(ids) == len(set(ids))