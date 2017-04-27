# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER = (
    ('m', 'Male'),
    ('f', 'Female')
)

JOB_TYPE = (
    ('faculty', 'Faculty'),
    ('staff', 'Staff')
)

MEAL_PLAN = (
    ('sun', 'Sunday Meal'),
    ('sat', 'Saturday Meal'),
    ('sunsat', 'Saturday & Sunday Meal'),
)

class Retreat(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField()
    retreat_datetime = models.DateTimeField(verbose_name='Retreat Date/Time',db_index=True)
    recurring_datetime = models.DateTimeField(verbose_name='Recurring Date/Time',
                         db_index=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(str(self.name))
        super(Retreat, self).save(*args, **kwargs)

    def retreat_id(self):
        gen_name = [n[0].upper() for n in self.name.split(' ')]
        return '{name}-{num}'.format(name=''.join(gen_name),num=self.pk)

    def get_absolute_url(self):
        return reverse('retreat', kwargs={'pk': self.pk, 'slug': self.slug})

class MealPlan(models.Model):
    plan_name = models.CharField(max_length=100, choices=MEAL_PLAN, db_index=True)
    meal_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.plan_name

class Department(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    def __str__(self):
        return self.name

class AttendeeCommon(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=2, db_index=True, choices=GENDER)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        abstract = True

class Session(models.Model):
    SESSION_TYPE = (
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
        ('age_group', 'Age Group'),
    )
    
    retreat = models.ForeignKey(Retreat, related_name='retreat_sessions')
    session_type = models.CharField(max_length=10, choices=SESSION_TYPE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(str(self.title))
        super(Session, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('session', kwargs={'pk': self.pk, 'slug': self.slug})

class Attendee(AttendeeCommon):
    session = models.ForeignKey(Session, related_name='session_attendees', blank=True)
    meal_plan = models.CharField(max_length=100, choices=MEAL_PLAN, db_index=True)
    department = models.ForeignKey(Department, related_name='department_attendees', blank=True)
    telephone = models.CharField(max_length=30, null=True, blank=True)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_badge_name(self):
        return '{first_name} - {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    def get_absolute_url(self):
        return reverse('attendee', kwargs={'pk': self.pk, 'slug': self.slug})

class Dependent(AttendeeCommon):
    attendee = models.ForeignKey(Attendee, related_name='dependents', blank=True)

    def __str__(self):
        return '{first} {last}'.format(first=self.first_name, last=self.last_name)

class SessionChair(models.Model):
    chair = models.ForeignKey(Session, related_name='session_chairs')
    attendee = models.ForeignKey(Attendee)

    def __str__(self):
        return self.attendee.first_name
