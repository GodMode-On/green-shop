from django.views import generic

from apps.blog import models


class PostsListView(generic.ListView):
    model = models.Post
    template_name = 'dashboard/blog/posts_list.html'
    paginate_by = 10
    context_object_name = 'posts'
    ordering = '-date_added'
