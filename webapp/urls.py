from django.urls import path

from views import PollIndexView, PollDetailView, PollCreateView

urlpatterns = [
    path('', PollIndexView.as_view(), name="poll_index"),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_create'),
]
