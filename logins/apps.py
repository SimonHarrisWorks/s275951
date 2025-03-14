from django.apps import AppConfig

# used aids in handling of large data
class LoginsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    ## defines the name of the app
    name = 'logins'
