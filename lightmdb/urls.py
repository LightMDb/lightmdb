"""
lightmdb URL Configuration.
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from web import views

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
    url(r'^$', views.index, name='index'),
)
