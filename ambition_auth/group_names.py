from edc_permissions.constants import ADMINISTRATION, EVERYONE, CLINIC, PII
from edc_permissions.constants.group_names import LAB, PII_VIEW

RANDO = "RANDO"
TMG = "TMG"

# commonly grouped like this ..
CLINIC_USER_GROUPS = [ADMINISTRATION, EVERYONE,
                      CLINIC, PII, RANDO]
LAB_USER_GROUPS = [ADMINISTRATION, EVERYONE, LAB, PII_VIEW]
TMG_USER_GROUPS = [ADMINISTRATION, EVERYONE, TMG]
