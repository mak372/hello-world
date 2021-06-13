from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Internshipform,Volunteerform


def careers(response):
	return render(response,"careers/careers.html", {})

def internform(request):
	if request.method == 'POST':
		form = Internshipform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('careers')
		else:
			form = Internshipform()
			context = {'form':form}
			return render(request,"careers/internship.html",context)
	else:
		form = Internshipform()
		context = {'form':form}
		return render(request,"careers/internship.html",context)

def volunteerform(request):
	if request.method == 'POST':
		form = Volunteerform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('careers')
		else:
			form = Volunteerform()
			context = {'form':form}
			return render(request,"careers/internship.html",context)
	else:
		form = Volunteerform()
		context = {'form':form}
		return render(request,"careers/internship.html",context)


