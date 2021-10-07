from django import forms

from notes.note.models import Notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ('profile', )

