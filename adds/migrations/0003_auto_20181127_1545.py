# Generated by Django 2.0.8 on 2018-11-27 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adds', '0002_post_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Ad',
        ),
        migrations.AddField(
            model_name='adimage',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='adds.Ad'),
        ),
    ]