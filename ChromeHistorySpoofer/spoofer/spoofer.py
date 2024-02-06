import random
import webbrowser
import time
import subprocess

i = 0

killchrome = input("Should the application kill chrome after its done (Windows Only!) (false / true): ")
sleep = input("How long should the program sleep between inputs? (Recommended 2-5): ")
times = input("How many times should the program spoof the URL?: ")
url = input("URL to spoof to? (Say 'Pluster' for default URL): ")
realUrl = url

while i < int(times):
    if realUrl == "Pluster":
        url = "https://www.google.com/search?q=HISTORY+SPOOFED+BY+PLUSTER+" + str(random.randint(0,999)) + "+SPOOFER&oq=HISTORY+SPOOFED+BY+PLUSTER+SPOOFER+" + str(random.randint(0, 999)) + "&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiiBDIHCAIQABiiBDIHCAMQABiiBDIHCAQQABiiBDIHCAUQABiiBNIBCTEwNDU0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
    time.sleep(float(sleep))
    webbrowser.open(url)
    i += 1

if killchrome == "true":
    chrome_close_command = "taskkill /f /im chrome.exe"
    subprocess.run(chrome_close_command, shell=True)




    