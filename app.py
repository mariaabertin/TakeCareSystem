from flask import Flask, render_template, request
from src.classes import Sono, Treino, Alimentacao, Hidratacao, Leitura
from src.services import buscarClima

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    clima = buscarClima("Brasilia")
    score = 0
    exibir_resultado = False

    if request.method == 'POST':
        exibir_resultado = True
        # Coletando os dados do formulário
        hr_sono = float(request.form.get('horas', 0))
        treinou = request.form.get('treino') == 's'
        nota_ali = float(request.form.get('nota', 0))
        agua = float(request.form.get('agua', 0))
        leu_livro = request.form.get('leitura') == 's'
        paginas = int(request.form.get('paginas', 0)) if leu_livro else 0

        # Criando os objetos das suas classes
        horas_sono = Sono(hr_sono)
        fez_exercicio = Treino(treinou)
        nota_alimentacao = Alimentacao(nota_ali)
        qnt_agua = Hidratacao(agua)
        leitura = Leitura(leu_livro, paginas)

        # Lógica exata do seu Score (Etapa 1)
        if horas_sono.get_horasSono() >= 7:
            score += 20
        else:
            score += (hr_sono / 7) * 20

        if fez_exercicio.get_fezExercicio(): score += 20

        if nota_alimentacao.get_notaAlimentacao() >= 8:
            score += 20
        else:
            score += (nota_alimentacao.get_notaAlimentacao() / 8) * 20

        if qnt_agua.get_qntAgua() >= 2: score += 20

        if leitura.get_leuLivro(): score += 5
        if leitura.get_qntPag() >= 10: score += 15

    return render_template('index.html', clima=clima, score=score, exibir=exibir_resultado)

if __name__ == '__main__':
    app.run(debug=True)