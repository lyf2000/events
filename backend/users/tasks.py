from django.contrib.auth import get_user_model

UserModel = get_user_model()


# @shared_task
# def send_register_confirmation_email(user_id, domain, to_email):
#     user = UserModel.objects.get(id=user_id)
#     mail_subject = 'Activate your event account.'
#     message = render_to_string('users/acc_active_email.html', {
#         'user': user,
#         'domain': domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#     })
#
#     msg = EmailMultiAlternatives(mail_subject, '', 'from_email', [to_email])
#     msg.attach_alternative(message, "text/html")
#     msg.send()


# @shared_task
# def send_reset_email(to_email, domain, site_name, use_https, subject_template_name, email_template_name, from_email,
#                      html_email_template_name):
#     users = UserModel.objects.filter(email=to_email)
#     for user in users:
#         print(user)
#         context = {
#             'email': to_email,
#             'domain': domain,
#             'site_name': site_name,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'user': user.username,
#             'token': default_token_generator.make_token(user),
#             'protocol': 'https' if use_https else 'http',
#             # **(extra_email_context or {}),
#         }
#         PasswordResetForm().send_mail(
#             subject_template_name, email_template_name, context, from_email,
#             to_email, html_email_template_name=html_email_template_name,
#         )
