from django.urls import path
from .views import titlefunc,test



#.as_viewをやらないとなぜか起動しない(classのときはas_view()をつける)
urlpatterns = [
    path('', titlefunc.as_view()),
    path('test/',test,name = "test"),
]