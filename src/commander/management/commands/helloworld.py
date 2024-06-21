from django.core.management.base import BaseCommand
from typing import Any
# Name of the class always should be Command 
class Command(BaseCommand):
    # here you can Write code to be Executed when the command is called
    def handle(self, *args: Any, **options: Any):
        print("Heloo World")