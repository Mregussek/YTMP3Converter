class text(object):
    def __init__(self):
        self.textToChange = "None"

    def setTextToChange(self, text):
        self.textToChange = text

    def setYtUrl(self):
        url = "https://www.youtube.com/watch?v="
        returnUrl = url + self.textToChange
        return returnUrl
