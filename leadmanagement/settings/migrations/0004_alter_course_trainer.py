# Generated by Django 4.2.7 on 2023-11-20 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0003_alter_branches_adress_alter_branches_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Faculty', 'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL, verbose_name='Trainer'),
        ),
    ]
