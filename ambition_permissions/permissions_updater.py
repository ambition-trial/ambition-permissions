from django.conf import settings
from django.contrib.auth.models import Group, Permission
from edc_permissions.constants import ADMINISTRATION, PII, PII_VIEW
from edc_permissions.constants import CLINIC, LAB, AUDITOR
from edc_permissions.constants.group_names import PHARMACY
from edc_permissions.permissions_updater import (
    PermissionsUpdater as EdcPermissionsUpdater,
)

from .group_names import RANDO, TMG


class PermissionsUpdater(EdcPermissionsUpdater):

    """
    A class to setup persistent access permissions for
    models and other objects.

    After making changes run migrate and check.
    """

    extra_pii_models = [
        "ambition_subject.subjectconsent",
        "ambition_subject.subjectreconsent",
        "ambition_screening.subjectscreening",
    ]

    extra_auditor_app_labels = [
        "ambition_ae",
        "ambition_screening",
        "ambition_subject",
        "ambition_prn",
        "ambition_lists",
    ]

    extra_dashboard_codenames = {
        settings.APP_NAME: [
            ("view_screening_listboard", "Can view Screening Listboard"),
            ("view_subject_listboard", "Can view Subject Listboard"),
            ("view_tmg_listboard", "Can view TMG Listboard"),
        ]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for group in Group.objects.filter(name__in=[CLINIC, TMG, LAB, AUDITOR]):
            self.add_dashboard_permissions(group, codename="view_screening_listboard")
            self.add_dashboard_permissions(group, codename="view_subject_listboard")
            if group.name != LAB:
                self.add_dashboard_permissions(group, codename="view_tmg_listboard")
            self.add_dashboard_permissions(
                group, codename="view_subject_review_listboard"
            )
            self.add_dashboard_permissions(group, dashboard_category=LAB)

        pii_group_names = [PII, PII_VIEW]
        pii_codenames = [
            x.codename
            for x in Permission.objects.filter(group__name__in=pii_group_names)
        ]
        for group_name in self.group_names:
            # ensure PII codenames not in any other group
            if group_name not in pii_group_names:
                codenames = [
                    x.codename
                    for x in Permission.objects.filter(group__name=group_name)
                ]
                group = Group.objects.get(name=group_name)
                for permission in Permission.objects.filter(
                    codename__in=[x for x in codenames if x in pii_codenames]
                ):
                    group.permissions.remove(permission)

    def extra_lab_group_permissions(self, group):
        for permission in Permission.objects.filter(
            content_type__app_label="ambition_subject",
            content_type__model="subjectrequisition",
            codename__startswith="view",
        ):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label="ambition_subject",
            content_type__model="subjectrequisition",
            codename__startswith="change",
        ):
            group.permissions.add(permission)

        self.add_permissions_to_group(
            group=group, codenames=["edc_navbar.nav_subject_section"]
        )

        self.add_permissions_to_group(
            group=group, codenames=["edc_navbar.nav_subject_section"]
        )

    def extra_clinic_group_permissions(self, group):

        # add basic permissions. Exclude PII models here as they will
        # be included in another group (e.g. PII or PI_VIEW)
        exclude_models = [m.split(".")[1] for m in self.pii_models] + [
            "aetmg",
            "deathreporttmg",
        ]
        for permission in Permission.objects.filter(
            content_type__app_label__in=[
                "ambition_ae",
                "ambition_prn",
                "ambition_subject",
                "edc_offstudy",
            ]
        ).exclude(content_type__model__in=exclude_models):
            group.permissions.add(permission)

        # allow CLINIC users to view Ambition list models
        for permission in Permission.objects.filter(
            content_type__app_label__in=["ambition_lists"], codename__startswith="view"
        ):
            group.permissions.add(permission)

        # allow CLINIC users to view AeTmg
        for permission in Permission.objects.filter(
            content_type__app_label__in=["ambition_ae"],
            content_type__model__in=["aetmg"],
            codename__startswith="view",
        ):
            group.permissions.add(permission)

        self.add_permissions_to_group(
            group=group,
            codenames=[
                "edc_navbar.nav_subject_section",
                "edc_navbar.nav_screening_section",
            ],
        )

    def update_tmg_group_permissions(self):
        group_name = TMG
        group = Group.objects.get(name=group_name)
        group.permissions.clear()
        for permission in Permission.objects.filter(
            content_type__app_label__in=["edc_action_item"]
        ):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label__in=["ambition_ae"],
            content_type__model__in=["aetmg"],
        ):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label__in=["ambition_ae"], codename__startswith="view"
        ):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label__in=["ambition_subject"],
            codename__startswith="view",
        ).exclude(content_type__model__in=["subjectconsent", "subjectreconsent"]):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label__in=["ambition_lists"], codename__startswith="view"
        ):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label__in=["edc_appointment"],
            content_type__model__in=["appointment", "historicalappointment"],
        ):
            group.permissions.add(permission)
        for permission in Permission.objects.filter(
            content_type__app_label="ambition_prn", content_type__model="deathreporttmg"
        ):
            group.permissions.add(permission)

        permission = Permission.objects.get(
            content_type__app_label="ambition_prn", codename="view_deathreport"
        )
        group.permissions.add(permission)

        codenames = [
            "ambition_prn.view_amphotericinmisseddoses",
            "ambition_prn.view_fluconazolemisseddoses",
            "ambition_prn.view_flucytosinemisseddoses",
            "ambition_prn.view_significantdiagnoses",
            "ambition_prn.view_historicalamphotericinmisseddoses",
            "ambition_prn.view_historicalfluconazolemisseddoses",
            "ambition_prn.view_historicalflucytosinemisseddoses",
            "ambition_prn.view_historicalsignificantdiagnoses",
        ]
        self.add_permissions_to_group(group=group, codenames=codenames)

        Permission.objects.get(
            content_type__app_label="edc_navbar", codename="nav_tmg_section"
        )
        group.permissions.add(permission)

        self.add_permissions_to_group(
            group=group,
            codenames=[
                "edc_navbar.nav_tmg_section",
                "edc_dashboard.view_subject_review_listboard",
            ],
        )

    def update_rando_group_permissions(self):
        group_name = RANDO
        group = Group.objects.get(name=group_name)
        group.permissions.clear()
        for permission in Permission.objects.filter(
            content_type__app_label="ambition_rando", codename="view_randomizationlist"
        ):
            group.permissions.add(permission)
        permission = Permission.objects.get(
            content_type__app_label="ambition_rando", codename="display_randomization"
        )
        group.permissions.add(permission)
