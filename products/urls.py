from django.conf.urls import url
from .views import (
    ProductListView,
    ProductDetailSlugView
                            )

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^products_fn/(?P<pk>\d+)/$', product_detail_view),
    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
]
