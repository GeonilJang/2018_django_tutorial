# 2018_django_tutorial

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
