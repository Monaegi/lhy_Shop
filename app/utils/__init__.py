from django.http import QueryDict
from django.urls import reverse


def build_url(*args, **kwargs):
    params = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)

    if not params:
        return url

    qdict = QueryDict('', mutable=True)
    for k, v in params.items():
        if isinstance(v, list):
            qdict.setlist(k, v)
        else:
            qdict[k] = v
    return f'{url}?{qdict.urlencode()}'
