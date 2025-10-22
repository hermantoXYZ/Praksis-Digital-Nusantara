import os
from django.conf import settings
from django.utils import translation


# myapp/context_processors.py
def web_name(request):
    return {
        'baseurl': 'http://127.0.0.1:8000/',
        'web_name': 'Praksis Digital Nusantara - From Ideas to Impact',
        'webname': 'PADINUSANTARA.CO.ID',
        'web_title': 'Praksis Digital Nusantara - Padinusantara.co.id',
        'address': 'Makassar',
        'telp': '0895 124 02404',
        'fax': '(0411) 889464',
        'website': 'http://padinusantara.co.id',
        'email': 'praksisdn@gmail.com',
        'instagram': '@padinusantara',
        'created_by': 'hermantoXYZ',
    }

def versioned_static(request):
    """Context processor untuk versioning static files"""
    import time
    return {
        'STATIC_VERSION': int(time.time())
    }