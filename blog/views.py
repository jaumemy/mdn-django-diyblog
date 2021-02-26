from django.shortcuts import render
from blog.models import BlogAuthor, Blog, BlogComment
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):

    num_blogs = Blog.objects.all().count()
    num_comments = BlogComment.objects.all().count()
    num_authors = BlogAuthor.objects.all().count()

    context = {
        'num_blogs': num_blogs,
        'num_comments': num_comments,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)



class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog


class BlogAuthorListView(generic.ListView):
    model = BlogAuthor


class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor


class BlogCommentCreate(LoginRequiredMixin, CreateView):

    model = BlogComment
    fields = ['description']

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})
