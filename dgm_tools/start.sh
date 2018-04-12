#!/bin/sh
if [$COLLECT_STATIC == 'True']; then
    python3 /dgm_tools/dgm_tools/manage.py collectstatic
fi

if [$RUN_MIGRATIONS == 'True']; then
    python3 /dgm_tools/dgm_tools/manage.py migrate
fi

uwsgi --http :8000 --chdir /dgm_tools/ --module dgm_tools.wsgi --env DJANGO_SETTINGS_MODULE=dgm_tools.settings --master --processes 4 --threads 2 --stats :9191