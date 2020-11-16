from django.shortcuts import render, HttpResponse
from blog.models import Blog
# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request, 'bloghome.html',context)

def contact(request):
    if request.method =='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        instance=contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()

    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')

def blogpost(request, slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
     
    return render(request, 'blogpost.html', context)

