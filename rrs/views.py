# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, TemplateView
from rrs.models import Retreat, Session, Attendee
from rrs.forms import RetreatForm, SessionForm, AttendSessionForm

# Create your views here.
class RetreatListView(ListView):
    paginate_by = 10
    model = Retreat

class RetreatCreateView(CreateView):
    form_class = RetreatForm
    model = Retreat

class RetreatDetailView(DetailView):
    model = Retreat

class SessionCreateView(CreateView):
    form_class = SessionForm
    model = Session

class SessionDetailView(DetailView):
    model = Session

    def get_context_data(self, **kwargs):
        context = super(SessionDetailView, self).get_context_data(**kwargs)
        session_name = {
            'faculty': 'Faculty',
            'staff': 'Staff',
            'age_group': 'Age Group'
        }

        context['session_type'] = session_name[self.object.session_type]
        return context

class AttendSessionCreateView(CreateView):
    form_class = AttendSessionForm
    model = Attendee

class AttendeeDetailView(DetailView):
    model = Attendee

    def get_context_data(self, **kwargs):
        context = super(AttendeeDetailView, self).get_context_data(**kwargs)
        gender_name = {
            'm': 'Male',
            'f': 'Female',
        }

        context['get_gender'] = gender_name[self.object.gender]
        return context
