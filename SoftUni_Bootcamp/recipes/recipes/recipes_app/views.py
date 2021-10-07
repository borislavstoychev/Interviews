from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from recipes.recipes_app.forms import RecipeForm
from recipes.recipes_app.models import Recipe


class HomeView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'recipes'
    model = Recipe


class CreateView(generic.CreateView):
    template_name = 'create.html'
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('home page')


class EditView(generic.UpdateView):
    template_name = 'edit.html'
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('home page')


class DeleteView(generic.DeleteView):
    template_name = 'delete.html'
    model = Recipe
    success_url = reverse_lazy('home page')
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context[self.context_object_name]
        form = RecipeForm(data=
                          {'title': recipe.title,
                           'image_url': recipe.image_url,
                           'description': recipe.description,
                           'ingredients': recipe.ingredients,
                           'time': recipe.time,
                           })
        for (_, field) in form.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


class DetailsView(generic.DetailView):
    template_name = 'details.html'
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context[self.context_object_name]
        ingredients = recipe.ingredients.split(", ")
        context['ingredients'] = ingredients

        return context

