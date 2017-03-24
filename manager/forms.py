from django import forms
from django.forms import ModelForm, inlineformset_factory, ModelChoiceField
from .models import issues, equipment, equipment_manager, groups_of_reason, solutions
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class IssuesForm(ModelForm):
     #equipment = equipment.objects.all()
     #equipment_inventory = equipment.inventory_number
     class Meta:
         model = issues
         fields = ['level_issue', 'current_status', 'brief_description', 'start_down_date', 'start_down_time', 'start_issue_date', 'start_issue_time', 'workspace', 'equipment_name', 'creator', 'groups_of_work', 'coordinator', 'executor', 'progress', 'group_of_reason', 'solution', 'comment', 'close_down_date', 'close_down_time', 'close_issue_date', 'close_issue_time']
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
         #self.fields['equipment_name'] = equipment.objects.get_name()#equipment.objects.all().values("name")
         #self.fields['equipment_model'] = equipment.objects.get_model()
         #self.fields['equipment_inventory'].queryset = equipment.objects.all()
         #self.fields['number_issue'].queryset = int(str(issues.objects.values('number_issue').order_by().last()))+1
         #self.fields['number_issue'].widget = forms.TextInput()
       
         
class TestForm(ModelForm):
     class Meta:
         model = equipment
         fields = ['name', 'model', 'inventory_number']
         #widgets = {'model': forms.RadioSelect }
     #equipment_model = forms.ModelChoiceField(queryset=equipment.objects.all(), label = "модель")




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
    

