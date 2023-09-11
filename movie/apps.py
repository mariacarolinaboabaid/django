from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movie"

    def ready(self):
        from .models import User
        import os
        
        # Creating a Super User
        email = os.getenv('EMAIL_ADMIN')
        password = os.getenv('PASSWORD_ADMIN')
        
        users = User.objects.filter(email=email)
        if not users:
            User.objects.create_superuser(username='admin', email=email, password=password, 
                                          is_active=True, is_staff=True)