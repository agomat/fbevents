from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from mixins.CommonListsMinix import CommonListsMixin
from app.models import Topic
from app.models import Event


class TopicView(CommonListsMixin, ListView):
    model = Event
    context_object_name = "events"
    template_name = "app/sections/index.html"

    def get_queryset(self):
        active_topic = get_object_or_404(Topic, name=self.kwargs['term'])
        return Event.objects.filter(topic=active_topic)
