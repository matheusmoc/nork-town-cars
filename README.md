# 🚗 Visão Geral do App Nork-Town Cars

O **Nork-Town Cars** é um aplicativo desenvolvido para resolver um desafio único na pequena cidade fictícia de Nork Town, onde o governo local implementou restrições à propriedade de veículos para controlar o número de carros na região. O aplicativo serve como um sistema de gerenciamento para uma concessionária de automóveis, permitindo o rastreamento dos proprietários de carros e seus respectivos veículos, enquanto cumpre as regulamentações da cidade.

## 🌟 Principais Funcionalidades e Especificações:

1. **Limitações de Propriedade de Veículos:**
   - Cada pessoa pode possuir **até três veículos**. Isso garante a conformidade com a lei local, que visa controlar a quantidade de carros na cidade.

2. **Especificações dos Veículos:**
   - Os veículos podem ter uma das três cores: **amarelo, azul ou cinza**.
   - Cada veículo pode pertencer a um dos três modelos: **hatch, sedan ou conversível**.

3. **Gerenciamento de Proprietários de Carros:**
   - O aplicativo permite a adição de **proprietários de carros**. É importante notar que os proprietários de carros podem não ter veículos inicialmente e podem ser marcados como **oportunidades de venda**. Essa funcionalidade ajuda as concessionárias a rastrear potenciais clientes para futuras vendas de veículos.

4. **Registro de Veículos:**
   - Os carros não podem existir no sistema sem um proprietário associado. Isso garante que todos os veículos sejam contabilizados e ajuda a manter a integridade da estrutura de propriedade dentro do aplicativo.

5. **Interface do Usuário:**
   - O aplicativo deve apresentar uma interface amigável onde os funcionários da concessionária podem adicionar e gerenciar facilmente os proprietários de carros e seus veículos. Isso pode incluir formulários para inserir os dados do proprietário, selecionar cores e modelos de veículos e marcar potenciais vendas.

6. **Validação de Dados:**
   - O aplicativo deve implementar regras de validação para impedir que os proprietários ultrapassem o limite de três veículos e garantir que todas as entradas de veículos estejam vinculadas a um proprietário.

7. **Rastreamento de Oportunidades:**
   - Para proprietários sem carros, o sistema deve permitir que os funcionários da concessionária anotem esses proprietários como potenciais compradores, o que pode ajudar em futuros esforços de marketing e vendas.

## 🎯 Propósito do App:

O objetivo principal do aplicativo **Nork-Town Cars** é criar uma forma organizada e eficiente de gerenciar a propriedade de veículos em conformidade com as regulamentações locais. Ao implementar funcionalidades que rastreiam os proprietários de carros e seus veículos, o aplicativo ajudará a concessionária Carford a otimizar as oportunidades de venda, garantindo ao mesmo tempo a adesão aos limites de propriedade de veículos estabelecidos pelo governo da cidade. Essa abordagem não apenas ajuda a manter a ordem na comunidade, mas também fornece uma ferramenta valiosa para a concessionária gerenciar efetivamente seus relacionamentos com os clientes.


# 🚀 Como Iniciar o Projeto com Docker

Siga os passos abaixo para configurar e iniciar o projeto **Nork-Town Cars** utilizando Docker:

<br>

## Pré-requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas:

- [Docker](https://www.docker.com/get-started) (versão mais recente)
- [Docker Compose](https://docs.docker.com/compose/install/) (para gerenciar múltiplos contêineres)

<br>

## Passo a Passo

### 1. Clone o Repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/matheusmoc/nork-town-cars.git
cd nork-town-cars
```
### 2. Crie o Arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env` e adicione as variáveis de ambiente necessárias. 

Exemplo de conteúdo para o arquivo `.env`:

```plaintext
FLASK_ENV=development
DATABASE_URL=sqlite:///nork_town_cars.db
````

### 3. Construa e Inicie os Contêineres

Utilize o Docker Compose para construir e iniciar os contêineres do projeto.

1. **Construa os Contêineres:**

   Execute o seguinte comando para construir os contêineres:

   ```bash
   docker-compose build
   docker-compose up
   ````
   Ou em segundo plano
   
   ```bash
   docker-compose up -d
   ```
### 4. Rodando o projeto
   Para rodar um projeto Flask basta usar o comando:
   
   ```bash
   flask run
   ```

Este projeto utiliza as seguintes tecnologias:

- [Flask](https://flask.palletsprojects.com/) - Um microframework para Python que permite criar aplicações web rapidamente.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Uma extensão que adiciona suporte ao SQLAlchemy para aplicações Flask.
- [Flask-Login](https://flask-login.readthedocs.io/) - Uma extensão para gerenciar sessões de usuários em aplicações Flask.
- [Flask-Testing](https://flask-testing.readthedocs.io/) - Uma extensão que fornece ferramentas para facilitar os testes de aplicações Flask.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Uma biblioteca SQL e ORM para Python que permite interagir com bancos de dados de forma simples e eficiente.
- [Flasgger](https://flasgger.readthedocs.io/) - Uma extensão que simplifica a criação de APIs RESTful e a documentação com Swagger.
- [Vue.js 2.6](https://vuejs.org/v2/guide/) - Um framework progressivo para construir interfaces de usuário, que permite a criação de aplicações web reativas e dinâmicas.

# 🖼️ Overview de Imagens

## 🏠 Tela de login
![image](https://github.com/user-attachments/assets/bec8f740-b70f-4585-a7d1-dc428f9c0199)

*Descrição: Conta com um sistema de autenticação onde somente pessoas com autorização têm acesso às funcionalidades.*

## 📋 Tela de listagem

![image](https://github.com/user-attachments/assets/3598ee85-e760-4b10-afbd-e98647ebb22e)
![image](https://github.com/user-attachments/assets/b2611637-7288-4c43-bf6f-dbecff3354a4)

*Descrição: Tela de listagem do Nork-Town Cars, onde os usuários podem visualizar os proprietários e veículos.*

## ✍️ Cadastro de Proprietário

![image](https://github.com/user-attachments/assets/2da7a25e-6128-4d5e-8ea3-6324eb66ab29)

*Descrição: Formulário para cadastrar um novo proprietário de carro.*

## 🚙 Registro de Veículo

![image](https://github.com/user-attachments/assets/c66429e5-7375-40d1-a007-01c79a7b5d29)

*Descrição: Interface para registrar um novo veículo associado a um proprietário.*


## 📜 Documentação da API

A documentação da API está disponível através do Flasgger e pode ser acessada localmente após a execução do servidor Flask.

### 🌐 Acessando a Documentação

Após iniciar o servidor, a documentação da API pode ser acessada na seguinte URL: http://127.0.0.1:5000/apidocs/

![image](https://github.com/user-attachments/assets/873a2926-00ac-42c5-8968-8236c841b219)

Para visualizar as rotas completas do projeto, basta rodar:

```bash
flask route
```

![image](https://github.com/user-attachments/assets/e31d2834-ac9f-4b63-88e0-d551dbecb34e)


### ⚠️ Notas

- Certifique-se de que o servidor Flask está em execução antes de acessar a URL.
- A documentação incluirá todos os endpoints disponíveis na API, juntamente com suas respectivas descrições, parâmetros e exemplos de resposta.

## Testes Unitários

Este projeto inclui testes unitários para garantir que a aplicação funcione corretamente. Os testes estão localizados no arquivo https://github.com/matheusmoc/nork-town-cars/tree/master/app/tests. Você pode executar os testes utilizando o seguinte comando:

```bash
python -m unittest app/tests/test_cars.py
python -m unittest app/tests/test_owners.py 
````


