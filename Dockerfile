FROM            azelf/greenwrap:base

ENV             DJANGO_SETTINGS_MODULE  config.settings.local

COPY            .   /srv/project
CMD             python /srv/project/app/manage.py runserver 0:8000

EXPOSE          8000
