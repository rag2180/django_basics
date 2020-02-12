# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.get_query_set().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.get_query_set().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    queryset = Product.objects.all()  # get everything in the database
    template_name = "products/list.html"

    # def get_context_data(self, **kwargs):
    #     """
    #     We simply overrided this function to print context to understand what is passed to our html file
    #     Also we can add our own context if we want by this.
    #     :param kwargs:
    #     :return:
    #     """
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     # context["abc"] = "Hello"
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, "product/product_list_view.html", context)


class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Doesn't Exist")
        return instance


def product_detail_view(request, pk=None, *args, **kwargs):
    """
    This pk is coming from URL. see urls.py.
    :param request:
    :param pk:
    :return:
    """
    #instance = Product.objects.get(id=pk)  # id - autoincrememnt number id can be replaced with pk also
    #instance = get_object_or_404(Product, pk=pk)

    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     raise Http404("Product Doesn't Exist")
    # except:
    #     print("Unexpected Error")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product Doesn't Exist")
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Doesn't Exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
