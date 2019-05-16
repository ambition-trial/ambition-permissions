from django.contrib.auth.models import Group
from edc_permissions.utils import add_permissions_to_group_by_codenames

from ..group_names import AE_REVIEW


def update_ae_review_group_permissions():

    group_name = AE_REVIEW
    group = Group.objects.get(name=group_name)

    # nav and dashboard
    add_permissions_to_group_by_codenames(
        group,
        codenames=["edc_navbar.nav_ae_section", "edc_dashboard.view_ae_listboard"],
    )
    return group_name
