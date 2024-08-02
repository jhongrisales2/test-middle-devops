import pytest
 
class TestIniciales():
    
    def test_inicial(self):
        assert "pruebas" == "pruebas", "Prueba Exitosa !!!"
    
    def test_inicial2(self):
        assert "pruebas" == "prueb4s", "Prueba NO Exitosa :("

class TestOperaciones():
    
    def test_suma(self):
        assert 2 + 3 == 5, "Suma EXITOSA !!!"
    
    def test_resta(self):
        assert 2 - 2 == 1, "Resta NO exitosa :("
