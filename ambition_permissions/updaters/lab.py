from django.contrib.auth.models import Group
from edc_permissions import LAB, LAB_VIEW
from edc_permissions.utils import (
    add_permissions_to_group_by_codenames,
    add_permissions_to_group_by_model,
    remove_permissions_from_model_by_action,
    remove_pii_permissions_from_group,
    remove_historical_group_permissions,
)

from .pii_models import pii_models
from edc_permissions.utils.generic import make_view_only_model
from django.conf import settings


def extra_lab_group_permissions():

    group_name = LAB
    group = Group.objects.get(name=group_name)

    add_permissions_to_group_by_model(group, settings.SUBJECT_REQUISITION_MODEL)
    remove_permissions_from_model_by_action(
        group, model=settings.SUBJECT_REQUISITION_MODEL, actions=["delete", "add"]
    )

    add_permissions_to_group_by_codenames(
        group=group,
        codenames=[
            "edc_dashboard.view_screening_listboard",
            "edc_dashboard.view_subject_listboard",
        ],
    )
    add_permissions_to_group_by_codenames(
        group=group, codenames=["edc_navbar.nav_subject_section"]
    )

    remove_pii_permissions_from_group(group, extra_pii_models=pii_models)
    remove_historical_group_permissions(group)
    return group_name


def extra_lab_view_group_permissions():

    group_name = LAB_VIEW
    group = Group.objects.get(name=group_name)

    add_permissions_to_group_by_model(group, settings.SUBJECT_REQUISITION_MODEL)
    make_view_only_model(group, settings.SUBJECT_REQUISITION_MODEL)
    remove_pii_permissions_from_group(group, extra_pii_models=pii_models)
    remove_historical_group_permissions(group)
    return group_name
