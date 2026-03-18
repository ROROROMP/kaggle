from pathlib import Path
import os

class Config:
    # 環境判定
    IS_KAGGLE = bool(os.getenv("KAGGLE_URL_BASE"))

    # ルート
    ROOT = Path("/kaggle/working") if IS_KAGGLE else Path.cwd()

    # データ
    DATA = Path("/kaggle/input/titanic") if IS_KAGGLE else ROOT / "data/raw"

    # 出力
    OUTPUT = ROOT / "output"
    OUTPUT.mkdir(exist_ok=True)

    # DB（必要なら）
    # DB = ROOT / "data/db/titanic.duckdb"

    # その他
    # TARGET = "Survived"
