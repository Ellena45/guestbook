from django.core.management.base import BaseCommand
import datetime
import sqlite3
from datetime import datetime, timedelta
from base.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        today = datetime.datetime.now()
        timedelta = datetime.timedelta(days=180)
        date_difference = today - timedelta
        queryset = User.objects.filter(leave=datetime)
        print(date_difference)

"""

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int)
        parser.add_argument('--created')
        parser.add_argument('--leave')


    def handle(self, *args, **options):
        if options['id']:
            
            try:
                instance = User.objects.get(id=options['id'])
                instance.delete()
                self.stdout.write(self.style.SUCCESS('User Deleted'))
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR('User not found'))
        elif options['created'] and options['leave']:
            date_range = [options['created'], options['leave']]
            User.objects.filter(datetime_field__range=date_range).delete()
            self.stdout.write(self.style.SUCCESS('Objects Deleted'))
        else:
            self.stdout.write(self.style.ERROR('options are not given'))




class Command(BaseCommand):

    def handle(self, *args, **options):
        today = datetime.datetime.now()
        time_delta = datetime.timedelta(days=180)
        date_difference = today - time_delta
        queryset = User.objects.filter(leave=datetime)

    for user in queryset:

 

 def handle(self, *args, **kwargs):
        first_date = datetime.date(2020, 12, 16)
        second_date = datetime.date(2015, 12, 16)


        result = first_date < second_date
        print(result)






class Command(BaseCommand):
    help = 'Delete User'
    model = User
    queryset = User.objects.filter(leave=datetime)

    for user in queryset:
        user.leave = datetime.now
        user.save()
   print()"""