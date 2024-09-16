import pytest
from src.gestor_de_tareas import GestorDeTareas

@pytest.fixture
def gestor():
    return GestorDeTareas()

def test_agregar_tarea(gestor):

    gestor.agregar_tarea("Tarea de prueba")
    assert gestor.chequear_tarea("Tarea de prueba")

    gestor.agregar_tarea("Segunda tarea de prueba")
    assert gestor.chequear_tarea("Segunda tarea de prueba")

def test_completar_tarea(gestor):

    gestor.agregar_tarea("Tarea de prueba")
    gestor.completar_tarea("Tarea de prueba")
    assert gestor.chequear_tarea_completada("Tarea de prueba")

    gestor.agregar_tarea("Segunda tarea de prueba")
    gestor.completar_tarea("Segunda tarea de prueba")
    assert gestor.chequear_tarea_completada("Segunda tarea de prueba")

def test_eliminar_tarea(gestor):

    gestor.agregar_tarea("Tarea de prueba")
    gestor.eliminar_tarea("Tarea de prueba")
    assert gestor.chequear_tarea("Tarea de prueba")

    # gestor.agregar_tarea("Segunda tarea de prueba")
    # gestor.eliminar_tarea("Segunda tarea de prueba")
    # with pytest.raises(ValueError):
    #     gestor.chequear_tarea("Segunda tarea de prueba")