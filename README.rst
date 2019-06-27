=====
Posts
=====

Posts is a simple Django app for adding blog functionality to your Django CMS based website (placeholder that accepts installed CMS plugins: text, image, file, video, etc.). It supports multiple sections hooked to a page as an AppHook with front end editing as a normal Django CMS page. Multilanguage is also supported.

Quick start
-----------

1. Add "posts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        modeltranslation, # included before all other apps
        ...
        'autoslug', # AutoSlug model field to auto-generate slug
        'model_utils', # model utilities (TimestampedModel mixin for created and modified fields)
        'posts',
    ]

2. App has 3 extra dependencies as stated above: django-modeltranslation, django-autoslug and django-model-utils so install them first using pip

3. Run `python manage.py migrate` to create the posts models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create sections and posts.

5. Create a new section and add its `namespace`

6. Add a new page or hook the app to the existing page (Advanced settings - Application - Select `Posts` from the dropdown - Select Section name from the dropdown)

7. Add new post from the Admin (POSTS - Posts - Add new - Add title - Select Section - Save and continue editing - Edit link appears to edit the page live)

8. View the page in your browser, your post list will be displayed with the link to the post detail
