# Generated by Django 3.1 on 2020-09-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_auto_20200919_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='WysiwygModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField()),
            ],
        ),
    ]