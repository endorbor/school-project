# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200, verbose_name='school name')),
                ('description', models.TextField(verbose_name='school description')),
                ('email', models.EmailField(max_length=254, verbose_name='school email')),
                ('tel', models.CharField(max_length=14, verbose_name='school telephone')),
                ('address', models.CharField(max_length=300, verbose_name='school address')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'abouts',
            },
        ),
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u0639\u0646\u0648\u0627\u0646 \u0641\u0639\u0627\u0644\u06cc\u062a', max_length=300, verbose_name='\u0639\u0646\u0648\u0627\u0646')),
                ('img', models.ImageField(default='images/gallery/defaults.jpg', help_text='size', upload_to='images/gallery/', verbose_name='\u062a\u0635\u0648\u06cc\u0631')),
                ('date', models.DateField(verbose_name='\u062a\u0627\u0631\u06cc\u062e')),
                ('summary', models.TextField(default='\u062e\u0644\u0627\u0635\u0647 \u0641\u0639\u0627\u0644\u06cc\u062a', verbose_name='\u062e\u0644\u0627\u0635\u0647 \u0641\u0639\u0627\u0644\u06cc\u062a')),
                ('Comments', models.TextField(verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a')),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='\u0622\u0645\u0648\u0632\u0634\u06cc', max_length=50, verbose_name='\u0646\u0648\u0639')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('imgone', models.ImageField(default='images/gallery/defaults.jpg', help_text='size', upload_to='images/gallery/', verbose_name='\u062a\u0635\u0648\u06cc\u0631 \u0627\u0648\u0644')),
                ('imgtwo', models.ImageField(default='images/gallery/defaults.jpg', help_text='size', upload_to='images/gallery/', verbose_name='\u062a\u0635\u0648\u06cc\u0631 \u062f\u0648\u0645')),
                ('date', models.DateField(verbose_name='\u062a\u0627\u0631\u06cc\u062e')),
                ('text', models.TextField(verbose_name='\u0645\u062a\u0646')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolApp.categories', verbose_name='\u0646\u0648\u0639')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u0639\u0646\u0648\u0627\u0646')),
                ('day', models.DateField(verbose_name='\u0631\u0648\u0632')),
                ('date', models.DateField(verbose_name='\u062a\u0627\u0631\u06cc\u062e')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u0639\u0646\u0648\u0627\u0646')),
                ('small_img', models.ImageField(default='images/gallery/defaults.jpg', help_text='size', upload_to='images/gallery/', verbose_name='\u0639\u06a9\u0633')),
                ('large_img', models.ImageField(default='images/gallery/defaults.jpg', help_text='size', upload_to='images/gallery/', verbose_name='\u0639\u06a9\u0633')),
                ('alt', models.CharField(default='', max_length=100, verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0639\u06a9\u0633')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u0639\u0646\u0648\u0627\u0646')),
                ('summary', models.TextField(default='title of news', verbose_name='\u062e\u0644\u0627\u0635\u0647 \u062e\u0628\u0631')),
                ('content', models.TextField(verbose_name='\u0645\u062a\u0646 \u062e\u0628\u0631')),
                ('img', models.ImageField(default='images/news/defaults.jpg', help_text='size(1400*714)', upload_to='images/news/', verbose_name='\ufe96\ufebb\ufeed\u06cc\ufead')),
                ('date', models.DateField(verbose_name='\u062a\u0627\u0631\u06cc\u062e')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='\u0646\u0627\u0645')),
                ('last_name', models.CharField(max_length=100, verbose_name='\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc')),
                ('post', models.CharField(max_length=100, verbose_name='\u0633\u0645\u062a')),
                ('grades', models.CharField(max_length=100, verbose_name='\u0645\u062f\u0631\u06a9')),
                ('image', models.ImageField(blank=True, help_text='size', null=True, upload_to='images/teacher/', verbose_name='image')),
            ],
            options={
                'verbose_name': '\u067e\u0631\u0633\u0646\u0644',
            },
        ),
        migrations.AddField(
            model_name='activities',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolApp.categories', verbose_name='\u0646\u0648\u0639'),
        ),
    ]
