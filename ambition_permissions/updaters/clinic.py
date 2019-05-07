from django.contrib.auth.models import Group
from edc_permissions.utils import (
    add_permissions_to_group_by_app_label,
    add_permissions_to_group_by_codenames,
    make_view_only_app_label,
    make_view_only_model,
    remove_historical_group_permissions,
    remove_permissions_by_model,
    remove_pii_permissions_from_group,
)

from ..group_names import CLINIC
from .pii_models import pii_models


def extra_clinic_group_permissions():

    group_name = CLINIC
    group = Group.objects.get(name=group_name)

    for app_label in [
        "ambition_ae",
        "ambition_lists",
        "ambition_prn",
        "ambition_subject",
        "edc_offstudy",
    ]:
        add_permissions_to_group_by_app_label(group, app_label)

    make_view_only_app_label(group, "ambition_lists")

    make_view_only_model(group, "ambition_ae.aetmg")

    remove_permissions_by_model(group, "ambition_prn.deathreporttmg")

    # nav and dashboard
    add_permissions_to_group_by_codenames(
        group,
        codenames=[
            "edc_navbar.nav_ae_section",
            "edc_navbar.nav_subject_section",
            "edc_navbar.nav_screening_section",
            "edc_dashboard.view_ae_listboard",
            "edc_dashboard.view_subject_review_listboard",
            "edc_dashboard.view_screening_listboard",
            "edc_dashboard.view_subject_listboard",
            "edc_dashboard.view_tmg_listboard",
        ],
    )

    remove_pii_permissions_from_group(group, extra_pii_models=pii_models)
    remove_historical_group_permissions(group)
    return group_name
