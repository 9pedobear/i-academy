from django.core.mail import send_mail


def send_password_with_username(user_email, username):
    send_mail(
        'Zeon IT hub'
        ' Пароль',
        f'ваш пароль : wow808wtf745\n ваш логин {username}',
        'sabyrjanov39@gmail.com',
        [user_email],
        fail_silently=True,
    )
