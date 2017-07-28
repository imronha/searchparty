from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import base64

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST':
        # myfile = request.FILES['myfile']
        # print myfile
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        context = {
            # 'uploaded_file_url': uploaded_file_url,
            'img': request.POST['image'],
            'submitted': 'true;'
        }
        return render(request, 'core/simple_upload.html', context)
        # return render(request, 'core/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    context = {
        'submitted': 'false;',
    }
    return render(request, 'core/simple_upload.html', context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
