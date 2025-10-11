from django import forms
from django.utils import timezone
from .models import Page, Article, UserAnggota, UserAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
tgl_now = timezone.now()


class formProfile(forms.ModelForm):
    class Meta:
        model = UserAdmin
        fields = [    
            'telp',
            'gender',
            'photo',
        ]
        widgets = {
            'gender': forms.Select(
                choices=[
                    ('Laki-laki', 'Laki-laki'),
                    ('Perempuan', 'Perempuan'),
                ],
                attrs={'class': 'form-control'}
            ),
            'telp': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

        
class formUserEdit(forms.ModelForm):
    class Meta:
        model = UserAdmin
        fields = [
            'telp',
            'gender',
            'photo',
        ]
        widgets = {
            'gender': forms.Select(
                choices=[
                    ('Laki-laki', 'Laki-laki'),
                    ('Perempuan', 'Perempuan'),
                ],
                attrs={'class': 'form-control'}
            ),
            'telp': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }



class formPageEdit(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Page
        fields = ['title', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
        }


class formPageCreate(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Page
        fields = ['title', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title (Bahasa Indonesia)'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
        }

class formArticleCreate(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Article
        fields = ['title', 'created_at', 'slug', 'category', 'content', 'featured_image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title (English)'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class formArticleEdit(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Article
        fields = ['title', 'slug', 'category', 'content', 'featured_image', 'status','created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title (Bahasa Indonesia)'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

