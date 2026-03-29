from api.models import User

def get(pk=None):
    if pk is not None:
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
    
    return User.objects.all()

def create(data):
    user = User.objects.create(**data)
    return user

def update(pk, data):
    try:
        user = User.objects.get(pk=pk)
        for attr, value in data.items():
            setattr(user, attr, value)
        user.save()
        return user
    except User.DoesNotExist:
        return None

def delete(pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return user
    except User.DoesNotExist:
        return None