# Generated by Django 3.1.7 on 2021-03-29 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_office_officer_subsriber_transferredsubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField()),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('address1', models.CharField(blank=True, max_length=150, null=True)),
                ('address2', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=150, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=150, null=True)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subsriber')),
            ],
        ),
    ]
