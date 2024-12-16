from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class BlogListView(View):
    def get(sefl,request, *args, **kwargs):
        return render (request, 'blog_list.html', context)