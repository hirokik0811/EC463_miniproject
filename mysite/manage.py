#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from setuptools import setup



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    """
    setup(name='miniproject',
      version='0.1',
      description='EC463 SW mini project',
      url='https://github.com/hirokik0811/EC463_miniproject',
      author='Hiroki Kawai, Zachary Bachrach',
      author_email='hirokik@bu.edu',
      license='MIT',
      packages=['miniproject'],
      install_requires=[
          'django',
          'social-auth-app-django',
          'geoip2',
          'matplotlib',
          'postgres',
          'django-tz-detect'
      ],
      zip_safe=False)
    """
    main()
