import pytest
from src.services import buscarClima

def test_conexaoApiClima():
    #Verifica se a API externa responde corretamente
    resultado = buscarClima("Brasilia")

    #Valida se a API retornou um dicionário e não None
    assert resultado is not None
    assert 'temp' in resultado
    assert isinstance(resultado['temp'], int)