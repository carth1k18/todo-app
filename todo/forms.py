from django import forms
from .models import Project, Todo
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['unique id','title','created_date','list of todos']
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['unique id', 'description', 'status', 'created_date', 'updated_date']
