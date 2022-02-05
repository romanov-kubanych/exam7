from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choises/create.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll_id = poll.id
        choice.save()
        return redirect('poll_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choises/update.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll_id})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choises/delete.html'

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll_id})

