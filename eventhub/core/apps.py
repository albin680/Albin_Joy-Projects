from django.apps import AppConfig

class CoreConfig(AppConfig):
    # This sets the type of auto-generated primary keys for your models
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'