# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels


class About(models.Model):
    school_name = models.CharField(max_length=200, verbose_name=_('school name'))
    description = models.TextField(verbose_name=_('school description'))
    email = models.EmailField(verbose_name=_('school email'))
    tel = models.CharField(max_length=14, verbose_name=_('school telephone'))
    address = models.CharField(max_length=300, verbose_name=_('school address'))

    def __unicode__(self):
        return self.school_name

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('abouts')


class categories(models.Model):
    category = models.CharField(max_length=50, verbose_name=u'نوع', default=u'آموزشی')

    def __unicode__(self):
        return self.category


class activities(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'عنوان', default=u'عنوان فعالیت')
    img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                            verbose_name=u'تصویر', help_text=_('size'))
    date = jmodels.jDateField(verbose_name=u'تاریخ')
    summary = models.TextField(max_length=300, verbose_name=u'خلاصه فعالیت', default=u'خلاصه فعالیت')
    Comments = models.TextField(max_length=300, verbose_name=u'توضیحات')
    category = models.ForeignKey(categories, verbose_name=u'نوع')

    def __unicode__(self):
        return self.title


class Consultation(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    imgone = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                              verbose_name=u'تصویر اول', help_text=_('size'))
    imgtwo = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                              verbose_name=u'تصویر دوم', help_text=_('size'))
    date = jmodels.jDateField(verbose_name=u'تاریخ')
    text = models.TextField(verbose_name=u'متن')
    category = models.ForeignKey(categories, verbose_name=u'نوع')

    def __unicode__(self):
        return self.title


class ConsultationSchedule(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'عنوان')
    day = models.DateField(verbose_name=u'روز')
    date = jmodels.jDateField(verbose_name=u'تاریخ')

    def __unicode__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'عنوان')
    summary = models.TextField(verbose_name=u'خلاصه خبر', default='title of news')
    content = models.TextField(verbose_name=u'متن خبر')
    img = models.ImageField(default='images/news/defaults.jpg', upload_to='images/news/', verbose_name=u'ﺖﺻﻭیﺭ',
                            help_text=_('size(1400*714)'))
    date = jmodels.jDateField(verbose_name=u'تاریخ')

    def __unicode__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'عنوان')
    small_img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                                  verbose_name=u'عکس', help_text=_('size'))
    large_img = models.ImageField(default='images/gallery/defaults.jpg', upload_to='images/gallery/',
                                  verbose_name=u'عکس', help_text=_('size'))
    alt = models.CharField(default='', max_length=100, verbose_name=u'توضیحات عکس')

    def __unicode__(self):
        return self.title


class Personnel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=u'نام')
    last_name = models.CharField(max_length=100, verbose_name=u'نام خانوادگی')
    post = models.CharField(max_length=100, verbose_name=u'سمت')
    grades = models.CharField(max_length=100, verbose_name=u'مدرک')
    image = models.ImageField(blank=True, null=True, upload_to='images/teacher/', verbose_name=_('image'),
                              help_text=_('size'))

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = u'پرسنل'
