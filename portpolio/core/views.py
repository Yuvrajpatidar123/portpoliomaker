from django.shortcuts import render,HttpResponse
from . models import *
# Create your views here.
def index(request):
    about = About.objects.first()
    skill = Skill.objects.all()
    education = Education.objects.all()
    exprience = Experience.objects.all()
    port = Portpolio.objects.all()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request,'index.html',{'about':about,'skill':skill,'education':education,'exprience':exprience,'port':port,'service':service,"testimonial":testimonial})

# def contactus(request):

#     if request.method=="POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']

#         contact = Contact(name = name,email = email, subject = subject, message = message)
#         contact.save()
#         return render(request,'index.html')
#     else:
#         return render(request, 'index.html')
    