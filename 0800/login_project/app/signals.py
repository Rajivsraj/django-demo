from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("logged in successfully")
    print("Sender: ", sender)
    print("request: ", request)
    print("user: ", user.password)
    print("**kwar: ", kwargs)
# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out)
def logout_signal(sender, request, user, **kwargs):
    print("Logout success -----------")
    print("Sender: ", sender)
    print("user: ", user)
    print("req: ", request)
    # print("**kwar: ", {kwargs})


@receiver(user_login_failed)
def login_fail(sender, credentials, request, **kwargs):
    print("Login Faild")
    print("Sender: ", sender)
    print("Cred: ", credentials)
    print("req: ", request)
    print("**kwar: ", {kwargs})


# pre_save
@receiver(pre_save, sender=User)
def pre_save_signal(sender, instance, raw, using, update_fields, **kwargs):
    print("pre save")
    print("Sender: ", sender)
    print("instance: ", instance)
    print("raw: ", raw)
    print("using: ", using)
    print("updated: ", update_fields)
    print("kwargs: ", kwargs)

    if update_fields:
        print("Data updated")
    else:
        print("New Record Created")


@receiver(post_save, sender=User)
def post_save_signal(sender, instance, created, **kwargs):
    print("----------post save signals --------------")
    print("Sender: ", sender)
    print("instance: ", instance)
    print("Created: ", created)
    print("kwargs: ", kwargs)