from django.contrib.auth.models import Group
from edc_permissions.utils import (
    add_permissions_to_group_by_app_label,
    make_view_only_app_label,
    remove_historical_group_permissions,
    remove_pii_permissions_from_group,
)

from edc_permissions import AUDITOR
from edc_permissions.utils.generic import add_permissions_to_group_by_codenames

from .pii_models import pii_models

extra_auditor_app_labels = [
    "ambition_ae",
    "ambition_screening",
    "ambition_subject",
    "ambition_prn",
    "ambition_lists",
]


def extra_auditor_group_permissions():

    group_name = AUDITOR
    group = Group.objects.get(name=group_name)

    # nav and dashboard
    add_permissions_to_group_by_codenames(
        group,
        codenames=[
            "edc_navbar.nav_tmg_section",
            "edc_navbar.nav_subject_section",
            "edc_navbar.nav_screening_section",
            "edc_dashboard.view_subject_review_listboard",
            "edc_dashboard.view_screening_listboard",
            "edc_dashboard.view_subject_listboard",
            "edc_dashboard.view_tmg_listboard",
        ],
    )

    for app_label in extra_auditor_app_labels:
        add_permissions_to_group_by_app_label(group, app_label)
        make_view_only_app_label(group, app_label)

    remove_pii_permissions_from_group(group, extra_pii_models=pii_models)
    remove_historical_group_permissions(group)
