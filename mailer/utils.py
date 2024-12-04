from logging import getLogger

from django.template import engines
from django.utils.safestring import mark_safe

logger = getLogger()


def render(src, request=None, engine_name="django", safe=True, **ctx):
    text = engines[engine_name].from_string(src).render(ctx, request=request)
    return safe and mark_safe(text) or text
