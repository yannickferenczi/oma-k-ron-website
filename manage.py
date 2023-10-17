#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

if os.path.isfile('env.py'):
    import env

development = os.environ.get('DEVELOPMENT', False)


def main():
    """Run administrative tasks."""
    if development == 'True':
        os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE',
            'oma_k_ron.dev_settings',
        )
    else:
        os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE',
            'oma_k_ron.prod_settings',
        )
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
    main()
