from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Importing for Class Based Views(CBV) and Mixins
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Importing Models
from App_Blog.models import BlogPost, BlogComment, BlogLike
from App_Login.models import UserProfile

# Importing for Unique ID
from uuid import uuid4



# Create your views here.
# For Add Blog
class AddBlog(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'App_Blog/add_blog.html'
    fields = ['blog_title', 'blog_content', 'blog_image']

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.author = self.request.user
        title = form_obj.blog_title
        form_obj.blog_slug = title.replace(' ', '-') + '-' + str(uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:blogs'))



# For Blogs
class BlogList(ListView):
    model = BlogPost
    template_name = 'App_Blog/blogs.html'
    context_object_name = 'blog_posts'
    ordering = ['-publish_date']



# For Blog Detail
# @login_required
def BlogDetail(request, blog_slug):
    blog_post = BlogPost.objects.get(blog_slug=blog_slug)

    return render(request, 'App_Blog/blog_detail.html', context={'blog_post': blog_post})