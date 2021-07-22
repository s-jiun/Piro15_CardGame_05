# Generated by Django 3.2.5 on 2021-07-22 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_card', models.PositiveIntegerField(default=0)),
                ('guest_card', models.PositiveIntegerField(default=0)),
                ('rule', models.CharField(choices=[('숫자가 더 큰 사람', '숫자가 더 큰 사람'), ('숫자가 더 적은 사람', '숫자가 더 적은 사람')], max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_guest', to='game.user')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_host', to='game.user')),
            ],
        ),
    ]