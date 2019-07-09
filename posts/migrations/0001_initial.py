import autoslug.fields
import cms.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import posts.models


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='LatestPostsCMSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='posts_latestpostscmsplugin', serialize=False, to='cms.CMSPlugin')),
                ('items', models.PositiveIntegerField(default=3, help_text='Minimum is 1, maximum is 100', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Number of posts')),
            ],
            options={
                'verbose_name': 'Latest posts by section plugin',
                'verbose_name_plural': 'Latest posts by section plugins',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True, verbose_name='Slug')),
                ('date', models.DateTimeField(null=True, verbose_name='Date')),
                ('detail_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Detail url')),
                ('published', models.BooleanField(blank=True, default=False, verbose_name='Published')),
                ('post_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname=posts.models.post_detail_placeholder, to='cms.Placeholder')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('namespace', models.CharField(max_length=255, verbose_name='Namespace')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_section', to='posts.Section', verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='latestpostscmsplugin',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_posts_by_section_plugin', to='posts.Section', verbose_name='Section'),
        ),
    ]
