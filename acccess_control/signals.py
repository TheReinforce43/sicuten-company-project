import subprocess
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from acccess_control.Model.accces_log_model import AccessLog


LOG_FILE = "system_events.log"


def write_log_via_subprocess(message: str):
    """
    Append a log message to system_events.log using subprocess
    """
    subprocess.run(
        ["bash", "-c", f'echo "{message}" >> {LOG_FILE}'],
        check=False
    )


@receiver(post_save, sender=AccessLog)
def accesslog_created(sender, instance, created, **kwargs):
    """
    Trigger ONLY when a new AccessLog is created
    """
    if not created:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "GRANTED" if instance.access_granted else "DENIED"

    log_message = (
        f"[{timestamp}] - CREATE: "
        f"Access log created for card {instance.card_id}. "
        f"Status: {status}."
    )

    write_log_via_subprocess(log_message)


@receiver(post_delete, sender=AccessLog)
def accesslog_deleted(sender, instance, **kwargs):
    """
    Trigger when an AccessLog is deleted
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = (
        f"[{timestamp}] - DELETE: "
        f"Access log (ID: {instance.id}) "
        f"for card {instance.card_id} was deleted."
    )

    write_log_via_subprocess(log_message)
