# Generated by Django 3.2.8 on 2021-10-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20211024_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('NR - Not Rate', 'NR - Not Rate'), ('G - General Audiences', 'G - General Audiences'), ('PG – Parental Guidance Suggested', 'PG – Parental Guidance Suggested'), ('PG-13 – Parents Strongly Cautioned', 'PG-13 – Parents Strongly Cautioned'), (4, 'NC-16 – No Children under 16'), (5, 'M-18 – Restricted to persons 18 years and above'), (6, 'R21 – Strictly for adults aged 21 and above')], default='NR - Not Rate', max_length=200),
        ),
    ]
