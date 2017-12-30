from django.conf.urls import include, url

from oscar.apps.dashboard import app

from apps.dashboard.blog.app import application as blog_app


class DashboardApplication(app.DashboardApplication):
    def get_urls(self):
        base_urls = super(DashboardApplication, self).get_urls()

        urls = [
            url(r'^blog/', include(blog_app.urls)),
        ]
        return self.post_process_urls(urls + base_urls)


application = DashboardApplication()
