import ssl
from django.utils.functional import cached_property
from django.core.mail.backends.smtp import EmailBackend

class NewClass(EmailBackend):
    @cached_property
    def ssl_context(self):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context
