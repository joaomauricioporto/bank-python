# 🏦 Bank Python

Um sistema bancário simples e interativo rodando direto no terminal, totalmente desenvolvido em Python. Este projeto foi criado para gerenciar contas de usuários e simular operações bancárias do dia a dia de forma rápida e segura.

## 🚀 Funcionalidades

O sistema possui um menu interativo que permite realizar as seguintes ações:
- **Gerenciamento de Contas:** Criação e listagem de contas bancárias.
- **Operações Financeiras:** Realização de saques, depósitos e transferências entre contas.
- **Persistência de Dados:** Todas as contas e saldos são salvos e atualizados automaticamente em um arquivo `.json`, garantindo que nenhuma informação seja perdida ao fechar o programa.

## 📂 Estrutura do Projeto

O código foi dividido em módulos para facilitar a manutenção e leitura:

- `main.py`: Ponto de entrada principal do sistema.
- `menu.py`: Responsável por exibir a interface de texto e capturar as escolhas do usuário.
- `operacoes.py`: Contém a lógica das transações financeiras (saque, depósito, transferência).
- `contas.py`: Lida com a estrutura e regras das contas bancárias.
- `armazenamento.py`: Módulo dedicado a ler e escrever as informações no banco de dados local.
- `contas.json`: Arquivo que atua como banco de dados local do sistema.

## 💻 Como executar na sua máquina

1. Certifique-se de ter o [Python](https://www.python.org/) instalado.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/joaomauricioporto/bank-python.git](https://github.com/joaomauricioporto/bank-python.git)
