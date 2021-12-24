from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('the_eye.urls')),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='graphql'),
]

admin.site.site_header = "The Eye Admin Panel"
admin.site.site_title = "The Eye Portal"
admin.site.index_title = "Welcome to The Eye Portal!"
