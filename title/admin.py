from django.contrib import admin
from .models import Target1900,idiom1000

#dbが管理画面から見えるようにするコード
admin.site.register(Target1900)
admin.site.register(idiom1000)

