import os
from django.conf import settings
from django.utils import translation


# myapp/context_processors.py
def web_name(request):
    return {
        'baseurl': 'http://127.0.0.1:8000/',
        'web_name': 'IDPMI - From Ideas to Impact',
        'webname': 'IDPMI',
        'web_title': 'IDPMI - Ikatan Dosen dan Pasar Modal Indonesia',
        'address': 'Makassar',
        'telp': '0877 7579 5886',
        'fax': '(0411) 889464',
        'website': 'http://idpmi.id',
        'email': 'idpmindonesia@gmail.com',
        'instagram': '@idpmindonesia',
        'created_by': 'hermantoXYZ',
    }

def versioned_static(request):
    """Context processor untuk versioning static files"""
    import time
    return {
        'STATIC_VERSION': int(time.time())
    }