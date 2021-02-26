from django.shortcuts import render
from blog.models import BlogAuthor, Blog, BlogComment
from django.views import generic


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
