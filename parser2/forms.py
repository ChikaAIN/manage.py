from django import forms
from . import parser, models

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Game_kg', 'Game_kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        field =[
            'media_type'
        ]
    def parser_data(self):
        if self.data['media_type'] =="FILMS_KG":
            film_parser = parser.parser()
            for i in film_parser:
                models.ParserApp.objects.create(**i)