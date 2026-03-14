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
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS train AS
        SELECT *
        FROM read_csv_auto('{DATA}/train.csv')
    """)


def create_test():
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS test AS
        SELECT *
        FROM read_csv_auto('{DATA}/test.csv')
    """)


def create_full_data():
    train = conn.sql("SELECT * FROM train")
    test = conn.sql("SELECT * FROM test")

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS full_data AS
        ( SELECT
            PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
        FROM train
        UNION ALL
        SELECT
            PassengerId,NULL as Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
        FROM test )
        """)


if __name__ == "__main__":

    # print(DATA)
    # print(DB)

    create_train()
    create_test()
    create_full_data()

conn.close()
