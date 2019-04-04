from django.contrib.auth.models import Group
from edc_permissions.utils import (
    add_permissions_to_group_by_model,
    make_view_only_model,
    add_permissions_to_group_by_codenames,
    remove_pii_permissions_from_group,
    remove_historical_group_permissions,
)
from ..group_names import RANDO
from .pii_models import pii_models


def update_rando_group_permissions():
    group_name = RANDO
    group = Group.objects.get(name=group_name)
    group.permissions.clear()

    add_permissions_to_group_by_model(group, "ambition_rando.randomizationlist")
    make_view_only_model(group, "ambition_rando.randomizationlist")

    add_permissions_to_group_by_codenames(
        group, codenames=["ambition_rando.display_randomization"]
    )

    remove_pii_permissions_from_group(group, extra_pii_models=pii_models)
    remove_historical_group_permissions(group)
