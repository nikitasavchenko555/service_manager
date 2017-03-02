from django import forms
from .models import *


class IssuesForm(ModelForm):
     class Meta:
         model = issues
         fields = ['number_issue', 'level_issue', 'current_status', 'brief_description', 'start_downtime', 'start_issue',
 'workspace', 'equipment_name', 'equipment_model', 'equipment_inventory', 'creator', 'groups_of_work', 'coordinator', 'executor', 'progress', 'group_of_reason', 'solution', 'comment']
         widgets = {'progress': forms.Textarea, 'brief_description': forms.Textarea}

