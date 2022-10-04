from django.shortcuts import render
#외장이여서 random 불러와야한다.
import random


# Create your views here.
# 장고와 약속: request
def index(request):
  # 첫번째 인자는 무조건 request이다.
  # request 인자에 요청한 사람의 정보가 들어온다.
  # 요청에 대한 정보는 하나의 객체가 되어서 들어온다.
  # 여기에서 Welcome 페이지를 보여준다.
  names = ['Anna', 'Taylor', 'Virginia', 'Hamish', 'Nicole', 'Alexandra']
  name = random.choice(names)
  
  context = {
    # 변수명(key): 값(value)
    'name': name,
    # name(값)에 작은따옴표 주의
    'img': 'https://thumbs.dreamstime.com/b/welcome-sign-flower-blooming-decoration-pink-background-175919766.jpg',
  }
  return render(request, 'index.html', context)  
  # context(reder함수의 세번째 인자)는 딕셔너리를 데이터로 넣는다. 
  # 그리고 index.html에 3번째 주입된 딕셔너리 데이터를 템플릿에 전달해준다.
  # 그 데이터를 템플릿에서 활용한다.


def welcome(request, name):
  # 두번째 인자는 name이라고 하는 사용자들의 입력값을 사용한다.  
  # 사람들이 /welcome/본인이름 을 입력하면 환영 인사와 이름을 보여준다.
  
  images = [
    'https://thumbs.dreamstime.com/b/welcome-sign-hanging-wooden-flower-bouquet-decoration-216831854.jpg',
      'https://thumbs.dreamstime.com/b/welcome-sign-flower-blooming-decoration-wooden-background-221043138.jpg',
      'https://thumbs.dreamstime.com/b/welcome-sign-tulip-flower-blooming-decoration-pink-background-182818281.jpg'
  ]

  img = random.choice(images)
  
  context = {
    'name': name,
    # 사람들이 입력한 이름을 변수명에 넣고 두번째 인자로 받은 name 데이터를 넣는다.
    'greetings': [
      'Good Day', 'Nice Day', 'Good Morning', 'Good Afternoon'

    ],

    'img': img,
  }
  return render(request, 'welcome.html', context)