from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    # def _make_hash_value(self, user, timestamp):
    #     login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
    #     return (
    #         six.text_type(user.pk) + six.text_type(timestamp) +
    #         six.text_type(user.is_active) + six.text_type(login_timestamp)
    #     )
    pass
account_activation_token = TokenGenerator()