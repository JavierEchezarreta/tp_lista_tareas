import pytest
from src.gestor_de_tareas import GestorDeTareas, Tarea

@pytest.fixture
def gestor():
    return GestorDeTareas()

def test_agregar_tarea(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    assert gestor.tarea_existe(tarea_1)

def test_agregar_mas_de_una_tarea(gestor):

    gestor.agregar_tarea("tarea_1")
    gestor.agregar_tarea("tarea_2")
    gestor.agregar_tarea("tarea_3")
    assert gestor.contar_tareas() == 3

def test_agregar_mas_de_una_tarea_con_la_misma_descripcion(gestor):

    gestor.agregar_tarea("tarea_1")
    gestor.agregar_tarea("tarea_1")
    assert gestor.contar_tareas() == 2

def test_chequear_estado_pendiente_al_crear_tarea(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    assert not gestor.chequear_tarea_completada(tarea_1)

def test_chequear_estado_tarea_completada(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    gestor.completar_tarea(tarea_1)
    assert gestor.chequear_tarea_completada(tarea_1)

def test_completar_tarea_completada(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    gestor.completar_tarea(tarea_1)
    with pytest.raises(ValueError):
        gestor.completar_tarea(tarea_1)

def test_eliminar_tarea(gestor):

    tarea_1 = gestor.agregar_tarea("tarea_1")
    gestor.eliminar_tarea(tarea_1)
    assert not gestor.tarea_existe(tarea_1)

def test_eliminar_tarea_inexistente(gestor):

    with pytest.raises(ValueError):
        gestor.eliminar_tarea(1)