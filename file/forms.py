from django import forms
from file.models import file_file

class file_fileForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="enter the title of the file to add")
    pub_date = forms.DateTimeField(widget=forms.HiddenInput())
    files = forms.FileField()
    
    class Meta:
       model= file_file
