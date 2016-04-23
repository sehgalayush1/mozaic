from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
	url(r'^category/([\w-]+)/$', views.category, name='category'),
	url(r'^team/$', views.team, name='ourteam'),
	url(r'^contact_us/', views.contact_us, name='contact_us'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)