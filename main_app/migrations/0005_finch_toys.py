# Generated by Django 4.2.5 on 2023-09-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy_alter_feeding_options_alter_feeding_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
