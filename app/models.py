import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
User.add_to_class("__str__", lambda self: f"{self.username} - {self.first_name}")

# MODEL USER ANGGOTA DAN ADMIN

def rename_photo_anggota(instance, filename):
    ext = filename.split('.')[-1]
    nip_username = instance.id_anggota.username
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{nip_username}_{timestamp}.{ext}"
    return os.path.join('img_profile/dsn/', new_filename)

class UserAnggota(models.Model):
    id_anggota = models.OneToOneField(User, on_delete=models.CASCADE, to_field="username", primary_key=True)
    telp = models.CharField(max_length=15, verbose_name="Nomor Telepon")
    gender = models.CharField(
        max_length=15,
        choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')],
    )
    tempat_lahir = models.CharField(max_length=50, null=True, blank=True)
    tgl_lahir = models.DateField(null=True, blank=True, verbose_name="Tanggal Lahir")
    nidn = models.CharField(max_length=20, null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)
    bidang_keahlian = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to=rename_photo_anggota, null=True, blank=True) # Tambahkan null=True, blank=True agar tidak wajib

    class Meta:
        verbose_name_plural = "User Anggota" # Penamaan yang lebih baik di admin

    def save(self, *args, **kwargs):
        if self.pk: # Periksa apakah ini objek yang sudah ada (bukan baru)
            try:
                old_instance = UserAnggota.objects.get(pk=self.pk)
                # Periksa jika ada foto lama dan foto baru berbeda
                if old_instance.photo and old_instance.photo != self.photo:
                    old_photo_path = os.path.join(settings.MEDIA_ROOT, old_instance.photo.name)
                    if os.path.isfile(old_photo_path):
                        os.remove(old_photo_path)
            except UserAnggota.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        user_obj = self.id_anggota # self.nip adalah objek User
        nama_lengkap = f"{user_obj.first_name} {user_obj.last_name}".strip()
        if not nama_lengkap:
            nama_lengkap = user_obj.username # Fallback jika nama depan/belakang kosong
        return f"{nama_lengkap} ({self.id_anggota.username})" # NIP adalah username


def rename_photo_admin(instance, filename):
    ext = filename.split('.')[-1]
    admin_username = instance.username.username
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{admin_username}_{timestamp}.{ext}"
    return os.path.join('img_profile/admin/', new_filename)


class UserAdmin(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, to_field="username", primary_key=True, verbose_name="Username Admin")
    telp = models.CharField(max_length=15, verbose_name="Nomor Telepon")
    gender = models.CharField(
        max_length=15,
        choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')],
    )
    photo = models.ImageField(upload_to=rename_photo_admin, null=True, blank=True) # Tambahkan null=True, blank=True agar tidak wajib

    class Meta:
        verbose_name_plural = "Admin User" # Pen

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = UserAdmin.objects.get(pk=self.pk)
                if old_instance.photo and old_instance.photo != self.photo:
                    old_photo_path = os.path.join(settings.MEDIA_ROOT, old_instance.photo.name)
                    if os.path.isfile(old_photo_path):
                        os.remove(old_photo_path)
            except UserAdmin.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        user_obj = self.username # self.username adalah objek User
        nama_lengkap = f"{user_obj.first_name} {user_obj.last_name}".strip()
        if not nama_lengkap:
            nama_lengkap = user_obj.username
        return f"{nama_lengkap} ({self.username.username})"

# MODEL CATEGORY DAN ARTICLE UNTUK BLOG/NEWS

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

def rename_featured_image(instance, filename):
    ext = filename.split('.')[-1]
    title_slug = slugify(instance.title)
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{title_slug}_{timestamp}.{ext}"
    return os.path.join('articles/featured_images/', new_filename)

class Article(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to=rename_featured_image, blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pages')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
