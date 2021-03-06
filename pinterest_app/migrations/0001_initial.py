# Generated by Django 3.1.2 on 2021-11-18 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('privacy', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('alt_txt', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('destination_link', models.URLField(blank=True, null=True)),
                ('type', models.CharField(choices=[('image', 'video')], default='image', max_length=10)),
                ('url', models.ImageField(upload_to='')),
                ('boards', models.ManyToManyField(blank=True, to='pinterest_app.Board')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('followers', models.ManyToManyField(related_name='followees', to='pinterest_app.User')),
                ('friends', models.ManyToManyField(blank=True, to='pinterest_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subscribers', models.ManyToManyField(blank=True, to='pinterest_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='pin_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest_app.pin')),
            ],
        ),
        migrations.AddField(
            model_name='pin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest_app.user'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('message_date', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest_app.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='freind_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='pinterest_app.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='pinterest_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest_app.user'),
        ),
    ]
