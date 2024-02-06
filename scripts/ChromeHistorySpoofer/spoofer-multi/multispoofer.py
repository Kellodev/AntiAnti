# please add the URLS that would be good for the reason you might be using pluster:)
# add like ALOT of diffrent urls, like typos in normal stuff etc. because if you dont it wont add them to history

import random, webbrowser, time

i = 0

sleep = input("How long should the program sleep between inputs? (Recommended 2-5): ")
times = input("How many times should the program spoof the URL?: ")
# i suggest adding 10-20 urls, im too lazy to do so:D
urls = [
    'https://classroom.google.com/',
    # just the google link of searching "classroom"
    'https://www.google.com/search?q=classroom&oq=classroom&gs_lcrp=EgZjaHJvbWUyEQgAEEUYORhDGIMBGLEDGIoFMgkIARAAGEMYigUyEwgCEC4YgwEYrwEYxwEYsQMYgAQyDAgDEAAYQxixAxiKBTINCAQQABiDARixAxiABDIHCAUQABiABDIHCAYQABiABDIGCAcQRRg8qAIAsAIA&sourceid=chrome&ie=UTF-8'
]
while i < int(times):
    url = random.choice(urls)
    
    time.sleep(float(sleep))
    webbrowser.open(url)
    i += 1