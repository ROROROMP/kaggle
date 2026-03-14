from pathlib import Path
import os


# Kaggle Notebook上かどうかを判定
if os.getenv("KAGGLE_URL_BASE"):
    # Kaggle Notebook用のパス
    ROOT = Path("/kaggle/working")
    DATA = Path("/kaggle/input/titanic")
else:
    # ローカル用のパス（VSCodeで実行する場合）
    ROOT = Path(__file__).resolve().parents[1]
    DATA = ROOT / "data/raw"
    DB = ROOT / "data/db/titanic.duckdb"

# 出力フォルダ
OUTPUT = ROOT / "data/processed"


# print(f"ルートフォルダ：{ROOT}")
# print(f"データフォルダ：{DATA}")
# print(f"出力フォルダ：{OUTPUT}")
