# Generated by Django 4.0.4 on 2022-04-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book_the_json_alter_book_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='the_json',
        ),
        migrations.AlterField(
            model_name='book',
            name='section',
            field=models.TextField(max_length=100),
        ),
    ]