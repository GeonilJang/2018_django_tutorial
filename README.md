# 2018_django_tutorial
pip install -r requirements.txt


makemigrations blog
migrate blog
showmigrations blgo -> 마이그레이션 적용 형황
sqlmigrate blog -> 적용 sql 확인가능


blog/001
blog/002
blog/003
blog/004
blog/005  <-

python3 manage.py migrate blog 004 이렇게 하면 이쪽으로 넘어 갑니다.








데이터 정보를 주고 받는 것을 잘 확인하기위해서 아래의 모듈을 설치하는 것을 추천한다,
pip install django-debug-toolbar
-> settings.py 에 앱추가
INSTALLED_APPS = debug_toolbar
MIDDLEWEARE = debug_toolbar.middleware.DebugToolbarMiddleware
INTERNAL_IPS = localhost

_ModelManager_
model.objects.all()
model.objects.all().order_by('-id')[:10]

#C
1)
model.objects.create(필드명=값, 필드명=값)
Post.objects.create(author="장건일",title="테스트",content="안뇽")

2)
model_instance = Post(author="goenil")
model_instance.save() 로 저장도 가능



#R
queryset = Post.objects.all()
queryset = queryset.filter(조건필드 = 조건값 , 조건필드 = 조건값)
queryset = queryset.filter(조건필드 = 조건값)

queryset.get(id=1)
queryset.get(title='my title')



&and
Post.objects.filter(title__icontains='1') 타이틀에서 값이 대소 문자 구별하지 않고 1이 포합되어 있는것
Post.objects.filter(title__icontains='1').exclude(title__endswith='3') 1포함 3제외


메니투메니
Post.objects.filter(tag_set__name="파이썬")
Post.objects.filter(tag_set__name__in=["파이썬","장고"])


$or
from django.db.models import Q
Post.objects.filter( Q(title__icontains='1') | Q(title__endswith='3')

#U

해당 쿼리셋을 획득 하는 여러가지 방법을 통하여 획득하고 그를 통한 저장을 시도한다.
post = Post.objects.get(id=1)
post.content ="안뇽"
post.save()

여러개 한방에 업데이트)
queryset = Post.objects.all()
queryset.update(content="장건일은 멋쟁")

#D
post = Post.objects.get(id=id)
post.delete()

or

queryset.delete (여러개 지울떄)


ForignKey 1 : n
ManyToMnay m : n

다시좀 봅시다ㅛ;ㅔㅈ


ForignKey 와 OneToOneField 의 차이점

생성되는 필드명은 같으나 유일성의 차 1:n 1:1

ForignKey를 이용할 때 데이터를 가져오는방법
#1 comment = Comment.objects.get(id=1) 뭐 어떻게든 커멘트의 객체를 가져와서
   comment.post 로 데이터를 접근 하는 방법이 있고

#2 Post.objects.get(id=comment.post_id)  포스트 모델에서 comment 모델로 접근하는 방법도 있고



#related_name
ForignKey 를 사용할 떄 데이터를얻어 오는 방법
post = Post.objects.first()
Comment.objects.filter(post=post)  #방법1
post.comment_set.all() #방법2 -> related_name 상용함.



comment = Comment.object.first()
comment.post






200 성공
302 리다이렉트 return HttpResponseRedirect('/blog/') / resolve_url('blog:post_list') / redirect('blog:post_list')
404 못찾음 raise Http404 / post = get)object_or_404(Post, id=100) 없는 id 접근시 발생
500 서버오류
