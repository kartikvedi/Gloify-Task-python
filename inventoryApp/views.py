from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from .models import Books, BooksForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
@csrf_exempt
def bookslist(request):
    """
    passdata-> Lists of all books(info) exist in inventory db.
    newbooks-> Lists of all books(info) get by search query.
    idlist-> Lists of all books's Google Api id, exists in inventory db.
    """
    i=0
    passdata =[0]*Books.objects.all().count()
    for book in Books.objects.all():
        passdata[i] = {'title':book.title,'id':book.bookid,'copies':book.copies,'link':book.readlink}
        i+=1

    if request.GET.get('search'):
        # Fetch and show books for given query and also indicate weather it is exist in inventory or not.
        query = request.GET.get('mytextbox')
        print(query)
        r= requests.get(url="https://www.googleapis.com/books/v1/volumes?q="+ query)
        jsonlist = r.json()
        i=0
        newbooks=[0]*len(jsonlist['items'])
        idlist=[0]*len(passdata)
        for book in jsonlist['items']:
            newbooks[i] = {'title':book['volumeInfo']['title'],'id':book['id'],'link':book['volumeInfo']['infoLink']}
            i+=1
        for i in range(len(passdata)):
            idlist[i] = passdata[i]['id']
        return render(request, 'booklist.html', {'passdata':passdata,'newbooks':newbooks,'idlist':idlist})

    if request.GET.get('Add'):
        # Add new Book to the inventory.
        q=Books(title=request.GET.get('booktitle'),readlink=request.GET.get('booklink'),copies=1,bookid=request.GET.get('bookid'))
        q.save()
        return redirect('/')

    if request.GET.get('AddCopy'):
        #Update copies on adding existing book.
        book = Books.objects.get(bookid=request.GET.get('bookid'))
        copies = book.copies
        copies+=1
        book.copies = copies
        book.save()
        return redirect('/')

    if request.GET.get('Delete'):
        #Remove a book copy from the inventory.
        book = Books.objects.get(bookid=request.GET.get('bookid'))
        if book.copies > 0:
            book.copies = book.copies - 1
            book.save()
        return redirect('/')

    return render(request, 'booklist.html',{'passdata':passdata})







# Create your views here.
