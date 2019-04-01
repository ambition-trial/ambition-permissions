"""A snapshot of current codenames.

Validated with the PermissionsInspector in tests and system checks.

"""

from edc_permissions.codenames import (
    account_manager,
    administration,
    data_manager,
    everyone,
    export,
    lab,
    pharmacy,
)
from edc_permissions.constants import (
    AUDITOR,
    LAB,
    EVERYONE,
    PII,
    ADMINISTRATION,
    PHARMACY,
    ACCOUNT_MANAGER,
    CLINIC,
    PII_VIEW,
    EXPORT,
    DATA_MANAGER,
)

from ..group_names import TMG, RANDO
from .auditor import auditor
from .clinic import clinic
from .pii_view import pii_view
from .pii import pii
from .rando import rando
from .tmg import tmg


CODENAMES = {
    ACCOUNT_MANAGER: account_manager,
    ADMINISTRATION: administration,
    AUDITOR: auditor,
    CLINIC: clinic,
    DATA_MANAGER: data_manager,
    EVERYONE: everyone,
    EXPORT: export,
    LAB: lab,
    PHARMACY: pharmacy,
    PII: pii,
    PII_VIEW: pii_view,
    RANDO: rando,
    TMG: tmg,
}
