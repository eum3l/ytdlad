import os

x = True
while x:
    url = input('? ')
    if url.lower() == "exit":
        x = False
    else:
        os.system(f"youtube-dl {url}")

