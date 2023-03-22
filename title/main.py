"""
スクレイピングをしてデータを取得

import sys, pprint
pprint.pprint(sys.path)
importの参照先に、pthファイルを作ることでpathを通す
"""

import requests
from bs4 import BeautifulSoup

def main():
    page_url = "https://ukaru-eigo.com/target-1900-word-list/"

    r = requests.get(page_url)

    #インスタンスの作成
    soup = BeautifulSoup(r.text, features="html.parser")
    #tdタグに単語
    #column-3 and column-4

    word_list = soup.find_all("td", class_="column-3")
    w_list = [x.text for x in word_list]
    meaning_list = soup.find_all("td", class_="column-4")
    m_list = [x.text for x in meaning_list]

    



#main.pyなら実行するという意味
if __name__ == "__main__":
    main()
