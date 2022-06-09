



from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'tribune.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'',include('news.urls')),
    path('logout/',auth_views.logout_then_login, name ='logout'),
    path(r'accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'^tinymce/', include('tinymce.urls')),
      
]

