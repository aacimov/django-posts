from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from posts.models import Post, Section


@register(Section)
class SectionTranslation(TranslationOptions):
    fields = ("title",)


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ("title",)
