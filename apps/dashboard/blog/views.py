# -*- coding: utf-8 -*-

from django.views import generic
from django.core.urlresolvers import reverse

from apps.blog import models
from apps.dashboard.blog import forms


class PostsListView(generic.ListView):
    model = models.Post
    template_name = 'dashboard/blog/posts_list.html'
    paginate_by = 10
    context_object_name = 'posts'
    ordering = '-date_added'


class PostCreateView(generic.CreateView):
    template_name = 'dashboard/blog/post_create_update.html'
    model = models.Post
    form_class = forms.PostCreateUpdateForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(PostCreateView, self).get_context_data(*args, **kwargs)
        ctx['page_title'] = "Створити"
        return ctx

    def get_success_url(self):
        return reverse('dashboard:posts-list')


class PostEditView(generic.UpdateView):
    template_name = 'dashboard/blog/post_create_update.html'
    model = models.Post
    form_class = forms.PostCreateUpdateForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(PostEditView, self).get_context_data(*args, **kwargs)
        ctx['page_title'] = "Редагувати"
        return ctx

    def get_success_url(self):
        return reverse('dashboard:posts-list')


class PostDeleteView(generic.DeleteView):
    model = models.Post

    def get_success_url(self):
        return reverse('dashboard:posts-list')
