from pathlib import Path
from django.core.files import File as DjangoFile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.pdf.canvas.color.color import HexColor

from decimal import Decimal

from .models import infoCVModel
from .forms import infoCVForm

def mainPage(request):
    return render(request, 'constructCVapp/mainPage.html')


def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'constructCVapp/signUpUser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('currentUser')
            except IntegrityError:
                return render(
                    request,
                    'constructCVapp/signUpUser.html',
                    {'form': UserCreationForm(), 'error': 'This name is already taken. Try another.'}
                )
        else:
            return render(
                request,
                'constructCVapp/signUpUser.html',
                {'form': UserCreationForm(), 'error': 'Passwords doesnt match'}
            )


def logInUser(request):
    if request.method == 'GET':
        return render(request, 'constructCVapp/logInUser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(
                request,
                'constructCVapp/logInUser.html',
                {'form': AuthenticationForm(), 'error': 'Username and password didnt match'}
            )
        else:
            login(request, user)
            return redirect('currentUser')


def logOutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('mainPage')



def createCV(request):
    if request.method == 'GET':
        return render(request, 'constructCVapp/createCV.html', {'form': infoCVForm()})
    else:
        form = infoCVForm(request.POST, request.FILES)
        if form.is_valid():
            firstName = form.cleaned_data.get('firstName')
            secondName = form.cleaned_data.get('secondName')

        pdf = Document()
        page = Page()
        pdf.add_page(page)
        r: Rectangle = Rectangle(
            Decimal(400),
            Decimal(848 - 84 - 100),
            Decimal(125),
            Decimal(150),
        )
        page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))
        Paragraph(firstName + ' ' + secondName, horizontal_alignment=Alignment.CENTERED).layout(page, r)

        with open(Path(f'constructCVapp/static/constructCVapp/{firstName}{secondName}CV.pdf'), 'wb') as new_pdf:
            PDF.dumps(new_pdf, pdf)
        CV = DjangoFile(open(Path(f'constructCVapp/static/constructCVapp/{firstName}{secondName}CV.pdf'), mode='rb'))
        data = infoCVModel(
            firstName=firstName,
            secondName=secondName,
            fileCV=CV,
        )
        data.user = request.user
        data.save()

        return redirect('currentUser')


def currentUser(request):
    files = infoCVModel.objects.filter(user=request.user)
    return render(request, 'constructCVapp/currentUser.html', {'files': files})
