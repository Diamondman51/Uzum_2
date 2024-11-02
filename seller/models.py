from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class SellerManager(BaseUserManager):
    def create_user(self, company=None, email=None, password=None, phone=None, address=None, longitude=None,
                    latitude=None, landmark=None):
        user = self.model(
            email=self.normalize_email(email),
            company_name=company,
            phone=phone,
            address=address,
            longitude=longitude,
            latitude=latitude,
            landmark=landmark
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, company_name, email, phone, password):
        user = self.create_user(
            company=company_name,
            email=email,
            phone=phone,
            password=password
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Seller(AbstractBaseUser, PermissionsMixin):
    company_name = models.CharField(max_length=300, null=True, blank=False, unique=True)
    email = models.EmailField(unique=True, null=True, blank=False)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=False)
    longitude = models.FloatField(max_length=200, null=True, blank=False)
    latitude = models.FloatField(max_length=200, null=True, blank=False)
    landmark = models.CharField(max_length=300, null=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name', 'phone']

    objects = SellerManager()

    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return f'{self.company_name} {self.email}'

    class Meta:
        verbose_name_plural = 'Sellers'


class QuantityOfProduct(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Property(models.Model):
    quantity_id = models.ForeignKey(QuantityOfProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Properties'


class Product(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)
