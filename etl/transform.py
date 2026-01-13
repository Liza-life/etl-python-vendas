import pandas as pd
from etl.logger import get_logger

logger = get_logger()

def transform_data(clientes, produtos, vendas):
    logger.info("Início da transformação dos dados")

    registros_antes = vendas.shape[0]

    vendas["data_venda"] = pd.to_datetime(vendas["data_venda"], errors="coerce")

    # Data quality
    datas_invalidas = vendas["data_venda"].isna().sum()
    if datas_invalidas > 0:
        logger.warning(f"Datas inválidas encontradas: {datas_invalidas}")

    df = vendas.merge(clientes, on="cliente_id", how="left") \
               .merge(produtos, on="produto_id", how="left")

    df["valor_total"] = df["quantidade"] * df["preco"]

    # Regra de qualidade
    valores_negativos = (df["quantidade"] <= 0).sum()
    if valores_negativos > 0:
        logger.warning(f"Registros com quantidade inválida: {valores_negativos}")

    registros_depois = df.shape[0]

    logger.info(f"Registros antes: {registros_antes}")
    logger.info(f"Registros depois: {registros_depois}")

    return df
