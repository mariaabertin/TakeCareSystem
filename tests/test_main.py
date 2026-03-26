import pytest
from src.classes import Sono, Alimentacao, Hidratacao

#CAMINHO FELIZ
def test_score_sono_meta_atingida():
    #Meta de sono atingida (>= 7h)
    horas = 8
    obj_sono = Sono(horas)
    # Valida se o obj armazena o valor corretamente
    assert obj_sono.get_horasSono() == 8


def test_score_alimentacao_proporcional():
    #Teste de regra de negócio: Nota 4 de 8 deve dar 50% dos pontos da categoria
    nota = 4
    meta = 8
    obj_ali = Alimentacao(nota)

    # Simulação da lógica de calculo aplicada no main
    porcentagem = obj_ali.get_notaAlimentacao() / meta
    pontos_categoria = porcentagem * 20

    assert pontos_categoria == 10  #4 é metade de 8, então ganha 10 pontos de 20


def test_hidratacao_zero():
    #Teste de caso limite: Quando o usuário não bebeu água
    agua = 0
    obj_agua = Hidratacao(agua)
    assert obj_agua.get_qntAgua() == 0


# ENTRADA INVÁLIDA OU COMPORTAMENTO INDEVIDO
def test_entrada_negativa_hidratacao():
    #Valida como o sistema lida com valores impossíveis (hidratação negativa)
    agua_negativa = -5
    obj_agua = Hidratacao(agua_negativa)

    # Se a água é negativa, o score de hidratação não deve ser computado (deve ser 0)
    pontos = 0
    if obj_agua.get_qntAgua() > 0:
        pontos = (obj_agua.get_qntAgua() / 3) * 20

    assert pontos == 0


# CASO LIMITE (Boundary Case)
def test_score_alimentacao_limite_minimo():
    #Testa o limite inferior: nota zero na alimentação
    nota_zero = 0
    obj_ali = Alimentacao(nota_zero)

    # Cálculo: (nota / 10) * 20. Se a nota é 0, pontos devem ser 0.
    pontos_categoria = (obj_ali.get_notaAlimentacao() / 10) * 20
    assert pontos_categoria == 0


def test_score_alimentacao_limite_maximo():
    #Testa o limite superior: nota dez na alimentação (pontuação máxima)
    nota_dez = 10
    obj_ali = Alimentacao(nota_dez)

    pontos_categoria = (obj_ali.get_notaAlimentacao() / 10) * 20
    assert pontos_categoria == 20