from edc_permissions.utils import get_pii_models

extra_pii_models = [
    "ambition_subject.subjectconsent",
    "ambition_subject.subjectreconsent",
    "ambition_screening.subjectscreening",
]

pii_models = get_pii_models(extra_pii_models)
