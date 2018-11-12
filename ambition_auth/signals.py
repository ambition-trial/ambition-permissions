from ambition_ae.constants import AE_TMG_ACTION
from ambition_prn.constants import DEATH_REPORT_TMG_ACTION
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import m2m_changed
from django.dispatch.dispatcher import receiver
from edc_notification.models import Notification

from .group_names import TMG


@receiver(m2m_changed, weak=False,
          dispatch_uid='update_notifications_for_group')
def update_notifications_for_group(
        action, instance, reverse, model, pk_set, using, **kwargs):

    try:
        instance.userprofile
    except AttributeError:
        pass
    else:
        tmg_ae_notification = Notification.objects.get(
            name=AE_TMG_ACTION)
        tmg_death_notification = Notification.objects.get(
            name=DEATH_REPORT_TMG_ACTION)
        try:
            instance.groups.get(name=TMG)
        except ObjectDoesNotExist:
            instance.userprofile.email_notifications.remove(
                tmg_ae_notification)
            instance.userprofile.email_notifications.remove(
                tmg_death_notification)
        else:
            instance.userprofile.email_notifications.add(
                tmg_ae_notification)
            instance.userprofile.email_notifications.add(
                tmg_death_notification)
