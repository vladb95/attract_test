from django.core.management.base import BaseCommand, CommandError
from task1.models import Document,People

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self,*args,**options):
        education_like=args[0] if len(args)<=1 else args.join(',')
        people=Document.objects.filter(education__contains=education_like)
        if(len(people)>0):
            for person in people:
                self.stdout.write(str(person))
            return
        self.stdout.write('Any of people hasn\'t this education')
