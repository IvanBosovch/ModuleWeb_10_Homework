# Generated by Django 5.0.2 on 2024-02-12 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_qoutes_quotes_alter_authors_born_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='create',
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='create',
        ),
    ]