from django.shortcuts import render
from pjt.settings import BASE_DIR
from .models import Article

# index.html에 {% for content in userwriting %} 이렇게 사용함
# userwriting = []

# 사용자가 작성한글 userwriting = ['Hello', 'Autumn', 'October']

# Create your views here.
def index(request):
  # print(BASE_DIR)
  # 사용자가 작성한글을 index.html에서 보여줌 (영구 저장소)
  # create함수에서 append한 content가 userwriting = []에서 차곡차곡 쌓이고 index.html에서 userwriting(위에 만들어 놓은 리스트를 사용함)이 보여진다
  # userwriting = [] 대신에 DB에서 가져오기
  userwriting = Article.objects.all()
  # SELECT * FROM articles;
 
  return render(request, 'articles/index.html', {'userwriting': userwriting})

def create(request):
  # content라는 이름으로 request안에 담겨있는 get안의 content라고 하는 것을 사용할것이다
  # return render(request, {'content': request.GET.get('content')})는 create 페이지에 {{ content }}로 사용된다
  # 오른쪽부터 천천히 읽는다
  # request GET에서 content 파라미터로 날라온 데이터를 잡아서 컨텐트(변수명)에 넣으려고 한다
  # 사용자가 작성한 내용이 create 페이지에 보여짐
  # 아직 index.html에서 보여지는 것은 아님
  content = request.GET.get('content')
  # userwriting에 append 통해서 content를 넣을것이다
  # userwriting.append(content)
  # append대신에 DB에 저장
  # Article아 record 하나 만들게
  Article.objects.create(content = content)

  return render(request, 'articles/create.html', {'content': content})
  # request GET에서 content 파라미터로 날라온 데이터를 잡아서 컨텐트(변수명)에 넣으려고 한다
  # 이것을 template에 content라는 이름으로 사용할 것이다 {'content': content}


# 작성한 글을 영구적인 저장소에 넣는 방법
# 사용자가 작성했던 글이 있으면 무조건 저장을 해야함
# 저장을 한다는 것은 영구적인 저장소에 넣는다는 것 
