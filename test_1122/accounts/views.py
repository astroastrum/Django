from django.shortcuts import render

# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

# 로그인 기능 
# django-allauth 사용하기
# pip install django-allauth
# 설치 후, settings.py에 반드시 등록
# (console.developers.google.com)에 접속 > 새 프로젝트 생성 페이지로 이동


def login(request):
  return render(request, 'accounts/login.html')



@login_required
def detail(request, user_pk):
    customer = get_user_model().objects.get(pk=user_pk)
    review_pg = request.GET.get("reviewpage")
    
    customer_rv = customer.review_set.all()
    # Paginator(분할될 객체, 페이지마다 넣을 객체수)
    review_data = Paginator(customer_rv, 5)
    review_page = review_data.get_page(review_pg)


    #reviews = customer.review_set.order_by('-pk')
    #review_page = request.GET.get('review_page', '1')
    #review_paginator = Paginator(reviews, 5)
    #review_page_obj = review_paginator.get_page(review_page)

    context = {
        "customer": customer,
        "review_page": review_page,
        # "reviews": review_page_obj,

    }
    return render(request, "accounts/detail.html", context)