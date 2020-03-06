# Generated by Django 2.2.6 on 2020-03-06 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IndexSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IndexSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_count', models.IntegerField(default=0)),
                ('mycategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='indexcategory', to='index.IndexCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='index_images')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], max_length=10)),
                ('S', models.BooleanField(default=True)),
                ('M', models.BooleanField(default=True)),
                ('L', models.BooleanField(default=True)),
                ('XL', models.BooleanField(default=True)),
                ('XL2', models.BooleanField(default=True)),
                ('XL3', models.BooleanField(default=True)),
                ('XL4', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock', models.IntegerField()),
                ('rating', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='index_category', to='index.IndexCategory')),
                ('subcategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='index_subcategory', to='index.IndexSubCategory')),
            ],
        ),
    ]
