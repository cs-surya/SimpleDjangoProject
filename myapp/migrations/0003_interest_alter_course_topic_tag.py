# Generated by Django 4.0.5 on 2022-07-11 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_course_interested_course_stages_alter_course_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interested', models.CharField(max_length=200)),
                ('levels', models.IntegerField(default=1)),
                ('comments', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='myapp.topic'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, null=True)),
                ('orders', models.ManyToManyField(to='myapp.order')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.student')),
                ('topic', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.topic')),
            ],
        ),
    ]