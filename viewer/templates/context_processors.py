from viewer.models import User_category


def points(request):
    points = []
    if request.user.is_authenticated:
        for score in User_category.objects.filter(user_id=request.user).values('points'):
            points.append(score['points'])
    return {'points': points}
