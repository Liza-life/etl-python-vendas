import pandas as pd
from etl.logger import get_logger

logger = get_logger()

def extract_data():
    logger.info("Início da extração de dados")

    clientes = pd.read_csv("data/raw/clientes.csv")
    produtos = pd.read_csv("data/raw/produtos.csv")
    vendas = pd.read_csv("data/raw/vendas.csv")

    logger.info(f"Clientes extraídos: {clientes.shape}")
    logger.info(f"Produtos extraídos: {produtos.shape}")
    logger.info(f"Vendas extraídas: {vendas.shape}")

    return clientes, produtos, vendas
