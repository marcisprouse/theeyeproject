from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

app_name='the_eye'


urlpatterns = [
    #path('', TemplateView.as_view(template_name="the_eye/index.html"), name='home'),
    path('', login_required(TemplateView.as_view(template_name="the_eye/index.html"), login_url='/accounts/login/?next=/accounts/'), name='home'),
    path('sessions', login_required(views.SessionListView.as_view(), login_url='/accounts/login/?next=/accounts/'),  name='sessions'),
    path('sessions/<int:pk>', login_required(views.SessionDetailView.as_view(), login_url='/accounts/login/?next=/accounts/'),  name='session_details'),
]

handler404="the_eye.views.handle_not_found"
