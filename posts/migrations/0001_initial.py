# Generated by Django 3.1.6 on 2021-02-11 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBSPosts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=255)),
                ('priority', models.IntegerField(default=1)),
                ('display_level', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbsPost', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='bbsLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BBSReply',
            fields=[
                ('bbsposts_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.bbsposts')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbsReply', to='posts.bbsposts')),
            ],
            bases=('posts.bbsposts',),
        ),
    ]
