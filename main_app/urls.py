from django.urls import path
from .views import (
    AboutViewSet,
    FAQViewSet,
    ClientsViewSet,
    CommentsViewSet,
    ContactsViewSet,
    FooterViewSet,
    PostsViewSet,
    ServiceCategoriesViewSet,
    ServicesViewSet,
    OurServiceViewSet,
    ContactViewSet,
    PriceViewSet,
    PriceListViewSet,
    TeachersViewSet,
    WorkersViewSet,
)

urlpatterns = [

    path('about/', AboutViewSet.as_view({'get': 'list', 'post': 'create'}), name='about-list'),
    path('about/<int:pk>/', AboutViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='about-detail'),


    path('faqs/', FAQViewSet.as_view({'get': 'list', 'post': 'create'}), name='faq-list'),
    path('faqs/<int:pk>/', FAQViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='faq-detail'),


    path('our-clients/', ClientsViewSet.as_view({'get': 'list', 'post': 'create'}), name='our-clients-list'),
    path('our-clients/<int:pk>/', ClientsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='our-clients-detail'),


    path('comments/', CommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
    path('comments/<int:pk>/', CommentsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comments-detail'),


    path('contacts/', ContactsViewSet.as_view({'get': 'list', 'post': 'create'}), name='contacts-list'),
    path('contacts/<int:pk>/', ContactsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='contacts-detail'),


    path('footer/', FooterViewSet.as_view({'get': 'list', 'post': 'create'}), name='footer-list'),
    path('footer/<int:pk>/', FooterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='footer-detail'),


    path('posts/', PostsViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts-list'),
    path('posts/<int:pk>/', PostsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='posts-detail'),


    path('service-categories/', ServiceCategoriesViewSet.as_view({'get': 'list', 'post': 'create'}), name='service-categories-list'),
    path('service-categories/<int:pk>/', ServiceCategoriesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='service-categories-detail'),


    path('services/', ServicesViewSet.as_view({'get': 'list', 'post': 'create'}), name='services-list'),
    path('services/<int:pk>/', ServicesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='services-detail'),


    path('our-service/', OurServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='our-service-list'),
    path('our-service/<int:pk>/', OurServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='our-service-detail'),


    path('contact/', ContactViewSet.as_view({'get': 'list', 'post': 'create'}), name='contact-list'),
    path('contact/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='contact-detail'),


    path('pricing/', PriceViewSet.as_view({'get': 'list', 'post': 'create'}), name='pricing-list'),
    path('pricing/<int:pk>/', PriceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pricing-detail'),


    path('price-list/', PriceListViewSet.as_view({'get': 'list', 'post': 'create'}), name='price-list-list'),
    path('price-list/<int:pk>/', PriceListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='price-list-detail'),


    path('teachers/', TeachersViewSet.as_view({'get': 'list', 'post': 'create'}), name='teachers-list'),
    path('teachers/<int:pk>/', TeachersViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='teachers-detail'),


    path('workers/', WorkersViewSet.as_view({'get': 'list', 'post': 'create'}), name='coworkers-list'),
    path('workers/<int:pk>/', WorkersViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='coworkers-detail'),
]