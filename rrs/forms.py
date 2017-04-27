from django.forms import MultiWidget
from rrs.models import Retreat, Session, Attendee
from django import forms
from datetimewidget.widgets import DateTimeWidget

class RetreatForm(forms.ModelForm):
    class Meta:
        model = Retreat
        fields = ('name', 'description',
                  'retreat_datetime', 'recurring_datetime')

        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian' : True
        }
        widgets = {
            'retreat_datetime': DateTimeWidget(usel10n = True, bootstrap_version=3),
            'recurring_datetime': DateTimeWidget(usel10n = True, bootstrap_version=3),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        exclude = ('slug',)

class AttendSessionForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
