**CADASTRO DE PRODUTOS COM AZURE + SQL SERVER + PYTHON + STREAMLIT**

Este projeto foi desenvolvido como parte do curso Azure Cloud Native,
com o objetivo de aplicar conceitos práticos de desenvolvimento em nuvem utilizando Python, Streamlit, Azure Blob Storage e Microsoft SQL Server.

**Funcionalidades**
- Cadastro de produtos com: Nome, Preço, Descrição e Imagem
- Upload da imagem diretamente no Azure Blob Storage
- Armazenamento dos dados no Microsoft SQL Server
- Interface interativa criada com Streamlit
- Listagem de produtos com imagem, nome, descrição e preço formatado

**Tecnologias e Ferramentas**
- Python
- Streamlit
- Azure Blob Storage
- Microsoft SQL Server
- PyODBC
- dotenv
- uuid

**Como rodar o projeto**

Clone o repositório:
git clone https://github.com/MarceloIacovinaJr/cadastro-produtos-azure.git
cd cadastro-produtos-azure

Instale as dependências:

pip install -r requeriments.txt

Crie um arquivo lab.env com as seguintes variáveis de ambiente:

BLOB_CONNECTION_STRING= sua_connection_string_azure
BLOB_CONTAINER_NAME= nome-do-container
BLOB_ACCOUNT_NAME= nome-da-conta

SQL_SERVER= seu-servidor.database.windows.net
SQL_DATABASE= nome-do-banco
SQL_USER= usuario
SQL_PASSWORD= senha
 
Atenção: Não suba este arquivo para o GitHub! Ele contém informações sensíveis como senhas e chaves de acesso.

Execute o projeto:

streamlit run lab001.py


**Capturas de tela**

✅ Tela de desenvolvimento (VSCode)

![77270f0c-23fe-4632-81f1-ffe74b7ebbb2](https://github.com/user-attachments/assets/7b148329-16ee-45a3-9878-025030d632aa)

✅ Tela do banco de dados (Azure)

![c9f84a62-9442-41c6-b882-7ae7b02f1506](https://github.com/user-attachments/assets/e858ea7b-1193-46d4-b0ca-3deb5591f37b)


✅ Tela de Cadastro de produto

![e36cb2ec-e835-4576-aac6-ed637ea173ca](https://github.com/user-attachments/assets/73f8f379-b4fa-46bd-8b34-5d14cd8dbe14)


✅ Cadastrando produtos

![6807f202-7f99-4c25-862d-c8bd06e30537](https://github.com/user-attachments/assets/c39196cb-6d84-418d-a09f-b4b7f0bbea8e)


📦 Listagem de produtos

![0440428d-695f-457f-9e2c-57d59ce3a0d4](https://github.com/user-attachments/assets/3e5aaf04-8550-44ad-8fd3-8950514762a9)


**Aprendizados**
- Conectar uma aplicação Python ao Azure Blob Storage e ao SQL Server com pyodbc

**Resolver problemas reais como:**
- Timeout de conexão
- Driver ODBC não encontrado
- Push bloqueado no GitHub por conter dados sensíveis no commit
- Entender a estrutura básica de um app cloud native com front-end em Streamlit e back-end na nuvem

**Melhorias futuras**
- Adicionar autenticação de usuários
- Editar e remover produtos
- Filtro de busca por nome ou preço
- Publicação em nuvem (Azure App Service ou Streamlit Cloud)

