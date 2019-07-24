from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='external_url',
            field=models.URLField(blank=True, help_text='If post is published on an external webiste, use this field to link the title and the image to the external source. Opens in new window.', verbose_name='Post external URL'),
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Shown on post lists', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Featured image'),
        ),
    ]
