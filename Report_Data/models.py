from django.db import models

# Create your models here.

class NagraDetails(models.Model):
    network_id=models.CharField(max_length=30, blank=True)
    network_name=models.CharField(max_length=30, blank=True)
    bouquet_id=models.CharField(max_length=30, blank=True)
    bouquet_name=models.CharField(max_length=30, blank=True)
    transport_id=models.CharField(max_length=30, blank=True)
    channel_name=models.CharField(max_length=30, blank=True)
    call_sign=models.CharField(max_length=30, blank=True)
    products=models.CharField(max_length=30, blank=True)
    frequency=models.CharField(max_length=30, blank=True)
    modulation=models.CharField(max_length=30, blank=True)
    transport_key=models.CharField(max_length=30, blank=True)
    service_key=models.CharField(max_length=30, blank=True)
    channel_number=models.CharField(max_length=30, blank=True)
    alternate_channel_number=models.CharField(max_length=30, blank=True)
    dvbsi_mpeg=models.CharField(max_length=30, blank=True)
    acref_int=models.CharField(max_length=30, blank=True)
    acref_hex=models.CharField(max_length=30, blank=True)
    original_network_id=models.CharField(max_length=30, blank=True)
    scrambling_algorithm=models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.network_id

    

