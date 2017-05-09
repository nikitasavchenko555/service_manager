from django import forms
from django.utils import timezone
from django.forms import ModelForm, inlineformset_factory, ModelChoiceField
from .models import issues, equipment, equipment_manager, groups_of_reason, solutions, status_issue
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class IssuesForm(ModelForm):
    
     class Meta:
         model = issues
         fields = ['level_issue', 'current_status', 'brief_description', 'start_down_date', 'start_down_time', 'start_issue_date', 'start_issue_time', 'workspace',  'creator', 'groups_of_work', 'coordinator', 'executor', 'progress', 'group_of_reason', 'solution', 'comment', 'close_down_date', 'close_down_time', 'close_issue_date', 'close_issue_time']
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
         self.fields['group_of_reason'].initial = groups_of_reason.objects.get(pk=7)
         self.fields['solution'].initial = solutions.objects.get(pk=7)
         self.fields['current_status'].initial = status_issue.objects.get(pk=1)
        

class IssuesEditForm(ModelForm):
     
     class Meta:
         model = issues
         fields = ['level_issue', 'current_status', 'brief_description', 'start_down_date', 'start_down_time', 'start_issue_date', 'start_issue_time', 'groups_of_work', 'coordinator', 'executor', 'progress', 'group_of_reason', 'solution', 'comment', 'close_down_date', 'close_down_time', 'close_issue_date', 'close_issue_time']
         widgets = {'progress': forms.Textarea, 'brief_description': forms.Textarea }
         
         
     def __init__(self, *args, **kwargs):
         super(IssuesEditForm, self).__init__(*args, **kwargs)
         self.fields['start_down_date'].widget = widgets.AdminDateWidget()
         self.fields['start_down_time'].widget = widgets.AdminTimeWidget()
         self.fields['start_issue_date'].widget = widgets.AdminDateWidget()
         self.fields['start_issue_time'].widget = widgets.AdminTimeWidget()
         self.fields['close_down_date'].widget = widgets.AdminDateWidget()
         self.fields['close_down_time'].widget = widgets.AdminTimeWidget()
         self.fields['close_issue_date'].widget = widgets.AdminDateWidget()
         self.fields['close_issue_time'].widget = widgets.AdminTimeWidget()
         self.fields['progress'].initial = timezone.now()

class ReportForm(forms.Form):
       start_period = forms.DateField(widget=AdminDateWidget())
       end_period = forms.DateField(widget=AdminDateWidget())
         





    

