from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(region='KZ')
    photo = models.ImageField(upload_to="user_photos/%Y/%m/%d/")

    def __str__(self):
        return self.user.username + 'info'


class Image(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return 'photo' + str(self.id)


class Post(models.Model):
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + '_' + str(self.created_at)


class Comment(models.Model):
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + '_' + str(self.created_at)


class Like(models.Model):
    post = models.ForeignKey('Post', models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('post', 'user',)

    def __str__(self):
        return self.post.user.username + '_' + str(self.post.created_at) + '_' + self.user.username


class Group(models.Model):
    photo = models.ImageField(upload_to="group_photos/%Y/%m/%d/")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name