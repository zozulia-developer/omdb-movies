from django import forms

from movies.models import Movie


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'director', 'actors']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie title'
        })
        self.fields['year'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie year'
        })
        self.fields['director'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie director'
        })
        self.fields['actors'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie actors'
        })


class EditMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'director', 'actors']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie title'
        })
        self.fields['year'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie year'
        })
        self.fields['director'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie director'
        })
        self.fields['actors'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter movie actors'
        })
