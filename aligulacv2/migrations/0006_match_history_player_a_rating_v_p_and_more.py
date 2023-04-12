# Generated by Django 4.1.2 on 2022-11-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aligulacv2', '0005_alter_match_history_player_a_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_history',
            name='player_a_rating_v_p',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='match_history',
            name='player_a_rating_v_t',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='match_history',
            name='player_a_rating_v_z',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='match_history',
            name='player_b_rating_v_p',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='match_history',
            name='player_b_rating_v_t',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='match_history',
            name='player_b_rating_v_z',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='player_stats',
            name='rating_v_p',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='player_stats',
            name='rating_v_t',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='player_stats',
            name='rating_v_z',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='match_history',
            name='player_a_rating',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='match_history',
            name='player_b_rating',
            field=models.IntegerField(default=1000),
        ),
    ]
