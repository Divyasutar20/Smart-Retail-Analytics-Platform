import pandas as pd
from sqlalchemy import create_engine

# =========================
# MYSQL CONNECTION
# =========================

engine = create_engine(
    "mysql+pymysql://root:@localhost:3307/smart_retail_db"
)

# =========================
# LOAD DATA FUNCTION
# =========================

def load_data():

    query = "SELECT * FROM sales_data"

    df = pd.read_sql(
        query,
        engine
    )

    return df