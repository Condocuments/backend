import os

from django.core.management import BaseCommand, call_command

from people.models import User


class Command(BaseCommand):
    fixture_name = 'load_data'

    def handle(self, *args, **options):
        if not User.objects.filter(username='condo').exists():
            user = User.objects.create_user(username='condo', password='Gerr@rd4')
            user.is_superuser = True
            user.is_staff = True
            user.save()

        call_command('loaddata', os.path.join('initials', 'fixture', 'bedroom_data.json'))
