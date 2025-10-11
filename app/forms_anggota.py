from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import UserAnggota
from django.contrib.auth.models import User

class formProfile(forms.ModelForm):
    class Meta:
        model = UserAnggota
        fields = [   
            'telp',
            'gender',
            'photo',
            'tempat_lahir',
            'tgl_lahir',
            'bidang_keahlian',
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
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control'}),
            'tgl_lahir': forms.DateInput(attrs={'class': 'form-control'}),
            'bidang_keahlian': forms.TextInput(attrs={'class': 'form-control'}),
        }

class formResetPasswordAnggota(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password Saat Ini'
        }),
        label='Password Saat Ini'
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password Baru'
        }),
        label='Password Baru',
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Konfirmasi Password Baru'
        }),
        label='Konfirmasi Password Baru'
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("Password baru dan konfirmasi password tidak cocok!")
        
        return cleaned_data