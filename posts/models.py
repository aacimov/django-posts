from autoslug import AutoSlugField
from django.db import models
from cms.models.fields import PlaceholderField
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


def post_detail_placeholder(instance):
	return 'Post detail'


class Section(TimeStampedModel):
	title = models.CharField("Title", max_length=255)
	slug = AutoSlugField(unique=True, populate_from='title', always_update=True)
	namespace = models.CharField(_("Namespace"), max_length=255)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _(u"Section")
		verbose_name_plural = _(u"Sections")


class Post(TimeStampedModel):
	title = models.CharField("Title", max_length=255)
	slug = AutoSlugField(_("Slug"), unique=True, populate_from='title', always_update=True)
	section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL, related_name="post_section", verbose_name=_("Section"))
	detail_url = models.CharField(_("Detail url"), blank=True, null=True, max_length=255)
	post_content = PlaceholderField(post_detail_placeholder)
	published = models.BooleanField(_("Published"), default=False, blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		try:
			section_namespace = self.section.namespace
		except:
			section_namespace = ''
		self.detail_url = '%s:%s' % (section_namespace, 'post_detail')
		super(Post, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _(u"Post")
		verbose_name_plural = _(u"Posts")


