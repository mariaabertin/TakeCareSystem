# TakeCareSystem

**Status do Projeto:** v2.0.0 
> 🌍 **Acesse o App Online:** [https://takecare-system.onrender.com](https://takecare-system.onrender.com)  
*(Nota: Por estar em um servidor gratuito, o primeiro acesso pode levar cerca de 1 minuto para carregar).*

---
Sistema: TakeCare

## Descrição do Problema Real
Muitas pessoas, imersas na rotina, negligenciam sua relação consigo mesmas e suas necessidades básicas de saúde. Essa falta de monitoramento pode levar ao esgotamento físico e mental (burnout), pois o indivíduo perde a percepção de quão pouco tem dormido ou se hidratado, de como está sua alimentação, se tem realizado exercícios e tirado um tempo para leitura.

## Proposta da Solução
A TakeCare surge como uma ferramenta objetiva para reter atenção pessoal e autoreflexão. Ao colocar parâmetros ativos para necessidades básicas diárias (sono, exercício, alimentação, hidratação e leitura), o sistema instiga o usuário a refletir sobre seu autocuidado. Além disso, o cálculo de um **score final** diário incentiva a busca por melhores hábitos para alcançar pontuações maiores no dia seguinte, transformando a disciplina em um processo visual e mensurável.

## Público-alvo
Público geral, estudantes e profissionais que buscam melhorar sua organização pessoal e saúde mental.

--

## Novidades da Versão 2.0.0 (Etapa Intermediária)
- **Interface Web:** Desenvolvida com Flask, HTML5 e CSS3 personalizado.
- **Estética Cozy:** Design focado em bem-estar com paleta de cores terrosas (Terracota, Sálvia e Creme).
- **Integração com API de Clima:** Consumo em tempo real da API HG Brasil Weather para contextualizar as recomendações de saúde com o clima de Brasília.
- **Dashboard Dinâmico:** Cálculo de Score de Autocuidado processado no Back-end e exibido em tempo real.
- **Deploy Automatizado:** Hospedagem via Render com integração contínua (CI/CD).

## Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **Web Framework:** Flask
- **Integração:** Requests (Consumo de API REST)
- **Servidor de Produção:** Gunicorn
- **Testes:** Pytest (Testes de unidade e integração)
- **Qualidade de Código:** Flake8 (Linting/PEP 8)
- **CI/CD:** GitHub Actions (Build e testes automáticos a cada Push/PR)

## Instruções de Instalação
1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone este repositório:
   git clone https://github.com/mariaabertin/TakeCareSystem.git
3. Acesse a pasta do projeto e instale as dependências necessárias:
   <br> pip install -r requirements.txt

## Instruções de Execução:
1. Para iniciar a aplicação via terminal, execute o seguinte comando na src do projeto:
   <br> python3 src/main.py

## Instruções para rodar os testes: 
Para validar a lógica de negócio e garantir que os cálculos estão corretos:
1. Certifique-se de estar na src do projeto.
2. Execute o comando:
   <br> python3 -m pytest

## Instruções para rodar o lint: 
Para verificar a conformidade do código com as boas práticas da PEP 8:
1. Execute o comando:
   <br> flake8 src/

## Informações adicionais:
Versão atual: 2.0.0 <br>
Autora: Maria Clara Bertin <br>
Link para repositório público: https://github.com/mariaabertin/TakeCareSystem

>Este projeto faz parte da disciplina de BootcampII da graduação em Engenharia de Software e segue os padrões de Clean Code e Gestão de Versão.
