from rest_framework import serializers
from unicodedata import category

from .models import (
    About, FAQ, Clients, Comments, Contacts, Footer,
    Posts, ServiceCategories, Services, OurService, Contact,
    Price, PriceList, Teachers, Workers
)

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'description']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['title', 'question', 'answer']


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['title']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['name', 'profession', 'text']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    contact = ContactsSerializer(read_only=True)

    class Meta:
        model = Footer
        fields = ['contact_id', 'title', 'contact']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'description']


class ServiceCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategories
        fields = ['name']


class ServicesSerializer(serializers.ModelSerializer):
    category = ServiceCategoriesSerializer()

    class Meta:
        model = Services
        fields = ['name', 'description', 'detail_info', 'read_link', 'category']


class OurServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategoriesSerializer(read_only=True)

    class Meta:
        model = OurService
        fields = ['title', 'description', 'category']


class ContactSerializer(serializers.ModelSerializer):
    category = ServiceCategoriesSerializer()

    class Meta:
        model = Contact
        fields = ['comments', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category_instance = ServiceCategories.objects.create(**category_data)
        contact_instance = Contact.objects.create(category=category_instance, **validated_data)
        return contact_instance
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['price', 'description', 'order', 'sub_description']


class PriceListSerializer(serializers.ModelSerializer):
    price = PriceSerializer(many=True)

    class Meta:
        model = PriceList
        fields = ['title', 'description', 'pricing']


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['name', 'profession']


class WorkersSerializer(serializers.ModelSerializer):
    teacher_id = serializers.IntegerField(write_only=True)
    teacher = TeachersSerializer(read_only=True)

    class Meta:
        model = Workers
        fields = ['title', 'teacher_id', 'teacher']

    def create(self, validated_data):
        teacher_id = validated_data.pop('teacher_id')
        worker = Workers.objects.create(teacher_id=teacher_id,
                                            **validated_data)
        return worker

class TranslateAboutSerializer(AboutSerializer):
    class Meta(AboutSerializer.Meta):
        fields = [f"{field}_uz" for field in AboutSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in AboutSerializer.Meta.fields] + \
                 [f"{field}_en" for field in AboutSerializer.Meta.fields]


class TranslateFAQSerializer(FAQSerializer):
    class Meta(FAQSerializer.Meta):
        fields = [f"{field}_uz" for field in FAQSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in FAQSerializer.Meta.fields] + \
                 [f"{field}_en" for field in FAQSerializer.Meta.fields]


class TranslateOurClientsSerializer(ClientsSerializer):
    class Meta(ClientsSerializer.Meta):
        fields = [f"{field}_uz" for field in ClientsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ClientsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ClientsSerializer.Meta.fields]


class TranslateCommentsSerializer(CommentsSerializer):
    class Meta(CommentsSerializer.Meta):
        fields = [f"{field}_uz" for field in CommentsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in CommentsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in CommentsSerializer.Meta.fields]


class TranslateContactsSerializer(ContactsSerializer):
    class Meta(ContactsSerializer.Meta):
        fields = [f"{field}_uz" for field in ContactsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ContactsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ContactsSerializer.Meta.fields]


class TranslateFooterSerializer(FooterSerializer):
    class Meta(FooterSerializer.Meta):
        fields = [f"{field}_uz" for field in FooterSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in FooterSerializer.Meta.fields] + \
                 [f"{field}_en" for field in FooterSerializer.Meta.fields]


class TranslatePostsSerializer(PostsSerializer):
    class Meta(PostsSerializer.Meta):
        fields = [f"{field}_uz" for field in PostsSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in PostsSerializer.Meta.fields] + \
                 [f"{field}_en" for field in PostsSerializer.Meta.fields]


class TranslateServiceCategoriesSerializer(ServiceCategoriesSerializer):
    class Meta(ServiceCategoriesSerializer.Meta):
        fields = [f"{field}_uz" for field in ServiceCategoriesSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ServiceCategoriesSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ServiceCategoriesSerializer.Meta.fields]


class TranslateServicesSerializer(ServicesSerializer):
    class Meta(ServicesSerializer.Meta):
        fields = [f"{field}_uz" for field in ServicesSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ServicesSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ServicesSerializer.Meta.fields]


class TranslateOurServiceSerializer(OurServiceSerializer):
    class Meta(OurServiceSerializer.Meta):
        fields = [f"{field}_uz" for field in OurServiceSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in OurServiceSerializer.Meta.fields] + \
                 [f"{field}_en" for field in OurServiceSerializer.Meta.fields]


class TranslateContactSerializer(ContactSerializer):
    class Meta(ContactSerializer.Meta):
        fields = [f"{field}_uz" for field in ContactSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in ContactSerializer.Meta.fields] + \
                 [f"{field}_en" for field in ContactSerializer.Meta.fields]


class TranslatePricingSerializer(PriceSerializer):
    class Meta(PriceSerializer.Meta):
        fields = [f"{field}_uz" for field in PriceSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in PriceSerializer.Meta.fields] + \
                 [f"{field}_en" for field in PriceSerializer.Meta.fields]


class TranslatePriceListSerializer(PriceListSerializer):
    class Meta(PriceListSerializer.Meta):
        fields = [f"{field}_uz" for field in PriceListSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in PriceListSerializer.Meta.fields] + \
                 [f"{field}_en" for field in PriceListSerializer.Meta.fields]


class TranslateTeachersSerializer(TeachersSerializer):
    class Meta(TeachersSerializer.Meta):
        fields = [f"{field}_uz" for field in TeachersSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in TeachersSerializer.Meta.fields] + \
                 [f"{field}_en" for field in TeachersSerializer.Meta.fields]


class TranslateCoworkersSerializer(WorkersSerializer):
    class Meta(WorkersSerializer.Meta):
        fields = [f"{field}_uz" for field in WorkersSerializer.Meta.fields] + \
                 [f"{field}_ru" for field in WorkersSerializer.Meta.fields] + \
                 [f"{field}_en" for field in WorkersSerializer.Meta.fields]