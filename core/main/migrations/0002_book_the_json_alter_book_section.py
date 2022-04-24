# Generated by Django 4.0.4 on 2022-04-24 08:09

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='the_json',
            field=jsonfield.fields.JSONField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='section',
            field=models.CharField(max_length=100),
        ),
    ]
