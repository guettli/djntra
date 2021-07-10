import uuid

from django.db import models


class Thing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024, blank=True, default='')
    text = models.TextField(blank=True)


class RelationType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024, blank=True, default='')
    text = models.TextField(blank=True)


class Relation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, related_name='relations')
    other = models.ForeignKey(Thing, on_delete=models.CASCADE, related_name='reverse_relations')
    type = models.ForeignKey(RelationType, on_delete=models.CASCADE)
