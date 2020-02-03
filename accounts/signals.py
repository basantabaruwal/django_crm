from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created: # user is created
        # assign a default group to the user
        group = Group.objects.get(name='customer') # default group
        user = instance
        user.groups.add(group)
        print("**************Default Group assined to user ", user.username)

# # we can use the decorator instead of this
# post_save.connect(assign_group, sender=User)



### Required to config apps.py and override ready method there for this to work