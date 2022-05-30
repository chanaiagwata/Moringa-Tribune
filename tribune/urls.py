from django.conf.urls import url,include



from django.contrib import admin
from django.contrib.auth import views

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'tribune.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('news.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),  #Django authentication***************************
    url(r'^logout/$', views.logout, {"next_page": '/'}),
   

    
    
]