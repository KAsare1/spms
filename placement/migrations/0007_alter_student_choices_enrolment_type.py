# Generated by Django 4.2.6 on 2023-10-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0006_student_choices_enrolment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_choices',
            name='Enrolment_Type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Fee paying', 'Fee Paying'), ('International', 'International')], max_length=200),
        ),
    ]
