from django.views.generic import TemplateView

from core.forms import MessageForm


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({
            'form': MessageForm()
        })
        return context
