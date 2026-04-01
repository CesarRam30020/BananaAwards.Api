from api.models import Edition

def get(pk=None):
    if pk is not None:
        try:
            return Edition.objects.get(pk=pk)
        except Edition.DoesNotExist:
            return None

    return Edition.objects.all()

def create(data):
    object = Edition.objects.create(**data)
    return object

def update(pk, data):
    try:
        object = Edition.objects.get(pk=pk)
        for attr, value in data.items():
            setattr(object, attr, value)
        object.save()
        return object
    except Edition.DoesNotExist:
        return None

def delete(pk):
    try:
        object = Edition.objects.get(pk=pk)
        object.delete()
        return object
    except Edition.DoesNotExist:
        return None