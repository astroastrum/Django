from django.shortcuts import render, redirect
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.
def index(request):
  return render(request, 'reviews/index.html')


def create(request):
  if request.method == "POST":
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
      review_form.save()
      return redirect("reviews:detail")
  else:
    review_form = ReviewForm()
  context = {
    "review_form": review_form
  }
  return render(request, 'reviews/form.html', context)



def detail(request, pk):
  review = Review.objects.get(pk=pk)
  context = {
    "review": review,
  }
  return render(request, "reviews/detail.html", context)


def update(request, pk):
  review = Review.objects.get(pk=pk)
  if request.method == "POST":
    review_form = ReviewForm(request.POST, instance=review)
    if review_form.is_valid():
      review_form.save()
      return redirect("reviews:index")
  else:
    review_form = ReviewForm(instance=review)
  context = {
    "review_form": review_form,
  }
  return render(request, "review/form.html", context)



def delete(request, pk):
  review = Review.objects.get(pk=pk)
  review.delete()
  return redirect('reviews:index')


