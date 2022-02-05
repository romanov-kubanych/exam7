from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PollForm
from webapp.models import Poll


class PollIndexView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    ordering = ('-created_at')
    paginate_by = 5
    paginate_orphans = 0


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/view.html'


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

