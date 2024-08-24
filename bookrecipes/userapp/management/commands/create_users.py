from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Create [count] users at a time.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='quantity users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(count):
            user = User(name=f'Alex{i}', email=f'{i}example@mail.com', gender='M',
                        password=f'12345678', username=f'{i}example@mail.com')
            user.save()
