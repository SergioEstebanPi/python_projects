# https://stackoverflow.com/questions/70146543/is-webbrowsers-open-new-deprecated
# https://apple.stackexchange.com/questions/305901/is-it-possible-to-open-a-new-chrome-browser-window-from-terminal-with-multiple-s

import webbrowser as wb

def webauto():
    chrome_path = "open -na /Applications/Google\ Chrome.app --args --new-tab %s"
    URLS = (
        "stackoverflow.com",
        "github.com/SergioEstebanPi",
        "gmail.com",
        "youtube.com"
    )
    for url in URLS:
        print('open ' + url)
        wb.get(chrome_path).open(url)
    
webauto()