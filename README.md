Projeto Clientes
Este é um sistema de gerenciamento de clientes, desenvolvido para organizar e facilitar a administração de informações de clientes. O aplicativo permite o cadastro, visualização, edição e exclusão de dados de clientes de forma eficiente.

URL do App
O aplicativo está rodando na seguinte URL: http://3.137.166.211:8000/

Deploy
O deploy foi realizado utilizando a AWS (Amazon Web Services).

Tecnologias Utilizadas
Python: Linguagem de programação principal utilizada no desenvolvimento.
Django: Framework web utilizado para construir o backend do aplicativo.
SQLite: Banco de dados utilizado para armazenar as informações dos clientes.
HTML/CSS: Tecnologias de front-end utilizadas para construir a interface do usuário.
JavaScript: Utilizado para adicionar interatividade à interface do usuário.
AWS: Utilizado para o deploy do aplicativo, garantindo escalabilidade e disponibilidade.
Como Rodar o Projeto Localmente
Pré-requisitos
Python 3.8+
pip (Python package installer)
Instalação
Clone o repositório:

bash
Copy code
git clone https://github.com/dnsouzadev/projeto-clientes.git
Navegue até o diretório do projeto:

bash
Copy code
cd projeto-clientes
Crie um ambiente virtual:

bash
Copy code
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copy code
venv\Scripts\activate
No Linux/MacOS:

bash
Copy code
source venv/bin/activate
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Executando o Projeto
Aplique as migrações:
bash
Copy code
python manage.py migrate
Inicie o servidor:
bash
Copy code
python manage.py runserver
O aplicativo estará disponível em http://127.0.0.1:8000/

Populando o Banco de Dados
Para popular o banco de dados com dados de exemplo, execute o script populate_script.py:

bash
Copy code
python populate_script.py
Estrutura do Projeto
manage.py: Script para gerenciar o projeto.
requirements.txt: Arquivo com as dependências do projeto.
populate_script.py: Script para popular o banco de dados com dados de exemplo.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
