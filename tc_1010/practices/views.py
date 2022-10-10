from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def ping(request):
  return render(request, 'ping.html')

def pong(request):
  # request가 어떤게 가능한건지 보기 위한것(메소드, 내용을 볼때)
  '''
  print(request)
  print(dir(request))
  print(request.GET,get('ball'))
  '''
  # name안에 들어있는 데이터 = request.GET.get('ball')
  ball = request.GET.get('ball')
  # template 안에서 name이라는 이름으로 사용한다
  context = {
    'name': ball,
  }
  return render(request, 'pong.html', context)
