from django.contrib.auth.models import Group

from edc_permissions.utils import (
    add_edc_action_permissions,
    add_permissions_to_group_by_app_label,
    add_permissions_to_group_by_codenames,
    add_permissions_to_group_by_model,
    make_view_only_app_label,
    make_view_only_model,
    remove_historical_group_permissions,
    remove_permissions_by_model,
    remove_pii_permissions_from_group,
)

from ..group_names import TMG
from .pii_models import pii_models


def update_tmg_group_permissions():
    group_name = TMG
    group = Group.objects.get(name=group_name)
    group.permissions.clear()

    # edc_action_item
    add_edc_action_permissions(group, allow_delete=True)
    make_view_only_model(group, "edc_action_item.actiontype")
    make_view_only_model(group, "edc_action_item.reference")

    # ambition_ae
    add_permissions_to_group_by_app_label(group, "ambition_ae")
    make_view_only_app_label(group, "ambition_ae")
    add_permissions_to_group_by_model(group, "ambition_ae.aetmg")
    add_permissions_to_group_by_model(group, "ambition_ae.historicalaetmg")

    # ambition_subject
    add_permissions_to_group_by_app_label(group, "ambition_subject")
    make_view_only_app_label(group, "ambition_subject")
    remove_permissions_by_model(group, "ambition_subject.subjectconsent")
    remove_permissions_by_model(group, "ambition_subject.subjectreconsent")

    # ambition_subject
    add_permissions_to_group_by_app_label(group, "ambition_lists")
    make_view_only_app_label(group, "ambition_lists")

    # ambition_prn
    add_permissions_to_group_by_model(group, "ambition_prn.deathreporttmg")
    add_permissions_to_group_by_codenames(
        group,
        codenames=[
            "ambition_prn.view_amphotericinmisseddoses",
            "ambition_prn.view_fluconazolemisseddoses",
            "ambition_prn.view_flucytosinemisseddoses",
            "ambition_prn.view_significantdiagnoses",
            "ambition_prn.view_historicalamphotericinmisseddoses",
            "ambition_prn.view_historicalfluconazolemisseddoses",
            "ambition_prn.view_historicalflucytosinemisseddoses",
            "ambition_prn.view_historicalsignificantdiagnoses",
            "ambition_prn.view_deathreport",
        ],
    )
    add_permissions_to_group_by_codenames(
        group,
        codenames=[
            "edc_appointment.view_historicalappointment",
            "edc_appointment.view_appointment",
        ],
    )

    # nav and dashboard
    add_permissions_to_group_by_codenames(
        group,
        codenames=[
            "edc_navbar.nav_ae_section",
            "edc_dashboard.view_ae_listboard",
            "edc_navbar.nav_tmg_section",
            "edc_navbar.nav_subject_section",
            "edc_navbar.nav_screening_section",
            "edc_dashboard.view_subject_review_listboard",
            "edc_dashboard.view_screening_listboard",
            "edc_dashboard.view_subject_listboard",
            "edc_dashboard.view_tmg_listboard",
        ],
    )

    remove_pii_permissions_from_group(group, extra_pii_models=pii_models)
    remove_historical_group_permissions(group)
    return group_name
