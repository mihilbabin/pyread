from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, pre_save

class Profile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    image = models.ImageField(upload_to="profileimages", blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(pk=self.pk)
            if this.image != self.image:
                this.image.delete(save=False)
        except Profile.DoesNotExist:
            pass
        super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_delete, sender=Profile)
def profile_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
