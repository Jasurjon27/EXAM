from rest_framework import viewsets
from .models import (
    About, FAQ, Clients, Comments, Contacts, Footer,
    Posts, ServiceCategories, Services, OurService, Contact,
    Price, PriceList, Teachers, Workers
)
from .serializer import (
    AboutSerializer, FAQSerializer, ClientsSerializer, CommentsSerializer, ContactsSerializer,
    FooterSerializer, PostsSerializer, ServiceCategoriesSerializer, ServicesSerializer,
    OurServiceSerializer, ContactSerializer, PriceSerializer, PriceListSerializer,
    TeachersSerializer, WorkersSerializer
)



class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer



class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer



class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer



class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer



class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer



class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer



class ServiceCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategories.objects.all()
    serializer_class = ServiceCategoriesSerializer



class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer



class OurServiceViewSet(viewsets.ModelViewSet):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer



class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer



class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer



class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
