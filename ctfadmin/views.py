from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from challs.models import Challs
from .models import Settings


# Create your views here.
def make_chall(request):
    if request.method == "POST":
        new_chall = Challs(name="",active=True,static_value=False,points=1000,solves=0,category="",task="",flags="",files="")
        file_name = ""
        if request.POST.get('cfile') != "":
            uploaded_file = request.FILES['cfile']
            if uploaded_file:
                fs = FileSystemStorage()
                file_name = fs.save(uploaded_file.name, uploaded_file)

        c = request.POST.dict()

        keys={"cactive", "cstatic", "ccasesens"}
        for key in keys:
            try:
                if c[key]:
                    c[key] = True
                else:
                    c[key] = False
            except:
                c[key] = False

        c["cfile"] = file_name
        new_chall = Challs(name=c["cname"],active=c["cactive"],static_value=c["cstatic"],points=c["cstatic-value"],solves=0,category=c["ccat"].upper(),task=c["ctext"],flags=c["cflag"],files=c["cfile"],time_created=c["ctime_created"])
        new_chall.save()

    return render(request, 'make-chall.html')

def edit_chall(request):
    d = Challs.objects.all()

    if request.method == "GET":
        editing = ""
        chall_to_edit = request.GET.get('chall_to_edit')
        if chall_to_edit:
            editing = Challs.objects.get(name=chall_to_edit)
    

    if request.method == "POST":
        editing_id = request.POST.get('cid')
        editing = Challs.objects.get(id=editing_id)
        
        editing_dict = request.POST.dict()

        keys={"cactive", "cstatic", "ccasesens"}
        for key in keys:
            try:
                if editing_dict[key]:
                    editing_dict[key] = True
                else:
                    editing_dict[key] = False
            except:
                editing_dict[key] = False
        
        #editing_dict["cfile"] = file_name

        editing.name            = editing_dict["cname"]
        editing.active          = editing_dict["cactive"]
        editing.static_value    = editing_dict["cstatic"]
        editing.points          = editing_dict["cstatic-value"]
        editing.category        = editing_dict["ccat"].upper()
        editing.task            = editing_dict["ctext"]
        editing.flags           = editing_dict["cflag"]
        editing.time_created    = editing_dict["ctime_created"]
        editing.save(update_fields=['name', 'active', 'static_value', 'points', 'category', 'task', 'flags', 'time_created'])
    
    
    challs_to_edit = {
            "challs": d,
            "editing": editing,
        }
    
    return render(request, 'edit-chall.html', challs_to_edit)



def admin_panel(request):
    chall_count = Challs.objects.all().count()
    active_challs = Challs.objects.filter(active=True).count()

    stats = {
        "count": chall_count,
        "active": active_challs,
    }
    return render(request, 'admin-panel.html', stats)

def admin_settings(request):

    current_settings = Settings.objects.get(id=1)

    if request.method == "POST":
        input = request.POST.dict()
        keys={"ctf_active"}
        for key in keys:
            try:
                if input[key]:
                    input[key] = True
                else:
                    input[key] = False
            except:
                input[key] = False
        current_settings.ctf_name           = input['ctf_name']
        current_settings.ctf_active         = input['ctf_active']
        current_settings.save(update_fields=['ctf_name', 'ctf_active'])
        
    current = {
        "settings": current_settings,
    }
    return render(request, 'settings.html', current)



def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
    return render(request, 'upload.html')




def admin_setup(request):
    if request.method == "POST":
        input = request.POST.dict()
        print(input)
        keys={"ctf_active"}
        for key in keys:
            try:
                if input[key]:
                    input[key] = True
                else:
                    input[key] = False
            except:
                input[key] = False

        settings = Settings(ctf_name=input['ctf_name'], ctf_active=input['ctf_active'])
        settings.save()
        return HttpResponse("<h1>It Works</h1>")
    else:
        return render(request, 'setup.html')
