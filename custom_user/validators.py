import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class AlphanumericPasswordValidator:
    def validate(self, password, user=None):
        if not re.fullmatch(r'[A-Za-z0-9]{8}', password):
            raise ValidationError(
                _("Password must be exactly 8 alphanumeric characters."),
                code='password_not_alphanumeric',
            )

    def get_help_text(self):
        return _("Your password must be exactly 8 alphanumeric characters (letters and numbers only).")
