class Sono:
    def __init__(self, horasSono):
        self.horasSono = horasSono

    def get_horasSono(self):
        return self.horasSono

    def set_horasSono(self, newHrSono):
        self.horasSono = newHrSono


class Treino:
    def __init__(self, fezExercicio):
        self.fezExercicio = fezExercicio

    def get_fezExercicio(self):
        return self.fezExercicio

    def set_fezExercicio(self, newFezExercicio):
        self.fezExercicio = newFezExercicio


class Alimentacao:
    def __init__(self, notaAlimentacao):
        self.notaAlimentacao = notaAlimentacao

    def get_notaAlimentacao(self):
        return self.notaAlimentacao

    def set_notaAlimentacao(self, newNotaAlimentacao):
        self.notaAlimentacao = newNotaAlimentacao


class Hidratacao:
    def __init__(self, qntAgua):
        self.qntAgua = qntAgua

    def get_qntAgua(self):
        return self.qntAgua

    def set_qntAgua(self, newQntAgua):
        self.qntAgua = newQntAgua


class Leitura:
    def __init__(self, leuLivro, qntPag):
        self.leuLivro = leuLivro
        self.qntPag = qntPag

    def get_leuLivro(self):
        return self.leuLivro

    def get_qntPag(self):
        return self.qntPag

    def set_leuLivro(self, newLeuLivro):
        self.leuLivro = newLeuLivro

    def set_qntPag(self, newQntPag):
        self.qntPag = newQntPag
