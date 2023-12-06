from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import ldap

class Command(BaseCommand):
    help = 'Synchronize users from LDAP'

    def handle(self, *args, **kwargs):
        # Connect to LDAP
        conn = ldap.initialize('ldap://192.168.31.250:389')
        conn.simple_bind_s('CN=Administrator,CN=Users,DC=qtoh,DC=local', 'Cow&Gate')

        # Search for users
        result = conn.search_s('CN=Estimators,DC=qtoh,DC=local', ldap.SCOPE_SUBTREE, '(objectClass=user)')
        
        # Synchronize users
        for dn, entry in result:
            User.objects.update_or_create(
                username=entry['sAMAccountName'][0].decode(),
                defaults={
                    'first_name': entry['givenName'][0].decode(),
                    'last_name': entry['sn'][0].decode(),
                    'email': entry['mail'][0].decode(),
                }
            )

        # Unbind the connection
    #     conn.unbind_s()