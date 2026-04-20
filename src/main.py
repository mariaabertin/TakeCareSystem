from classes import Sono, Treino, Alimentacao, Hidratacao, Leitura
from services import buscarClima

clima = buscarClima("Brasilia")
if clima:
    print(f"\n---------- Atenção Diária: ----------")
    print(f"Clima em Brasília: {clima['temp']}°C e {clima['condicao']}")
    if clima['temp'] > 28:
        print("Está calor! A meta de hidratação hoje é essencial!")

print("\n" + "-"*64)
print("Seja bem-vindo(a) ao TakeCare!")
print("Onde o objetivo é o autocuidado e a manutenção do seu bem estar!")
print("-"*64)


hrSono = float(input("Quantas horas você dormiu? "))
treinou = input("Fez exercício hoje? (s/n): ").lower() == 's'
notaAli = float(input("Qual a nota da sua alimentação hoje (0-10)? "))
agua = float(input("Quantos litros de água bebeu hoje? "))
leuLivro = input("Leu algum livro hoje? (s/n): ").lower() == 's'
if leuLivro:
    pagina = int(input("Quantas páginas? "))
else:
    pagina = 0


horasSono = Sono(hrSono)
fezExercicio = Treino(treinou)
notaAlimentacao = Alimentacao(notaAli)
qntAgua = Hidratacao(agua)
leitura = Leitura(leuLivro, pagina)


score = 0
if horasSono.get_horasSono() >= 7:
    score += 20
else:
    porcentamemSono = hrSono/7
    score += porcentamemSono*20

if fezExercicio.get_fezExercicio():
    score += 20

if notaAlimentacao.get_notaAlimentacao() >= 8:
    score += 20
else:
    porcentamemAli = notaAlimentacao.get_notaAlimentacao()/8
    score += porcentamemAli*20

if qntAgua.get_qntAgua() >= 2:
    score += 20


if leitura.get_leuLivro():
    score += 5
if leitura.get_qntPag() >= 10:
    score += 15


print("\n" + "-"*35)
print(f"Seu Score de Autocuidado hoje é: {score:.2f}%")

if score >= 80:
    print("Parabéns, você está sendo sua prioridade!")
elif 60 <= score <= 79:
    print("Tem dias turbulentos, mas você está no caminho! Se mantenha firme!")
else:
    print("Se priorizar é o 1º passo para uma vida equilibrada e prazeroza!")

print("\n" + "-"*35)
print("Amanhã é um novo dia, perfeito para novas oportunidades.")
print("Acredite em si mesmo!")
