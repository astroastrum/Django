from django.shortcuts import render
import random

# Create your views here.
def index(request):
  return render(request, "index.html")


def dinner(request):
  dinner_list = [
    {"name": "taco", "src":"https://cdn.traveltripper.io/site-assets/426_558_7669/media/2017-09-28-224820/best-tacos-new-york-city.jpg"},
    {"name": "steak", "src":"https://natashaskitchen.com/wp-content/uploads/2020/03/Pan-Seared-Steak-4.jpg"},
    {"name": "salad", "src":"https://www.licious.in/blog/wp-content/uploads/2020/12/3-Step-Chicken-Salad.jpg"},
  ]
  # 딕셔너리 데이터를 context에 담아서 templates에 넘겨줌
  fordinner = random.choice(dinner_list)
  
  context = {
    "fordinner" : fordinner

  }
  return render(request, "dinner.html", context)


