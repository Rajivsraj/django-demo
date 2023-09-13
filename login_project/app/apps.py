from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    default_app_config = "app.apps.AppConfig"

    def ready(self):
        import app.signals



