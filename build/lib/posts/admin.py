from django.urls import reverse, NoReverseMatch
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin
from posts.models import Post, Section


@admin.register(Section)
class SectionAdmin(TabbedDjangoJqueryTranslationAdmin, admin.ModelAdmin):
    pass


@admin.register(Post)
class MultilingualModelAdmin(TabbedDjangoJqueryTranslationAdmin, PlaceholderAdminMixin, admin.ModelAdmin):
    fields = ('title', 'section', 'edit_link', 'detail_url', 'published')
    readonly_fields = ('detail_url', 'edit_link',)
    list_display = ('title', 'edit_link', 'section', 'created', 'modified', 'published')
    list_editable = ('section', 'published')

    def edit_link(self, obj):

        try:
            post_section = Post.objects.get(id=obj.id).section.namespace
            return format_html(_("<a href='%s' target='_blank'>Edit</a>") % reverse('%s:%s' % (post_section, 'post_detail'), kwargs={'id': obj.id, 'slug': obj.slug}))

        except NoReverseMatch:
            return format_html(_("<span>Make a page with post namespace apphook</span>"))

        except:
            return format_html(_("<span>Save your post first</span>"))

    edit_link.allow_tags = True
    edit_link.short_description = _('Edit post live on page')
