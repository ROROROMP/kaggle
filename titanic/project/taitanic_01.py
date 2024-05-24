"""
Titanic - Machine Learning from Disaster

https://www.kaggle.com/competitions/titanic/

データサイエンス入門に従ってやってみる
https://www.youtube.com/watch?v=Wb2uLMOsZsg&t=995s


"""
# %%
# ファイルの読み込み確認
# --------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Jupyter Notebookでmatplotlibを使用する場合
# %matplotlib inline

parent = Path(__file__).resolve().parent
dir_path = parent.joinpath("../data")

# ファイルの読み込み確認
try:
    pd.read_csv(dir_path.joinpath("train.csv"))
    print("成功")
except FileNotFoundError:
    print("失敗")
# %%
# csv を読み込む
# --------------------------------
train_df = pd.read_csv(dir_path.joinpath("train.csv"))
test_df = pd.read_csv(dir_path.joinpath("test.csv"))

train_df.head(10)
test_df.head()

# %%
# データの大きさを確認
# --------------------------------
print("train data: ", train_df.shape)
print("test data: ", test_df.shape)

# %%
# データタイプを確かめる
# --------------------------------
train_df.dtypes
# str型はobjectと表示される
# %%
# 欠損値の確認
# --------------------------------
train_df.isnull().sum()
test_df.isnull().sum()

# %%
# infoメソッドでの欠損値確認
# --------------------------------
# こちらでは、欠けていないデータの数と、タイプ、メモリも出る
train_df.info()
test_df.info()

# %%
# データクレンジングのために、データを1つにする
# --------------------------------
df = pd.concat([train_df, test_df], ignore_index=True)
df.shape
df.tail()

# %%
# matplotlibを使った性別データの可視化
# １．性別のグループ分けとカウント
# ２．グラフ描画
count_sex = df.groupby("Sex")["PassengerId"].count()
plt.figure(figsize=(6, 4))
plt.bar(count_sex.index, count_sex.values)
plt.show()

# pandasでもグラフを描いてみる
count_sex.plot(kind="bar",figsize=(6,4))

# %%
# seabornでグラフを書いてみる
# seabornで作成すると、集計が不要でグラフ化できる
# --------------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df,x="Sex")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=df,x="Pclass")
plt.show()

# %%
# データの加工と前処理
# --------------------------------
"""
機械学習モデルの制度を上げるために
・欠損値の処理をする
・新しいカラムを作成（特徴量エンジニアリングという）
"""
df2 = df.drop(columns=[])