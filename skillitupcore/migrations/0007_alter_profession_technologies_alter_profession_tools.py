# Generated by Django 4.1 on 2022-08-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillitupcore', '0006_course_expert_trendingtool_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='skillitupcore.trendingtech'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='tools',
            field=models.ManyToManyField(blank=True, to='skillitupcore.trendingtool'),
        ),
    ]
