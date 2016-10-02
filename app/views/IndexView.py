from django.views.generic import TemplateView
from mixins.CommonListsMinix import CommonListsMixin
from django.shortcuts import redirect


class IndexView(CommonListsMixin, TemplateView):
    template_name = "app/sections/index.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('q', ''):
            redirect('topic', term='bar')
            pass
        return super(IndexView, self).dispatch(request, *args, **kwargs)
