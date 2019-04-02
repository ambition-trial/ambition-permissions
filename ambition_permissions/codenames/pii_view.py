from edc_permissions.codenames import pii_view

pii_view += [
    "ambition_screening.view_historicalsubjectscreening",
    "ambition_screening.view_subjectscreening",
    "ambition_subject.view_historicalsubjectreconsent",
    "ambition_subject.view_subjectreconsent",
]

pii_view.sort()
