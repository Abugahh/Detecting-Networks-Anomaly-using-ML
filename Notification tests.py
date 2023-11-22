# from plyer import notification

# notification.notify(
#     title='Testing',
#     message='This wass a test',
#     timeout=60
# )
#print ("sciprt is executed")

# from pynotifier import Notification


# Notification(
#     title='Test',
#     description='This is a test',
#     duration=5,  # Duration in seconds
#     #urgency=Notification.URGENCY_CRITICAL
# ).send()


import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def main():
    n = await notifier.send(
        title="Hello world!",
        message="Sent from Python"
    )
    await asyncio.sleep(5)  # wait a bit before clearing notification
    await notifier.clear(n)  # removes the notification
    await notifier.clear_all()  # removes all notifications for this app

asyncio.run(main())



   # notifier = DesktopNotifier()

    # async def main():
    #     # Your existing code here

    #     # If an attack is predicted, send a desktop notification
    #     if predictions[0] == 'Fuzzers, Analysis , Reconnaissance , DoS, Shellcode, Generic, Backdoors,Exploits,Worms':
    #         await notifier.send(
    #             title='Alert',
    #             message='An attack was predicted!',
    #             timeout=30
    #         )

    #     # Run the main function with asyncio
    # asyncio.run(main())

    # If an attack is predicted, send a desktop notification
    # if predictions[0] == 'Fuzzers, Analysis , Reconnaissance , DoS, Shellcode, Generic, Backdoors,Exploits,Worms':
    #         notification.notify(
    #             title='Alert',
    #             message='An attack was predicted!',
    #             timeout=30
    #         )
