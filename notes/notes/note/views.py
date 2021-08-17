from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

# Create your views here.
from notes.note.forms import  NoteForm
from notes.note.models import Notes
from notes.profiles.models import Profile


class HomeView(generic.ListView):
    def get(self, request, *args, **kwargs):
        if Profile.objects.all().exists():
            return render(request, 'home-with-profile.html', {'notes': Notes.objects.all()})
        return redirect('create profile')


class CreateNoteView(generic.CreateView):
    template_name = 'note-create.html'
    model = Notes
    form_class = NoteForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        profile = Profile.objects.all().first()
        note = form.save(commit=False)
        note.profile = profile
        note.save()
        return super().form_valid(form)


class EditNoteView(generic.UpdateView):
    template_name = 'note-edit.html'
    model = Notes
    form_class = NoteForm
    success_url = reverse_lazy('home page')


class DeleteNoteView(generic.DeleteView):
    model = Notes
    template_name = 'note-delete.html'
    success_url = reverse_lazy('home page')
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = context[self.context_object_name]
        form = NoteForm(data={'title': note.title, 'content': note.content, 'image_url': note.image_url})
        for (_, field) in form.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class DetailNoteView(generic.DetailView):
    model = Notes
    template_name = 'note-details.html'
    context_object_name = 'note'




