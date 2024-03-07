import pandas as pd
import sqlite3
import requests

# URLからデータを読み込む
url = "https://www.taisyaku.jp/sys-list/data/other.csv"
df = pd.read_csv(url, header=1, encoding='shift_jis')  # 列名なしで読み込み

# SQLite3データベースに接続し、データを保存
db_path = "other_data.db"
conn = sqlite3.connect(db_path)
df.to_sql("other_data", conn, index=False, if_exists="replace")
conn.close()

print(f"データが {db_path} として正常に保存されました。")
