# Generated by Django 4.2.5 on 2023-10-02 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('account_created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('account_updated', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
            options={
                'db_table': 'user_accounts',
            },
        ),
    ]
