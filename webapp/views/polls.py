from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Poll


class PollIndexView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    ordering = ('-created_at')
    paginate_by = 5
    paginate_orphans = 0
