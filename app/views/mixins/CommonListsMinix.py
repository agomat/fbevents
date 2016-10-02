from django.views.generic.base import ContextMixin
from app.models import Topic
from app.models import Location


class CommonListsMixin(ContextMixin):

    def get_topics(self):
        return Topic.objects.all()

    def get_locations(self):
        return Location.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CommonListsMixin, self).get_context_data(**kwargs)
        context['topics'] = self.get_topics()
        context['locations'] = self.get_locations()
        return context