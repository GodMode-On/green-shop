from django.conf.urls import url

from oscar.core.application import DashboardApplication

from apps.dashboard.blog.views import PostsListView


class CommsDashboardApplication(DashboardApplication):
    name = 'blog'
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^$', PostsListView.as_view(), name='posts-list'),
        ]
        return self.post_process_urls(urls)


application = CommsDashboardApplication()
