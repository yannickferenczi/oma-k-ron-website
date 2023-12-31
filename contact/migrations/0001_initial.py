# Generated by Django 3.2.21 on 2023-10-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('subject', models.CharField(choices=[('feedback', 'Feedback'), ('general', 'General'), ('subscriptions', 'Subscriptions'), ('reclamation', 'Reclamation'), ('product_info', 'Information Product')], max_length=150)),
                ('message', models.TextField(max_length=700, verbose_name='Your message')),
                ('answered', models.BooleanField(default=False)),
            ],
        ),
    ]
