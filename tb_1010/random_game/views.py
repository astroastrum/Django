from django.shortcuts import render
import random

# Create your views here.
def index(request):  
  return render(request, "index.html")


def today_dinner(request):
  dinner_list = [
    {"name": "salad", "src": "https://www.licious.in/blog/wp-content/uploads/2020/12/3-Step-Chicken-Salad.jpg"},
    {"name": "steak", "src": "https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4.jpg"},
    {"name": "pasta", "src": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-bucatinipasta-045-ls-1607552701.jpg"},
  ]
  
  dinner = random.choice(dinner_list)
  context = {
    "dinner" : dinner
  }
  
  return render(request, "today_dinner.html", context)


def lotto(request):
  # 1부터 46사이의 숫자를 6개 뽑는다
  # 로또 번호 6개를 5번 뽑기
  lotto_list = []

  '''
  lotto_result_list = [
    {"lotto":[1,2,3,4,5,6], "result":"1등 - 10억"},
    {"lotto":[1,2,3,4,5,6], "result":"1등 - 10억"},
    {"lotto":[1,2,3,4,5,6], "result":"1등 - 10억"},
    {"lotto":[1,2,3,4,5,6], "result":"1등 - 10억"},
    {"lotto":[1,2,3,4,5,6], "result":"1등 - 10억"},
  ]
  ''' 

  for _ in range(5):
    lotto = random.sample(range(1, 46),6)
    lotto_list.append(lotto)
  
  context = {
    "lotto_list": lotto_list,
  }
  return render(request, "lotto.html", context)


