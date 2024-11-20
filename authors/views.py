from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from FurryFunnies.utils import get_user_obj
from authors.forms import AuthorCreateForm
from authors.models import Author


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dash')
    template_name = 'authors/create-author.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthorDetails(DetailView):
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()




# class AuthorDelete(DeleteView):
#     template_name = 'authors/delete-author.html'
#     success_url = reverse_lazy('index')

