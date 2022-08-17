from pathlib import Path
from decimal import Decimal
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.pdf.canvas.color.color import HexColor


def constructor_cv(
        emailAdress, phoneNumber, gitHubLink, socialContacts,
        firstName, secondName, wantedJobTitle,
        educationSubscribe, workExperience
):
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
    # CV = DjangoFile(open(Path(f'constructCVapp/static/constructCVapp/{firstName}{secondName}CV.pdf'), mode='rb'))

