from django.conf.urls import url

from oscar.core.application import DashboardApplication

from apps.dashboard.blog import views


class CommsDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^$', views.PostsListView.as_view(), name='posts-list'),
            url(
                r'^post_create/$',
                views.PostCreateView.as_view(),
                name='post-create'),
            url(
                r'^post/(?P<pk>\d+)/edit/$',
                views.PostEditView.as_view(),
                name='post-edit'),
            url(
                r'^post/(?P<pk>\d+)/delete/$',
                views.PostDeleteView.as_view(),
                name='post-delete'),
        ]
        return self.post_process_urls(urls)


application = CommsDashboardApplication()
