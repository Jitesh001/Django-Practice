from django.apps import AppConfig


class DjangoauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoauth'
    
    def ready(self):
        import djangoauth.signals