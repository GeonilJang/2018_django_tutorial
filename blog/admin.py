from django.contrib import admin
from .models import Post, Comment,Tag
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','title','create_at','status','content_size','update_at']
    list_display_links = ['title']
    actions = ['make_published','make_widthraw','make_draft','myfun']

    def content_size(self, post):
        return '<strong>{}글자</strong>'.format(len(post.content)) #1
        #2 mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description ='글자수'
    content_size.allow_tags = True #1

    #모든 액션은 첫번째는 request를 받고 두 번째로는 queryset을 받습니다.
    def make_published(self, request, queryset):
        update_count = queryset.update(status='p')
        self.message_user(request, '{}건이 포스팅 되었습니다.'.format(update_count))

    def make_draft(self, request, queryset):
        update_count = queryset.update(status='d')
        self.message_user(request, '{}건이 드레프트 되었습니다.'.format(update_count))

    def make_widthraw(self, request, queryset):
        update_count = queryset.update(status='w')
        self.message_user(request, '{}건이 위드로우 되었습니다..'.format(update_count))

    def myfun(selg, request, queryset):
        update_date = queryset.update(content="hell world")

"""
list_editable -> 목록 상에서 수정할 필드 목록
list_per_page -> 페이지별로 보여질 최대 갯 수
list_filter -> 필토 옵션을 제공할 필드 목록
action -> 한 번의 여러개 수행!!


"""

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','message','author','update_at']
    list_display_links =['message']

@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links =['name']
