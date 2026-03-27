# Sistema Bancário com Python

Este repositório contém o desenvolvimento de um sistema bancário completo criado em Python. O projeto permite gerenciar contas bancárias, realizar operações financeiras e manter um histórico detalhado de todas as transações realizadas.

O sistema possui uma interface via terminal interativa e intuitiva, permitindo que usuários realizem operações bancárias de forma simples e organizada.

## Sobre o Projeto

O projeto foi desenvolvido com o objetivo de simular um sistema bancário real com funcionalidades essenciais para gerenciamento de contas e operações financeiras. A aplicação permite criar contas bancárias contendo informações como nome completo, CPF e número da conta, além de possibilitar operações como depósitos, saques e consultas de saldo e extrato.

A partir dessas funcionalidades, o sistema mantém um controle automático de todas as movimentações financeiras, gerando extratos detalhados que ajudam os usuários a acompanhar suas transações bancárias.

Além disso, o projeto também foi desenvolvido com foco na prática de organização de código em múltiplos módulos, separando responsabilidades entre interface de usuário, lógica de operações financeiras, gerenciamento de contas e persistência de dados.

## Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas no desenvolvimento deste projeto:

- **Python:** Linguagem de programação principal utilizada no desenvolvimento da aplicação.
- **JSON:** Formato utilizado para persistência de dados das contas bancárias.
- **Estrutura Modular em Python:** Organização do projeto em diferentes arquivos para separar responsabilidades e melhorar a manutenção do código.

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- **`main.py`**: Ponto de entrada principal do sistema, responsável pelo loop principal e coordenação das funcionalidades.
- **`menu.py`**: Responsável por exibir a interface de texto e capturar as escolhas do usuário.
- **`contas.py`**: Contém as funções para criação, listagem e exclusão de contas bancárias.
- **`operacoes.py`**: Implementa a lógica das transações financeiras (depósitos, saques, consultas de saldo e extrato).
- **`armazenamento.py`**: Responsável pela persistência de dados, leitura e escrita no arquivo JSON.
- **`contas.json`**: Arquivo de armazenamento que atua como banco de dados local do sistema.

Essa organização permite uma separação clara entre as diferentes responsabilidades do sistema, facilitando futuras melhorias e manutenção do código.

## Como Executar o Projeto

Para executar o projeto em seu ambiente local, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/joaomauricioporto/bank-python.git
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd bank-python
   ```

3. **Execute o sistema:**
   ```bash
   python main.py
   ```

**Observação:** O projeto utiliza apenas bibliotecas padrão do Python, portanto não é necessário instalar dependências adicionais.

## Funcionalidades do Sistema

O sistema permite realizar diversas operações bancárias, incluindo:

- **Criar Conta:** Cadastro de novas contas bancárias com nome, CPF e número de conta gerado automaticamente
- **Ver Contas:** Listagem de todas as contas cadastradas no sistema
- **Depositar:** Realização de depósitos em contas existentes com atualização automática do saldo
- **Sacar:** Realização de saques com verificação de saldo disponível
- **Ver Saldo:** Consulta do saldo atual de uma conta específica
- **Ver Extrato:** Visualização detalhada do histórico de movimentações de uma conta
- **Deletar Conta:** Exclusão de contas bancárias com confirmação de segurança
- **Persistência Automática:** Todas as operações são salvas automaticamente no arquivo JSON

## Possíveis Aplicações

Embora seja um projeto educacional e simplificado, sistemas desse tipo podem servir como base para:

- Aprendizado de conceitos de programação orientada a dados
- Compreensão de operações bancárias básicas
- Prática de organização modular de código Python
- Base para desenvolvimento de sistemas financeiros mais complexos
- Ensino de manipulação de arquivos e persistência de dados

## Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente incluem:

- Implementação de transferências entre contas
- Sistema de autenticação com senha para acesso às contas
- Limite de saques diários e taxas de operação
- Integração com banco de dados SQL para maior robustez
- Interface gráfica com Tkinter ou CustomTkinter
- Geração de relatórios financeiros em PDF
- Sistema de diferentes tipos de conta (corrente, poupança, investimento)
- Implementação de validação de CPF
- Histórico de transações com data e hora

## Contribuição

Contribuições para o projeto são bem-vindas. Caso tenha sugestões de melhorias, novas funcionalidades ou correções, fique à vontade para abrir uma *issue* ou enviar um *pull request*.

## Autor

- **João Maurício Porto** - <a href="https://github.com/joaomauricioporto">GitHub</a>
