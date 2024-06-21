from django.core.management.base import BaseCommand
# Here name of the Class always be command, NOte:
class Command(BaseCommand):

    def handle(self, *args: any, **options : any):
        # Here you can write your code to be executed when the command is called
        print("Second command ")