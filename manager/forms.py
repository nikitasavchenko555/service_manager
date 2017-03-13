from django import forms
from .models import *
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class IssuesForm(ModelForm):
     class Meta:
         model = issues
         fields = ['number_issue', 'level_issue', 'current_status', 'brief_description', 'start_down_date', 'start_down_time', 'start_issue_date', 'start_issue_time', 'workspace', 'equipment_name', 'equipment_model', 'equipment_inventory', 'creator', 'groups_of_work', 'coordinator', 'executor', 'progress', 'group_of_reason', 'solution', 'comment', 'close_down_date', 'close_down_time', 'close_issue_date', 'close_issue_time']
         widgets = {'progress': forms.Textarea, 'brief_description': forms.Textarea }
     def __init__(self, *args, **kwargs):
         super(IssuesForm, self).__init__(*args, **kwargs)
         self.fields['start_down_date'].widget = widgets.AdminDateWidget()
         self.fields['start_down_time'].widget = widgets.AdminTimeWidget()
         self.fields['start_issue_date'].widget = widgets.AdminDateWidget()
         self.fields['start_issue_time'].widget = widgets.AdminTimeWidget()
         self.fields['close_down_date'].widget = widgets.AdminDateWidget()
         self.fields['close_down_time'].widget = widgets.AdminTimeWidget()
         self.fields['close_issue_date'].widget = widgets.AdminDateWidget()
         self.fields['close_issue_time'].widget = widgets.AdminTimeWidget()
         
       


class EventForm(forms.Form):
    Date = forms.DateField(widget = forms.SelectDateWidget)
    datefrom = forms.DateTimeField(label='Дата',  widget=AdminDateWidget())
    time = forms.DateTimeField(label='Время',  widget=AdminTimeWidget())
   

    '''class Meta:
        model = issues
        fields = ('start_downtime','start_issue')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start_downtime'].widget = widgets.AdminDateWidget()
        self.fields['start_issue'].widget = widgets.AdminTimeWidget()'''
    

