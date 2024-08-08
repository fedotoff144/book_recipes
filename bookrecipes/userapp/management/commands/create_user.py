from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Create a new user.'

    def handle(self, *args, **kwargs):
        user = User(name='Alex', email='example@.mail.com', gender='M', password='12345678')
        user.save()
        return f'{user}'
