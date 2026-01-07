from django.apps import AppConfig


class AcccessControlConfig(AppConfig):
    name = "acccess_control"

    def ready(self):
        import acccess_control.signals  
