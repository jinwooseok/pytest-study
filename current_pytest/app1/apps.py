'''django 기본 AppConfig'''
from django.apps import AppConfig

class App1Config(AppConfig):
    '''app1 구성을 위한 설정'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
