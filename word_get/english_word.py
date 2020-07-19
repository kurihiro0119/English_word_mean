import requests
from bs4 import BeautifulSoup


def get_mean_word(spell):
    # アクセス先URL
    url = "https://ejje.weblio.jp/content/" + spell

    # データ取得＆エンコード設定
    source = requests.get(url)
    source.encoding = source.apparent_encoding

    # ビューティフルスープで抽出
    data = BeautifulSoup(source.text, "html.parser")
    explanation_list = data.select("td.content-explanation")

    return explanation_list[0].text
