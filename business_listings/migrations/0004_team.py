# Generated by Django 4.2.7 on 2023-12-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_listings', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
            ],
        ),
    ]
