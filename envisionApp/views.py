from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Message, Staff, JobData, BeforAfterImg, ServiceDetail, BlogDetailsView, ServiceCategory, AdditionalImage
# Create your views here.
def home(request):
    img = BeforAfterImg.objects.all()
    service = ServiceDetail.objects.all()
    servieCategory = ServiceCategory.objects.all()
    blog = BlogDetailsView.objects.all()
    staff = Staff.objects.all()
    additionlimage = AdditionalImage.objects.all()

    return render(request, 'index.html', { 'ba_img': img , 'service': service, 'blog': blog, 'staff': staff, "additionlimage":additionlimage, 'servieCategory':servieCategory })


def get_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")


        
        Message.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )

        print("Your message request has been submitted!")
        print(f"name: {name}, email: {email}, message: {message}")

        return redirect("/")

    else:
        print("Your message request has not been submitted!")
        return render(request, "contact.html")


def getJobData(request):
    if request.method == "POST":
        email = request.POST.get("email")
        service = request.POST.get("service")
        fileformat = request.POST.get("fileFormat")
        background = request.POST.get("background")
        message = request.POST.get("message")
        file = request.FILES.get("file")  
        check = request.POST.get("check")

        is_checked = True if check == "on" else False


        JobData.objects.create(
            email=email,
            service=service,
            fileformat=fileformat,
            background=background,
            message=message,
            file=file,
            checked=is_checked
        )

        print("Your request has been submitted!")
        print(f"email: {email}, service: {service}, fileformat: {fileformat}, background: {background}, message: {message}, checked: {is_checked}")
        return redirect('/')

    else:
        print("Your request has not been submitted!")
        return render(request, "index.html")


def service_detail(request, slug):
    service = get_object_or_404(ServiceDetail, slug=slug)
    img = BeforAfterImg.objects.all()

    return render(request, 'service-details-view.html', {'service': service, "image": img})


def blog_cards(request):
    blog = BlogDetailsView.objects.all()
    return render(request, "blog-card.html", {'blog': blog})

def blogDetailsView(request, slug):
    blog = get_object_or_404(BlogDetailsView, slug=slug)
    all_blogs = BlogDetailsView.objects.all()

    return render(request, "blog-details-view.html", {'blog':blog, 'all_blogs':all_blogs})


def aboutpage(request):
    staff = Staff.objects.all()
    return render(request, 'about.html', {'staff':staff})

def contactPage(request):
    return render(request, 'contact.html')

def servicePage(request):
    # service = ServiceCategory.objects.all()
    service = ServiceDetail.objects.all()

    return render(request, 'service.html', {'service':service})











