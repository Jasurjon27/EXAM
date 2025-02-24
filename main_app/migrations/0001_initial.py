import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('title_en', models.CharField(max_length=212, null=True)),
                ('title_ru', models.CharField(max_length=212, null=True)),
                ('title_uz', models.CharField(max_length=212, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='about')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('name_en', models.CharField(max_length=212, null=True)),
                ('name_ru', models.CharField(max_length=212, null=True)),
                ('name_uz', models.CharField(max_length=212, null=True)),
                ('profession', models.CharField(max_length=212)),
                ('profession_en', models.CharField(max_length=212, null=True)),
                ('profession_ru', models.CharField(max_length=212, null=True)),
                ('profession_uz', models.CharField(max_length=212, null=True)),
                ('image', models.ImageField(upload_to='comments')),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_ru', models.TextField(null=True)),
                ('text_uz', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=212)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('title_en', models.CharField(max_length=212, null=True)),
                ('title_ru', models.CharField(max_length=212, null=True)),
                ('title_uz', models.CharField(max_length=212, null=True)),
                ('question', models.TextField()),
                ('question_en', models.TextField(null=True)),
                ('question_ru', models.TextField(null=True)),
                ('question_uz', models.TextField(null=True)),
                ('answer', models.TextField()),
                ('answer_en', models.TextField(null=True)),
                ('answer_ru', models.TextField(null=True)),
                ('answer_uz', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('title_en', models.CharField(max_length=212, null=True)),
                ('title_ru', models.CharField(max_length=212, null=True)),
                ('title_uz', models.CharField(max_length=212, null=True)),
                ('icon', models.ImageField(upload_to='our_clients')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('title_en', models.CharField(max_length=212, null=True)),
                ('title_ru', models.CharField(max_length=212, null=True)),
                ('title_uz', models.CharField(max_length=212, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='posts')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('sub_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('name_en', models.CharField(max_length=212, null=True)),
                ('name_ru', models.CharField(max_length=212, null=True)),
                ('name_uz', models.CharField(max_length=212, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('profession', models.CharField(max_length=212)),
                ('image', models.ImageField(upload_to='teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('icon', models.ImageField(upload_to='footer')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.contacts')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('pricing', models.ManyToManyField(to='main.pricing')),
            ],
        ),
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicecategories')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('phone', models.CharField(max_length=212)),
                ('comments', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicecategories')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('name_en', models.CharField(max_length=212, null=True)),
                ('name_ru', models.CharField(max_length=212, null=True)),
                ('name_uz', models.CharField(max_length=212, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('detail_info', models.TextField()),
                ('detail_info_en', models.TextField(null=True)),
                ('detail_info_ru', models.TextField(null=True)),
                ('detail_info_uz', models.TextField(null=True)),
                ('read_link', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicecategories')),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teachers')),
            ],
        ),
    ]