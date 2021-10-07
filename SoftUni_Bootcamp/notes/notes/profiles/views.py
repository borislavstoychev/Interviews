from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from notes.profiles.forms import ProfileForm
from notes.profiles.models import Profile


class CreateProfileView(generic.CreateView):
    template_name = 'home-no-profile.html'
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('home page')


class ProfileView(generic.ListView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profiles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object_list[0]
        return context


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile.delete()
    return redirect('home page')

