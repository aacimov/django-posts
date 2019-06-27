from django.shortcuts import render
from django.views.generic.base import View

from posts.models import Post, Section


class PostDetail(View):
    model = Post
    template_name = 'posts/post_detail.html'

    def get(self, request, id, *args, **kwargs):

        try:
            section = Section.objects.get(namespace=request.current_page.application_namespace)
        except:
            section = None

        try:
            post = Post.objects.get(id=id)
        except:
            post = None

        context = {
            "post": post,
            "section": section,
            'request': request,
        }

        return render(request, self.template_name, context)


class PostList(View):
    model = Post
    template_name = 'posts/posts_list.html'

    def get(self, request, *args, **kwargs):

        try:
            section = Section.objects.get(namespace=request.current_page.application_namespace)
        except:
            section = None

        posts = Post.objects.filter(published=True, section__namespace=section)

        context = {
            "section": self.model.section,
            "posts": posts,
            'request': request,
        }

        return render(request, self.template_name, context)

