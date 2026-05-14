import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding='latin1'
)

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:@localhost:3307/smart_retail_db"
)

# Import to MySQL
df.to_sql(
    name="sales_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data Imported Successfully")