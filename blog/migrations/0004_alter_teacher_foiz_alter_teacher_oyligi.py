# Generated by Django 5.1.1 on 2024-10-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_lesson_date_alter_teacher_pupilnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='foiz',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='oyligi',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
