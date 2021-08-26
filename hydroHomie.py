from plyer import notification
import os
import time

title = "Drink a cup of water. Now"
msg = "DRINK DRINK DRINK ASAP"
icon = "water.ico"
timeout = 20
toast = True

while(True):
    notification.notify(title= title,
                    message= msg,
                    app_icon = icon,
                    timeout= timeout,
                    toast=True)
    time.sleep(60*60) #hourly notification
    
    