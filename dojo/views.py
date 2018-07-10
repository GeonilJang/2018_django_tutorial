from django.shortcuts import render

#1
from django.http import HttpResponse

# Create your views here.
def myfun(request, a,b):
    rs = int(a)+int(b)
    # return render(request, 'dojo/myfun.html',{
    #     "ra":a,
    #     "rb":b,
    #     "rs":rs,
    # })
    return HttpResponse(rs)
    # print("{} + {} = {}".format(a,b,a+b))

#fbv cbv 로 나누어 진다.
