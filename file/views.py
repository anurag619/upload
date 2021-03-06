from file.models import file_file
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from file.forms import file_fileForm
from django.core.context_processors import csrf


def home(request):
    return render(request, 'file/home.html')

def about(request):
    return render(request, 'file/about.html')


def add_file(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = file_fileForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
           
            form.save()
            return HttpResponseRedirect('/file/home') # Redirect after POST

    else:
          form = file_fileForm() # An unbound form
   
    args={}
    args.update(csrf(request))
    args['form']= form

    return render_to_response('file/add_file.html', args)







