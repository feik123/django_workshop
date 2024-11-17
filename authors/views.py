from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import BaseFormView

from authors.forms import AuthorCreateForm
from authors.models import Author


class CreateAuthorPage(CreateView):
    model = Author
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dash')
    template_name = 'authors/create-author.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


