# Generated by Django 3.2.21 on 2023-10-13 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_order_click_and_collect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]
