# 第一話
# 「この高尚な服が濡れたらかなわんわ」
# 晴天の中、コンビニで傘を買い、通り雨を凌いだ。
# Webの「予報情報」又は「雨雲レーダー情報」を使った推論と思われる。
# 実現方法が２つあります
#　１。WebAPI経由でデータを取得し、推論。容易。
#　２。雨雲サイトをスクレイピングして、雨雲画像を使った予測。高度な複雑系の計算が必要になります。

import requests

# 気象庁 JSONデータ 山梨県 概要
response = requests.get("https://www.jma.go.jp/bosai/forecast/data/overview_forecast/190000.json")
print(response.json())
response = requests.get("https://www.jma.go.jp/bosai/forecast/data/forecast/190000.json")
print(response.json())
