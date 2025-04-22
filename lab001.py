import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pyodbc
import uuid
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do .env
load_dotenv(dotenv_path="lab.env")

blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# Função para conectar ao banco usando pyodbc
def get_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USER};"
        f"PWD={SQL_PASSWORD};"
        f"Encrypt=yes;TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

# Função para fazer upload da imagem no Azure Blob Storage
def upload_blob(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
        container_client = blob_service_client.get_container_client(blobContainerName)
        blob_name = str(uuid.uuid4()) + "_" + file.name
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file, overwrite=True)
        image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
        return image_url
    except Exception as e:
        st.error(f"Erro ao fazer upload da imagem: {e}")
        return None

# Função para inserir produto no banco
def insert_product(name, price, description, image_file):
    try:
        image_url = upload_blob(image_file)
        if not image_url:
            return False

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (?, ?, ?, ?)",
            (name, price, description, image_url)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
        return False

# Função para listar produtos
def list_products():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []
    
# Tela para listar os produtos
def list_products_screen():
    products = list_products()
    if products:
        cards_por_linha = 3
        cols = st.columns(cards_por_linha)
        for i, product in enumerate(products):
            with cols[i % cards_por_linha]:
                st.markdown(f'### {product[1]}')  # Nome
                st.write(f'**Descrição:** {product[2]}')  # Descrição
                try:
                    preco_formatado = f'R${float(product[3]):.2f}'  # Preço
                except (ValueError, TypeError):
                    preco_formatado = 'Preço inválido'
                st.write(f'**Preço:** {preco_formatado}')
                if product[4]:  # Imagem
                    html_img = f'<img src="{product[4]}" width="200" height="200" alt="{product[1]}">'
                    st.markdown(html_img, unsafe_allow_html=True)
                st.markdown('---')
    else:
        st.write("Nenhum produto cadastrado.")

# Interface principal
st.header("Cadastro de Produto")

product_name = st.text_input("Nome do produto:")
product_price = st.number_input("Preço do produto:", min_value=0.0, format="%.2f")
product_description = st.text_input("Descrição do produto:")
product_image = st.file_uploader("Upload da imagem do produto", type=["jpg", "jpeg", "png"])

# Botão para salvar produto
if st.button("Salvar"):
    if product_name and product_description and product_price and product_image is not None:
        success = insert_product(product_name, product_price, product_description, product_image)
        if success:
            st.success("Produto salvo com sucesso.")
    else:
        st.warning("Por favor, preencha todos os campos e envie uma imagem.")

# Botão para listar produtos
st.header('Produtos Cadastrados')
if st.button('Listar Produtos'):
    list_products_screen()
    
    load_dotenv(dotenv_path="lab.env")