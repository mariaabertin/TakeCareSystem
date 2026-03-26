# TakeCareSystem

**Status do Projeto:** v1.0.0 (Finalizado)

Sistema: TakeCare

## Descrição do Problema Real
Muitas pessoas, imersas na rotina, negligenciam sua relação consigo mesmas e suas necessidades básicas de saúde. Essa falta de monitoramento pode levar ao esgotamento físico e mental (burnout), pois o indivíduo perde a percepção de quão pouco tem dormido ou se hidratado, de como está sua alimentação, se tem realizado exercícios e tirado um tempo para leitura.

## Proposta da Solução
A TakeCare surge como uma ferramenta objetiva para reter atenção pessoal e autoreflexão. Ao colocar parâmetros ativos para necessidades básicas diárias (sono, exercício, alimentação, hidratação e leitura), o sistema instiga o usuário a refletir sobre seu autocuidado. Além disso, o cálculo de um **score final** diário incentiva a busca por melhores hábitos para alcançar pontuações maiores no dia seguinte, transformando a disciplina em um processo visual e mensurável.

## Público-alvo
Público geral, estudantes e profissionais que buscam melhorar sua organização pessoal e saúde mental.

## Funcionalidades Principais
- Registro de horas de sono;
- Check-in de realização de exercícios físicos;
- Avaliação qualitativa da alimentação (nota 0-10);
- Monitoramento de volume de hidratação (litros);
- Registro de hábito de leitura (confirmação e quantidade de páginas);
- Cálculo automático de **Score de Autocuidado** com lógica de proporcionalidade.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **IDE:** PyCharm / VS Code
- **Testes:** Pytest
- **Qualidade de Código:** Flake8 (Linting)
- **CI/CD:** GitHub Actions

## Instruções de Instalação
1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone este repositório:
   git clone [COLE_AQUI_O_LINK_DO_SEU_REPOSITORIO]
3. Acesse a pasta do projeto e instale as dependências necessárias:
   pip install -r requirements.txt

## Instruções de Execução:
1. Para iniciar a aplicação via terminal, execute o seguinte comando na src do projeto:
   python3 src/main.py

## Instruções para rodar os testes: 
Para validar a lógica de negócio e garantir que os cálculos estão corretos:
1. Certifique-se de estar na src do projeto.
2. Execute o comando:
   python3 -m pytest

## Instruções para rodar o lint: 
Para verificar a conformidade do código com as boas práticas da PEP 8:
1. Execute o comando:
   flake8 src/

## Informações adicionais:
Versão atual: 1.0.0
Autora: Maria Clara Bertin
Link para repositório público: 
