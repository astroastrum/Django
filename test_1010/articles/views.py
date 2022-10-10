from django.shortcuts import render
import random



# Create your views here.
'''
def index(request):
  context = {
    'name': 'october',
    'img': 'https://thumbs.dreamstime.com/b/welcome-sign-flower-blooming-decoration-pink-background-175919766.jpg',
  }
  return render(request, 'index.html', context)
'''



def index(request):
  names = ['october', 'november', 'december']
  name = random.choice(names)
  context = {
    'name': name,
    'img': 'https://thumbs.dreamstime.com/b/welcome-sign-flower-blooming-decoration-pink-background-175919766.jpg',
  }
  return render(request, 'index.html', context)



# 사용자들이 랜덤하게 입력할 값을 다룰 수 있는 변수 = name
# 사용자들의 입력값 = name
def welcome(request, name):
  # 사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 보여줌
  context = {
    'name': name,
    'drinks': [
      'coke', 'latte', 'macchiato'
    ],

    'images': [
      'https://thumbs.dreamstime.com/b/welcome-sign-flower-blooming-decoration-pink-background-175919766.jpg',
      'https://thumbs.dreamstime.com/b/welcome-sign-tulip-flower-blooming-decoration-pink-background-182818281.jpg',
      'https://thumbs.dreamstime.com/b/welcome-sign-flower-blooming-decoration-wooden-background-221043138.jpg',
    ],
  }
  return render(request, 'welcome.html', context)


def fake(request):
  return render(request, 'fake.html')


def fakenaver(request):
  return render(request, 'fakenaver.html')