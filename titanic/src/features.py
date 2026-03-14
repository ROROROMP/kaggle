# -----------------------------
# 欠損値処理、カテゴリ変換、特徴量作成
# -----------------------------

import sys
from pathlib import Path

# モジュールとして import された場合は不要
# 直接実行される場合のみ親ディレクトリを sys.path に追加
if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.config import DATA, DB
import duckdb
import polars as pl

# 列が省略されないように
pl.Config.set_tbl_cols(-1)
pl.Config.set_tbl_rows(30)

# DuckDBに接続
conn = duckdb.connect(DB)


if __name__ == "__main__":

    full_data = conn.sql("SELECT * FROM full_data")

    print(full_data)

    # print(full_data)
    # print(summarize)

conn.close()


# def join_table():
#     # テーブルデータを結合

#     train = load_train()
#     test = load_test()

#     # DuckDBにDataFrameをテーブルとして登録
#     conn.register("train", train)
#     conn.register("test", test)

#     full_data = conn.query(f"""
#             WITH full_data AS (
#             SELECT
#                 PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
#             FROM train
#             UNION ALL
#             SELECT
#                 PassengerId,NULL as Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
#             FROM test
#             )
#             SELECT
#                 *,
#                 split_part(Name, ',', 1) AS last_name,
#                 trim(split_part(split_part(Name, ',', 2), '.', 1)) AS title,
#                 trim(split_part(split_part(Name, '.', 2), ' ', 2)) AS first_name,
#                 CASE
#                     WHEN Age IS NULL THEN NULL
#                     WHEN Age < 13 THEN 'child'
#                     WHEN Age < 20 THEN 'teen'
#                     WHEN Age < 40 THEN 'adult'
#                     WHEN Age < 60 THEN 'middle'
#                     ELSE 'senior'
#                 END AS age_group

#             FROM full_data
#             ;
#             """)

#     # DuckDBにDataFrameをテーブルとして登録
#     conn.register("full_data", full_data)
#     summarize = conn.query(f""" SUMMARIZE SELECT * FROM full_data ;""").pl()

#     A = conn.query(f"""
# SELECT age_group,title,count(PassengerId)
# FROM full_data
# GROUP BY age_group,title

#     """)

#     print(A)
#     return full_data, summarize
