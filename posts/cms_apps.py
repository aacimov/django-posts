from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from posts.cms_app_config import CMSConfigApp
from posts.models import Section


class PostsApp(CMSConfigApp):
    app_config = Section
    app_name = 'posts'
    name = _(u'Posts')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['posts.urls']


apphook_pool.register(PostsApp)

