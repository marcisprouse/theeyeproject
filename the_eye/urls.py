from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name='the_eye'


urlpatterns = [
    #path('', TemplateView.as_view(template_name="the_eye/index.html"), name='home'),
    path('', login_required(TemplateView.as_view(template_name="the_eye/index.html"), login_url='/accounts/login/?next=/accounts/'), name='home'),
]

handler404="the_eye.views.handle_not_found"
