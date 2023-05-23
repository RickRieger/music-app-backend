# Generated by Django 4.2.1 on 2023-05-23 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendshipStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAndTime', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Requested', 'requested'), ('Accepted', 'accepted'), ('Declined', 'declined')], default='Requested', max_length=9)),
                ('requestTo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requestTo_status', to=settings.AUTH_USER_MODEL)),
                ('requestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requestor_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('requestor', 'requestTo')},
            },
        ),
    ]
