# 1. 현재 폴더에서 django 프로젝트(my_pjt)와 앱(my_app)를 만들고 서버를 실행하기 위한 bash 명령어를 주석으로 작성하시오. 

# django-admin startproject 프로젝트이름
# python manage.py startapp 앱이름
# python manage.py runserver

# 2. http://127.0.0.1:8000/hello로 받은 요청을 통해 my_app 앱의 views.py에 있는 hello 함수를 실행시킬 수 있도록 아래 urls.py를 작성하시오 
from django.urls import path
from articles import views
urlpatterns = [
    path('hello/', views.hello),
]