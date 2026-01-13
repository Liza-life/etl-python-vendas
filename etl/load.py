from sqlalchemy import create_engine
from etl.logger import get_logger

logger = get_logger()

def load_data(df):
    logger.info("Início da carga no banco de dados")

    engine = create_engine("sqlite:///database/vendas.db")
    df.to_sql("fato_vendas", engine, if_exists="replace", index=False)

    logger.info(f"Total de registros carregados: {df.shape[0]}")
    logger.info("Carga finalizada com sucesso")
