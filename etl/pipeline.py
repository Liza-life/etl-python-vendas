from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    clientes, produtos, vendas = extract_data()
    df_final = transform_data(clientes, produtos, vendas)
    load_data(df_final)

if __name__ == "__main__":
    run_pipeline()
