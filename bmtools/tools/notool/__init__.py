
from ..registry import register

@register("notool")
def notool():
    from .api import build_tool
    return build_tool
