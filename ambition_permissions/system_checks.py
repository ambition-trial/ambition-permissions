# import sys
#
# from django.conf import settings
# from django.core.checks import Warning, register
#
# from .codenames import CODENAMES
# from .group_names import RANDO, TMG
#
#
# @register()
# def ambition_permission_check(app_configs, **kwargs):
#     errors = []
#     if (
#         settings.APP_NAME == "ambition_edc"
#         and "migrate" not in sys.argv
#         and "makemigrations" not in sys.argv
#     ):
#         default_codenames = CODENAMES
#         inspector = PermissionsInspector(
#             default_codenames=default_codenames,
#             manually_validate=True,
#             raise_on_warning=True,
#             extra_group_names=[RANDO, TMG],
#             extra_pii_models=[
#                 "ambition_screening.subjectscreening",
#                 "ambition_subject.subjectconsent",
#                 "ambition_subject.subjectreconsent",
#                 "edc_locator.subjectlocator",
#                 "edc_registration.registeredsubject",
#             ],
#         )
#         for group_name in inspector.group_names:
#             try:
#                 inspector.compare_codenames(group_name)
#             except PermissionsInspectorWarning as e:
#                 errors.append(
#                     Warning(
#                         str(e),
#                         hint=(
#                             "Check permissions for group using the "
#                             "PermissionInspector.diff_codenames."
#                         ),
#                         obj=group_name,
#                         id="ambition_permissions.W001",
#                     )
#                 )
#             except PermissionsInspectorError as e:
#                 errors.append(
#                     Warning(
#                         str(e),
#                         hint=(
#                             "Check permissions for group using the "
#                             "PermissionInspector."
#                         ),
#                         obj=group_name,
#                         id="ambition_permissions.W002",
#                     )
#                 )
#     return errors
