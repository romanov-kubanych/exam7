from django.urls import path

from views import PollIndexView

urlpatterns = [
    path('', PollIndexView.as_view(), name="poll_index"),
]