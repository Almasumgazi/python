from plyer import notification

import time
icon_image="D:\Code\Python-GitHub\python\icon.ico"
if __name__=="__main__":
    notification.notify(
            title="please please please drink water",
            message="1.For men: Around 3.7 liters or 125 ounces 2.For women: Around 2.7 liters or 91 ounces",
            app_icon=icon_image,
            timeout=12
    )
    