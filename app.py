from django.conf.urls import include, url
from oscar.app import Shop as OscarApp


from apps.blog.app import application as blog_app


class Shop(OscarApp):
    def get_urls(self):
        urls = super(Shop, self).get_urls()

        urls += [
            url(r'^blog/', include(blog_app.urls)),
        ]
        return self.post_process_urls(urls)


application = Shop()
