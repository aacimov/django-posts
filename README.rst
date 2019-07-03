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
        'cms',
        'posts',
    ]

2. App has dependencies so they should be included before the posts app

3. Run `python manage.py migrate` to apply the posts models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to create sections and posts.

5. Create a new section and add its `Namespace`

6. Add a new page or hook the app to the existing page (`Advanced settings` -> `Application`: Select `Posts` from the dropdown -> `Application Configuration`: Select Section name from the dropdown -> Click `Save`)

7. Add new post from the Admin (POSTS: Posts -> `Add new` -> Add `Title` -> Select `Section` -> Click `Save and continue editing` -> `Edit` link appears to edit the page live)

8. View the page in your browser, your post list will be displayed with the link to the post detail

NOTE: Posts have a `Published` field to control whether they are visible in list view, however they can be edited while not visible from the admin using the `Edit` link

Supported versions
-----------
- Python 3.x
