# Generated by Django 4.1.4 on 2022-12-11 07:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_person_play_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.AddField(
            model_name='club',
            name='team_pic',
            field=models.ImageField(blank=True, default='defaultimg.png', null=True, upload_to='', verbose_name='Team Image'),
        ),
        migrations.AlterField(
            model_name='play',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team', to='baseball.club'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score_t1', models.IntegerField()),
                ('score_t2', models.IntegerField()),
                ('game_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Date of Issuance')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team1', to='baseball.club')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team2', to='baseball.club')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Winner', to='baseball.club')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
