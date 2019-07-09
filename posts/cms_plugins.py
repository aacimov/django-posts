from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from posts.models import LatestPostsCMSPlugin, Section, Post


class LatestPostsPlugin(CMSPluginBase):
	module = 'Posts'
	model = LatestPostsCMSPlugin
	name = _('Latest Posts Plugin')
	render_template = "posts/plugins/latest_posts_plugin.html"
	cache = False

	def render(self, context, instance, placeholder):
		try:
			context = super(LatestPostsCMSPlugin, self).render(context, instance, placeholder)
		except:
			pass

		section = instance.section
		items = instance.items
		context.update({'section': section})

		posts = Post.objects.filter(section=section, published=True).order_by('-date')[:items]

		context.update({'posts': posts})

		return context


plugin_pool.register_plugin(LatestPostsPlugin)

