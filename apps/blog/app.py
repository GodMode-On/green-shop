from django.conf.urls import url

from oscar.core.application import Application

from apps.blog import views


class BlogApplication(Application):
    name = 'blog'

    def get_urls(self):
        urls = [
            url(r'^$', views.PostsListView.as_view(), name='posts-list'),
            url(
                r'^post/(?P<pk>\d+)/detail/$',
                views.PostDetailView.as_view(),
                name='post-detail'),
            # url(
            #     r'^post/(?P<pk>\d+)/edit/$',
            #     views.PostEditView.as_view(),
            #     name='post-edit'),
            # url(
            #     r'^post/(?P<pk>\d+)/delete/$',
            #     views.PostDeleteView.as_view(),
            #     name='post-delete'),
        ]
        return self.post_process_urls(urls)


application = BlogApplication()
