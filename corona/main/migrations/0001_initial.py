# Generated by Django 2.2.4 on 2020-03-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_location', models.CharField(choices=[('country', 'country'), ('city', 'city'), ('state', 'state'), ('ip', 'ip'), ('GPS', 'GPS')], max_length=7)),
                ('location', models.CharField(default='india', max_length=200)),
            ],
        ),
    ]
