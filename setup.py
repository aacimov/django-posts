import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-posts',
	version='0.1',
	packages=['posts'],
	include_package_data=True,
	install_requires=[
		'django-modeltranslation',
		'django-autoslug',
		'django-model-utils',
		'django-cms'
  	],
	license='GNU GPL License',  # example license
	description='A simple Django app to add blog functionality to your Django CMS website.',
	long_description=README,
	url='https://github.com/aacimov/posts',
	author='Aleks Acimovic',
	author_email='alex@multi-task.hr',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 2.x',  # replace "X.Y" as appropriate
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU GPL License',  # example license
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)
