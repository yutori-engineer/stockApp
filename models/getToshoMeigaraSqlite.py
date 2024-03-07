import pandas as pd
import sqlite3
from io import BytesIO
import requests

# URLからデータを読み込む
url = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"
response = requests.get(url)
data = response.content

# ExcelデータをPandas DataFrameに変換
df = pd.read_excel(BytesIO(data), header=0)  # 1行目を列名として指定

# SQLite3データベースに接続し、データを保存
db_path = "data_j.db"
conn = sqlite3.connect(db_path)
df.to_sql("data_j", conn, index=False, if_exists="replace")
conn.close()

print(f"データが {db_path} として正常に保存されました。")
