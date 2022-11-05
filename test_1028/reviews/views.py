from django.shortcuts import render



# 데이터 처리 기능
# Create = 글 작성/ 제품 등록   > 데이터베이스 조작어 INSERT
# Read = 글 읽기/ 제품 확인   > SELECT
# Update = 글 수정/ 제품 세일 기간 수정   > UPDATE
# Delete = 글 삭제/ 제품 판매 마감    > DELETE

# Create your views here.
def index(request):
  return render(request, 'reviews/index.html')

def reviews(request):
  return render(request, 'reviews/reviews.html')

def create(request):
  return render(request, 'reviews/create.html')

def detail(request, pk):
  review = Review.objects.get(pk=pk)
  context = {
    'review': review,
  }
  return render(request, 'reviews/detail.html', context)
