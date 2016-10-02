from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from mixins.CommonListsMinix import CommonListsMixin
from app.models import Event


class EventView(CommonListsMixin, DetailView):
    model = Event
    context_object_name = "event"
    template_name = "app/sections/event.html"

