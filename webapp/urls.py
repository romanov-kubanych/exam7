from django.urls import path

from views import PollIndexView, PollDetailView, PollCreateView, PollUpdateView, PollDeleteView

urlpatterns = [
    path('', PollIndexView.as_view(), name="poll_index"),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/update', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete', PollDeleteView.as_view(), name='poll_delete')
]
