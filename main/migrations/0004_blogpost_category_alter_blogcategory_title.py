# Generated by Django 4.0 on 2022-04-10 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(default='4', on_delete=django.db.models.deletion.CASCADE, to='main.blogcategory'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='title',
            field=models.CharField(default='uncategories', max_length=100),
        ),
    ]
