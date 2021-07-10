# Generated by Django 3.2.5 on 2021-07-10 04:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=1024)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=1024)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reverse_relations', to='djntra.thing')),
                ('thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='djntra.thing')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djntra.relationtype')),
            ],
        ),
    ]
