from .models import SiteConfiguration, Modal, Footer

def site_configuration(request):
    try:
        site_config = SiteConfiguration.objects.latest('updated')
    except SiteConfiguration.DoesNotExist:
        site_config = None

    return {'site_config': site_config}


def modal(request):
    try:
        modal = Modal.objects.latest('updated')
    except Modal.DoesNotExist:
        modal = None

    return {'modal': modal}


def footer(request):
    try:
        footer = Footer.objects.latest('updated')
    except Footer.DoesNotExist:
        footer = None

    return {'footer': footer}
