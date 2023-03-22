from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from .models import Target1900,idiom1000
import random
import requests
from bs4 import BeautifulSoup



st = 1
ed = 2
rw = 0
word_range = 0
params = {}

class titlefunc(TemplateView):
    template_name = "title.html"

    global st, ed, rw, word_range,params
    

    def post(self, request, *args, **kwargs):
        global st, ed, rw, word_range,params
        post = request.POST

        if request.method == 'POST': #requestからgetで辞書型でデータを取得する
            st = post.get('start')
            st = int(st)
            ed = post.get('end')
            ed = int(ed)
            rw = post.get('rw')
            #作成する単語をランダムチョイス(重複ナシ)
            l = [int(i) for i in range(st,ed+1,1)]
            #ここで単語数を変更
            ran = random.sample(l,36)
            
            #リストに含まれている数値を認識してフィルターにかける
            data = Target1900.objects.filter(idx__in = ran)
        
            params = {
                'format':rw,
                'data':data
                }

        return render(request,'title.html')
    

"""
            i = 0
            for w,m in zip(w_list,m_list):
                idiom1000.objects.create(idx = i, word = w , meaning = m)
                i += 1
"""


def test(request):

    global params

    q = params
    q['word'] = 'vtuber'

    """
    #単語追加コード(もっと楽なやり方知りたい)
    page_url = ""
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text, features="html.parser")
    
    word_list = soup.find_all("td", class_="column-2")
    w_list = [x.text for x in word_list]
    meaning_list = soup.find_all("td", class_="column-3")
    m_list = [x.text for x in meaning_list]

    i = 0
    for w,m in zip(w_list,m_list):
        idiom1000.objects.create(idx = i, word = w , meaning = m)
        i += 1
    """


    return render(request,'test.html',q)

#別の関数、クラスから変数にアクセスしたいときはglobalに注意

 
        

    

   


"""
    page_url = ""
    if page_url == "":
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

    i = 0
    for w,m in zip(w_list,m_list):
        Target1900.objects.create(idx = i, word = w , meaning = m)
        i += 1
    
"""
    
"""
引数
self→メソッドが動く？
request→httpresを受け取るという意味
*arg→arguement
**kwargs→keywardarguement

"""







######DBの操作############
#生成されたオブジェクトを変数に格納
