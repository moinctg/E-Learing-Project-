# Generated by Django 3.0.3 on 2020-06-17 14:15

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
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('present_address', models.TextField(blank=True, null=True)),
                ('perment_address', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
