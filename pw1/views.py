from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def home(request):
	return render(request,'pw1/index.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"  
			body = {
			'name': form.cleaned_data['name'], 
			'email': form.cleaned_data['email'],
			'subject':form.cleaned_data['subject'],
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			try:
				send_mail(subject, message, 'pratikp676@gmail.com', ['pratikp676@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect("success")

	form = ContactForm()
	return render(request, "pw1/contact.html", {'form':form})


def success(request):
	return render(request,'pw1/success.html')