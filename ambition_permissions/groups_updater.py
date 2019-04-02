from edc_permissions.groups_updater import GroupsUpdater
from edc_permissions.constants import ADMINISTRATION, LAB, PII, PII_VIEW, AUDITOR

from .group_names import RANDO, TMG


class GroupUpdater(GroupsUpdater):

    extra_group_names = [RANDO, TMG]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ensure_users_in_group(ADMINISTRATION, users_by_groups=[TMG])
        self.ensure_users_not_in_group(PII, users_by_groups=[TMG])
        self.ensure_users_not_in_group(PII_VIEW, users_by_groups=[TMG])
        self.ensure_users_not_in_group(
            RANDO, users_by_groups=[TMG, AUDITOR, LAB])