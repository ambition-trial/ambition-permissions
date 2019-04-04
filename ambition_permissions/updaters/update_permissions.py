from edc_permissions.permissions_updater import PermissionsUpdater
from edc_permissions.utils import (
    create_edc_dashboard_permissions,
    create_edc_navbar_permissions,
)

from ..group_names import TMG, RANDO
from .auditor import extra_auditor_group_permissions
from .clinic import extra_clinic_group_permissions
from .lab import extra_lab_group_permissions, extra_lab_view_group_permissions
from .pii_models import extra_pii_models
from .rando import update_rando_group_permissions
from .tmg import update_tmg_group_permissions

extra_updaters = [
    extra_auditor_group_permissions,
    extra_clinic_group_permissions,
    extra_lab_group_permissions,
    extra_lab_view_group_permissions,
    update_rando_group_permissions,
    update_tmg_group_permissions,
]


def update_permissions():

    create_edc_dashboard_permissions(
        extra_codename_tpls=[
            ("edc_dashboard.view_screening_listboard", "Can view Screening Listboard"),
            ("edc_dashboard.view_subject_listboard", "Can view Subject Listboard"),
            ("edc_dashboard.view_tmg_listboard", "Can view TMG Listboard"),
        ]
    )
    create_edc_navbar_permissions(
        extra_codename_tpls=[
            ("edc_navbar.nav_tmg_section", "Can access TMG section"),
            ("edc_navbar.nav_subject_section", "Can access subject section"),
            ("edc_navbar.nav_screening_section", "Can access screening section"),
        ]
    )

    PermissionsUpdater(
        extra_pii_models=extra_pii_models,
        extra_updaters=extra_updaters,
        extra_group_names=[RANDO, TMG],
    )
