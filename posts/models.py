from autoslug import AutoSlugField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


def post_detail_placeholder(instance):
	return 'post_detail'


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
	date = models.DateTimeField(_("Date"), null=True)
	section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL, related_name="post_section",
								verbose_name=_("Section"))
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


class LatestPostsCMSPlugin(CMSPlugin):
	section = models.ForeignKey(Section, null=True, related_name="latest_posts_by_section_plugin",
								verbose_name=_('Section'), on_delete=models.SET_NULL)
	items = models.PositiveIntegerField(_("Number of posts"), default=3,
										validators=[MinValueValidator(1), MaxValueValidator(100)],
										help_text=_("Minimum is 1, maximum is 100"))

	def __unicode__(self):
		return "%s" % self.section.title

	class Meta:
		verbose_name = _(u"Latest posts by section plugin")
		verbose_name_plural = _(u"Latest posts by section plugins")
