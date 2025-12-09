from django.apps import AppConfig
import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Caminho da pasta principal do projeto (onde está o manage.py)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Pastas que queremos garantir que existam
        pastas = ['xml', 'relatorios']

        for pasta in pastas:
            caminho = os.path.join(base_dir, pasta)

            if not os.path.exists(caminho):
                os.makedirs(caminho)
                print(f"Pasta criada automaticamente: {caminho}")
