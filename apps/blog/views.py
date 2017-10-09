from django.views import generic

from apps.blog import models


class PostsListView(generic.ListView):
    model = models.Post
    template_name = 'blog/posts_list.html'
    paginate_by = 10
    context_object_name = 'posts'
    ordering = '-date_added'


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = models.Post
