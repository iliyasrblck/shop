from django.apps import AppConfig


class SabzenoConfig(AppConfig):
    name = 'sabzeno'

    def ready(self):
        import sabzeno.signals