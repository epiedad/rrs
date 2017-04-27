# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rrs.models import (Retreat, MealPlan, Department, Session, SessionChair, Attendee, Dependent)
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"

# Register your models here.
@admin.register(Retreat)
class RetreatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'retreat_datetime',
                    'recurring_datetime']
    prepopulated_fields = {'slug': ('name',), }
    search_fields = ('name',)
    ordering = ('-retreat_datetime',)

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ['plan_name', 'meal_price']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

class SessionChairInline(admin.StackedInline):
    model = SessionChair
    extra = 1

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'retreat', 'session_type']
    prepopulated_fields = {'slug': ('title',), }
    inlines = [SessionChairInline]

class DependentInline(admin.StackedInline):
    model = Dependent
    extra = 3

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'session', 'meal_plan',
                    'department', 'telephone', 'job_type', 'age', 'gender']
    inlines = [DependentInline]

