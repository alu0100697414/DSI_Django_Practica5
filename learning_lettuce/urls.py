from django.conf.urls import patterns, include, url
 
from blog.views import quick_test
 
urlpatterns = patterns('',
    url(r'^quick-test/$', quick_test),
)
