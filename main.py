    import os 
    import webbrowser
    import time

    url = 'https://www.youtube.com/watch?v=tHYy5LhDqdw'

    seconds = 5
    views = 5
    counter = 0
    while counter != views:
        webbrowser.open(url)
        time.sleep(seconds) 
        os.system("taskkill /im chrome.exe /f")  
        counter+=1