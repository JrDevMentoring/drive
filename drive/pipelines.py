from django.contrib.auth.models import User

from django_slack_oauth.models import SlackUser


def register_user(request, api_data):
    user = User.objects.create_user(
        username=api_data['user_id']
        password='theothernotsocommonpassword'
    )

    slacker, _ = SlackUser.objects.get_or_create(slacker=user)
    slacker.access_token = api_data.pop('access_token')
    slacker.extras = api_data
    slacker.save()

    request.created_user = user

    return request, api_data

def debug_oauth_request(request, api_data):
    print(api_data)
    return request, api_data
