from django.template import engines
from django.utils.safestring import mark_safe
from logging import getLogger


logger = getLogger()


def render(src, request=None, engine_name="django", safe=True, **ctx):
    text = engines[engine_name].from_string(src).render(ctx, request=request)
    return safe and mark_safe(text) or text
