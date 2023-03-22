#models.pyでsqlite3を動かす
from django.db import models


class Target1900(models.Model):
    #CharFieldは文字列型のデータを表す
    idx = models.IntegerField()
    word = models.CharField(max_length = 100)
    meaning = models.CharField(max_length = 100)

class idiom1000(models.Model):
    idx = models.IntegerField()
    word = models.CharField(max_length = 100)
    meaning = models.CharField(max_length = 100)


"""
設定の指示書を作るときは
py manage.py makemigrations

maigrationsの指示書を実行するときは
py manage.py migrate
"""

#テーブルを削除するときは、modelsの記述を消して、makemigrations→migrate

"""
py manage,py createsuperuser
でユーザを作成し、dbを管理する

admin.pyをいじって、dbを管理画面に表示させる
"""



