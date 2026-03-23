import pytest
from src.classes import Sono, Alimentacao, Hidratacao

def test_score_sono_meta_atingida():
    """Teste de caminho feliz: Meta de sono atingida (>= 7h)"""
    horas = 8
    obj_sono = Sono(horas)
    # Valida se o obj armazena o valor corretamente
    assert obj_sono.get_horasSono() == 8


def test_score_alimentacao_proporcional():
    """Teste de regra de negócio: Nota 4 de 8 deve dar 50% dos pontos da categoria"""
    nota = 4
    meta = 8
    obj_ali = Alimentacao(nota)

    # Simulação da lógica de calculo aplicada no main
    porcentagem = obj_ali.get_notaAlimentacao() / meta
    pontos_categoria = porcentagem * 20

    assert pontos_categoria == 10  # 4 é metade de 8, então ganha 10 pontos de 20


def test_hidratacao_zero():
    """Teste de caso limite: Quando o usuário não bebeu água"""
    agua = 0
    obj_agua = Hidratacao(agua)
    assert obj_agua.get_qntAgua() == 0