# Generated by Django 5.1.1 on 2024-10-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_teacher_foiz_alter_teacher_oyligi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='birth',
            field=models.DateField(),
        ),
    ]
