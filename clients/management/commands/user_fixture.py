from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from clients.models import Client, Newsletter, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # user_johndoe = User.objects.create(surname="johndoe", email='marchuk-8282@mail.ru')
        # # user_petya = User.objects.get(surname="Петя", email='andmarchu8@gmail.com')
        # group = Group.objects.create(name="Manager")
        # user_johndoe.groups.add(group)
        # user_johndoe.set_password('123qwe321')
        # user_johndoe.save()

        new_group = Group(name="Manager")
        new_group.save()

        client_content_type = ContentType.objects.get_for_model(Client)
        newsletter_content_type = ContentType.objects.get_for_model(Newsletter)

        add_permission_client = Permission.objects.get(codename="add_client", content_type=client_content_type)
        change_permission_client = Permission.objects.get(codename="change_client", content_type=client_content_type)
        delete_permission_client = Permission.objects.get(codename="delete_client", content_type=client_content_type)
        view_permission_client = Permission.objects.get(codename="view_client", content_type=client_content_type)

        add_permission_newsletter = Permission.objects.get(codename="add_newsletter",
                                                           content_type=newsletter_content_type)
        change_permission_newsletter = Permission.objects.get(codename="change_newsletter",
                                                              content_type=newsletter_content_type)
        delete_permission_newsletter = Permission.objects.get(codename="delete_newsletter",
                                                              content_type=newsletter_content_type)
        view_permission_newsletter = Permission.objects.get(codename="view_newsletter",
                                                            content_type=newsletter_content_type)

        new_group.permissions.add(add_permission_client, change_permission_client, delete_permission_client,
                                  view_permission_client, add_permission_newsletter, change_permission_newsletter,
                                  delete_permission_newsletter, view_permission_newsletter
                                  )
        new_group.save()

