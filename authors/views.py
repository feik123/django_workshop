
from django.views.generic import TemplateView

from FurryFunnies.utils import get_user_obj


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['author'] = get_user_obj()
        return context
