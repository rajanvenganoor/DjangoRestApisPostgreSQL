from django.conf.urls import url
from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url ( r'^api/tutorials$', views.tutorial_list ),
    url ( r'^api/homeheads$', views.homehead_list ),
    url ( r'^api/children$', views.children_list ),
    url ( r'^api/transactions$', views.transaction_list ),
    url ( r'^api/expheads$', views.exphead_list ),
    url ( r'^api/expdetails$', views.expdetails_list ),
    url ( r'^api/event$', views.event_list ),
    url ( r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail ),
    url ( r'^api/homeheads/(?P<pk>[0-9]+)$', views.homehead_detail ),
    url ( r'^api/children/(?P<pk>[0-9]+)$', views.children_detail ),
    url ( r'^api/transactions/(?P<pk>[0-9]+)$', views.transaction_detail ),
    url ( r'^api/expheads/(?P<pk>[0-9]+)$', views.exphead_detail ),
    url ( r'^api/expdetails/(?P<pk>[0-9]+)$', views.expdetails_detail ),
    url ( r'^api/event/(?P<pk>[0-9]+)$', views.event_detail ),
    url ( r'^api/tutorials/published$', views.tutorial_list_published ),
    url ( r'^api/homeheads/published$', views.homehead_list_published ),
    url ( r'^api/cildren/published$', views.children_list_published ),
    url ( r'^api/transactions/published$', views.transaction_list_published ),
    url ( r'^api/expheads/published$', views.exphead_list_published ),
    url ( r'^api/expdetails/published$', views.expdetails_list_published ),
    url ( r'^api/event/published$', views.event_list_published )

]
'''
from django.conf.urls import url
from DjangoRestApisPostgreSQL.tutorials import views
#from django.urls import reverse
urlpatterns = [
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),

    url(r'^api/children$', views.children_list),
    url(r'^api/children/(?P<pk>[0-9]+)$', views.children_detail),
    url(r'^api/children/published$', views.children_list_published),

    url ( r'^api/homeheads$', views.homehead_list ),
    url ( r'^api/homeheads/(?P<pk>[0-9]+)$', views.homehead_detail ),
    url ( r'^api/homeheads/published$', views.homehead_list_published )

]
'''
