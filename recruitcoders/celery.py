from __future__ import absolute_import, unicode_literals

import os
import time

from celery import Celery
from django.apps import apps
from django.conf import settings
from redis import Redis

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruitcoders.settings")

app = Celery("recruitcoders", broker=settings.CELERY_BROKER_URL)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# Configuração do Celery Beat
app.conf.beat_schedule = {
    "atualizar-vagas-expiradas": {
        "task": "vagas.tasks.atualizar_vagas_expiradas",
        "schedule": 60 * 5,
    },
}

if __name__ == "__main__":
    app.start()
