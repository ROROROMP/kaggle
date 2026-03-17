# -----------------------------
# テーブル作成
# -----------------------------


import sys
from pathlib import Path

# モジュールとして import された場合は不要
# 直接実行される場合のみ親ディレクトリを sys.path に追加
if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.config import DATA, DB
import duckdb


# DuckDBに接続
conn = duckdb.connect(DB)


def create_train():
    # trainデータをテーブルに
    conn.execute(f"""
        CREATE OR REPLACE TABLE train AS
        SELECT *
        FROM read_csv_auto('{DATA}/train.csv')
    """)


def create_test():
    # testデータをテーブルに
    conn.execute(f"""
        CREATE OR REPLACE TABLE test AS
        SELECT *
        FROM read_csv_auto('{DATA}/test.csv')
    """)


def create_join_data():
    # 結合データをテーブルに
    train = conn.sql("SELECT * FROM train")
    test = conn.sql("SELECT * FROM test")

    conn.execute(f"""
        CREATE OR REPLACE TABLE join_data AS
        ( SELECT
            PassengerId,Survived,Pclass,Name,Sex,CAST(Age AS INTEGER) as Age,SibSp,Parch,Ticket,ROUND(Fare, 1) as Fare,Cabin,Embarked
        FROM train
        UNION ALL
        SELECT
            PassengerId,NULL as Survived,Pclass,Name,Sex,CAST(Age AS INTEGER) as Age,SibSp,Parch,Ticket,ROUND(Fare, 1) as Fare,Cabin,Embarked
        FROM test )
        """)


# モジュールとして import された場合は不要
# 直接実行される場合のみ親ディレクトリを sys.path に追加
if __name__ == "__main__":

    print(DATA)
    print(DB)

create_train()
create_test()
create_join_data()

conn.close()
