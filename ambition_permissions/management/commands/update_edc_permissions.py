from django.core.management.base import BaseCommand

from ...updaters import update_permissions


class Command(BaseCommand):

    help = "Update groups and group permissions"

    def handle(self, *args, **options):

        update_permissions()
