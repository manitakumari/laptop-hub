
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home', HomeView.as_view(), name='home'),
    url(r'^signup', SignupView.as_view(), name='signup'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^newItems', NewItemsView.as_view(), name='newItems'),
    url(r'^filetest', FiletestView.as_view(), name='filetest'),
    url(r'^product_details', ProductDetailsView.as_view(), name='product_details'),
    url(r'^payment', PaymentView.as_view(), name='payment'),
   ]

