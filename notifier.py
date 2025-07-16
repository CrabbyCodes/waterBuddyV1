from plyer import notification


def send_notification(title: str, message: str):
    """
    Shows a system notification with the given title and message.
    works on Windows 10/11
    """
    notification.notify(
        title=title,
        message=message,
        timeout=5 #secs
    )