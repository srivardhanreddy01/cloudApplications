import csv
import bcrypt
from django.utils.timezone import now  
from django.core.management.base import BaseCommand
from userAccount.models import UserAccount

class Command(BaseCommand):
    help = 'Load users from a CSV file'

    def handle(self, *args, **options):
        csv_file = '/opt/user.csv'

        def hash_password(password):
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                email = row['email']
                password = hash_password(row['password'])

                user, created = UserAccount.objects.get_or_create(
                    email=email,
                    first_name=row['first_name'], 
                    last_name=row['last_name'],   
                    password=password
                )
                
                if created:
                    user.account_created = now()
                else:
                    user.account_updated = now()
                
                user.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded users from CSV.'))
