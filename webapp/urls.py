from django.urls import path

from views import PollIndexView, PollDetailView, PollCreateView, PollUpdateView, PollDeleteView
from views.choises import ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView

urlpatterns = [
    path('', PollIndexView.as_view(), name="poll_index"),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/update', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete', PollDeleteView.as_view(), name='poll_delete'),
    path('poll/<int:pk>/choice/add/', ChoiceCreateView.as_view(), name='choice_create'),
    path('choice/<int:pk>/update/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete'),
]
