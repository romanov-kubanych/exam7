from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.models import Poll, Answer, Choice


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        context = {
            'poll': poll
        }
        return render(request, 'answers/index.html', context)

    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choice = get_object_or_404(Choice, pk=request.POST.get('answer'))
        new_answer = Answer.objects.create(poll=poll, option=choice)
        return redirect('answer_success', pk=poll.id)


class AnswerSuccessView(TemplateView):
    template_name = 'answers/success.html'

    def get_context_data(self, **kwargs):
        kwargs['poll'] = get_object_or_404(Poll, pk=kwargs['pk'])
        return super().get_context_data(**kwargs)
