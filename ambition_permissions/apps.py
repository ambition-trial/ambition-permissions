from django.apps import AppConfig as DjangoApponfig

# from django.core.checks import register

# from .system_checks import ambition_permission_check


class AppConfig(DjangoApponfig):
    name = "ambition_permissions"
    verbose_name = "Ambition Authentication and Permissions"
    # register(ambition_permission_check)
