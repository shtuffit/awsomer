from django.conf import settings # import the settings file

def installed_apps(request):
    return {'INSTALLED_APPS': settings.INSTALLED_APPS}
