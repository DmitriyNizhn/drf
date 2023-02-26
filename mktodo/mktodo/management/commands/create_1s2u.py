import django.contrib.auth.management
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import call_command
from django.core.management.base import BaseCommand

from users.models import Users


class Command(BaseCommand):
    help = "This command create superuser and two users"
