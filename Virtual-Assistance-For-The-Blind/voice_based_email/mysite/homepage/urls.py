from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    path(r'', views.login_view, name="login"),
    path(r'^compose/$', views.compose_view, name="compose"),
    path(r'^inbox/$', views.inbox_view, name="inbox"),
    path(r'^sent/$', views.sent_view, name="sent"),
    path(r'^trash/$', views.trash_view, name="trash"),
    path(r'^options/$', views.options_view, name="options"),
    path(r'^starred/$', views.starred_view, name="starred")

]
