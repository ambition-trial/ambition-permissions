from django.test import TestCase, tag
from edc_permissions import (
    ACCOUNT_MANAGER,
    ADMINISTRATION,
    AUDITOR,
    CLINIC,
    DATA_MANAGER,
    EVERYONE,
    EXPORT,
    LAB,
    LAB_VIEW,
    PHARMACY,
    PII,
    PII_VIEW,
)

from edc_permissions.codenames import pharmacy, export, data_manager, administration
from edc_permissions.utils import compare_codenames_for_group

from ..codenames import (
    ae_review,
    account_manager,
    auditor,
    clinic,
    everyone,
    lab,
    lab_view,
    pii,
    pii_view,
    rando,
    tmg,
    CODENAMES,
)
from ..group_names import RANDO, AE_REVIEW, TMG
from ..updaters import update_permissions


class TestPermissions(TestCase):
    def test_pii(self):
        update_permissions()
        # show_permissions_for_group(group_name=PII)
        compare_codenames_for_group(group_name=PII, expected=pii)
        # show_permissions_for_group(group_name=PII_VIEW)
        compare_codenames_for_group(group_name=PII_VIEW, expected=pii_view)

    def test_ae_review(self):
        update_permissions()
        compare_codenames_for_group(group_name=AE_REVIEW, expected=ae_review)

    def test_tmg(self):
        update_permissions()
        compare_codenames_for_group(group_name=TMG, expected=tmg)

    def test_pharmacy(self):
        update_permissions()
        compare_codenames_for_group(group_name=PHARMACY, expected=pharmacy)

    def test_export(self):
        update_permissions()
        compare_codenames_for_group(group_name=EXPORT, expected=export)

    def test_everyone(self):
        update_permissions()
        compare_codenames_for_group(group_name=EVERYONE, expected=everyone)

    def test_data_manager(self):
        update_permissions()
        compare_codenames_for_group(group_name=DATA_MANAGER, expected=data_manager)

    def test_auditors(self):
        update_permissions()
        compare_codenames_for_group(group_name=AUDITOR, expected=auditor)

    def test_administrations(self):
        update_permissions()
        compare_codenames_for_group(group_name=ADMINISTRATION, expected=administration)

    def test_account_manager(self):
        update_permissions()
        compare_codenames_for_group(
            group_name=ACCOUNT_MANAGER, expected=account_manager
        )

    def test_clinic(self):
        update_permissions()
        compare_codenames_for_group(group_name=CLINIC, expected=clinic)

    def test_rando(self):
        update_permissions()
        compare_codenames_for_group(group_name=RANDO, expected=rando)

    def test_lab(self):
        update_permissions()
        compare_codenames_for_group(group_name=LAB, expected=lab)
        compare_codenames_for_group(group_name=LAB_VIEW, expected=lab_view)

    def test_permissions_updater(self):
        update_permissions()
        for group_name, expected in CODENAMES.items():
            compare_codenames_for_group(group_name=group_name, expected=expected)
