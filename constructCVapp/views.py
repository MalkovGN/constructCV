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
            emailAdress = form.cleaned_data.get('emailAdress')
            phoneNumber = form.cleaned_data.get('phoneNumber')
            gitHubLink = form.cleaned_data.get('gitHubLink')
            socialContacts = form.cleaned_data.get('socialContacts')
            wantedJobTitle = form.cleaned_data.get('wantedJobTitle')
            educationSubscribe = form.cleaned_data.get('educationSubscribe')
            workExperience = form.cleaned_data.get('workExperience')
        else:
            return render(
                request,
                'constructCVapp/createCV.html',
                {'form': infoCVForm(), 'error': 'Please, enter a correct phone number!'}
            )
        # Checking emptiness of fields
        if emailAdress is None:
            emailAdress = ''
        if phoneNumber is None:
            phoneNumber = ''
        if gitHubLink is None:
            gitHubLink = ''
        if socialContacts is None:
            socialContacts = ''
        if educationSubscribe is None:
            educationSubscribe = ''
        if workExperience is None:
            workExperience = ''

        pdf = Document()
        page = Page()
        pdf.add_page(page)

        r: Rectangle = Rectangle(
            Decimal(450),
            Decimal(660),
            Decimal(125),
            Decimal(160),
        )
        page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))
        Paragraph(
            str(emailAdress) + '\n' + str(phoneNumber) + '\n' + str(gitHubLink) + '\n' + str(socialContacts),
            horizontal_alignment=Alignment.CENTERED
        ).layout(page, r)

        r: Rectangle = Rectangle(
            Decimal(50),
            Decimal(785),
            Decimal(340),
            Decimal(40),
        )
        Paragraph(
            firstName + ' ' + secondName,
            font_size=Decimal(22),
            vertical_alignment=Alignment.MIDDLE).layout(page, r)
        page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))

        r: Rectangle = Rectangle(
            Decimal(50),
            Decimal(770),
            Decimal(340),
            Decimal(15),
        )
        Paragraph(wantedJobTitle, font_size=Decimal(10), horizontal_alignment=Alignment.LEFT).layout(page, r)
        page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))

        if educationSubscribe != '':
            r: Rectangle = Rectangle(
                Decimal(50),
                Decimal(740),
                Decimal(400),
                Decimal(25),
            )
            Paragraph('Education', font_size=Decimal(14), horizontal_alignment=Alignment.CENTERED).layout(page, r)
            page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))

            r: Rectangle = Rectangle(
                Decimal(50),
                Decimal(660),
                Decimal(400),
                Decimal(75),
            )
            Paragraph(educationSubscribe, font_size=Decimal(10), text_alignment=Alignment.JUSTIFIED).layout(page, r)
            page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))
            if workExperience != '':
                r: Rectangle = Rectangle(
                    Decimal(50),
                    Decimal(630),
                    Decimal(400),
                    Decimal(25),
                )
                Paragraph(
                    'Work experience',
                    font_size=Decimal(14),
                    horizontal_alignment=Alignment.CENTERED
                ).layout(page, r)
                page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))

                r: Rectangle = Rectangle(
                    Decimal(50),
                    Decimal(480),
                    Decimal(400),
                    Decimal(150),
                )
                Paragraph(workExperience, font_size=Decimal(10), text_alignment=Alignment.JUSTIFIED).layout(page, r)
                page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))
        else:
            r: Rectangle = Rectangle(
                Decimal(50),
                Decimal(740),
                Decimal(400),
                Decimal(25),
            )
            Paragraph(
                'Work experience',
                font_size=Decimal(14),
                horizontal_alignment=Alignment.CENTERED
            ).layout(page, r)
            page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))

            r: Rectangle = Rectangle(
                Decimal(50),
                Decimal(590),
                Decimal(400),
                Decimal(150),
            )
            Paragraph(workExperience, font_size=Decimal(10), text_alignment=Alignment.JUSTIFIED).layout(page, r)
            page.add_annotation(SquareAnnotation(r, stroke_color=HexColor('#ffffff')))

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
