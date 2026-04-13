import datetime
import requests
import pyjokes

def process_command(command):
    command = command.lower()

    # TIME
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {now}"

    # DATE
    elif "date" in command:
        today = datetime.date.today()
        return f"Today's date is {today}"

    # WEATHER (simple)
    elif "weather" in command:
        city = command.split(" ")[-1]
        try:
            url = f"https://wttr.in/{city}?format=3"
            res = requests.get(url).text
            return res
        except:
            return "Unable to fetch weather"

    # JOKE
    elif "joke" in command:
        return pyjokes.get_joke()

    # GOOGLE SEARCH
    elif any(word in command for word in ["search", "google"]):
        query = command

    # remove trigger words
        query = query.replace("search", "")
        query = query.replace("google", "")
        query = query.replace("for", "")

        query = query.strip()

        return f"https://www.google.com/search?q={query}"

    # WIKI BASIC
    elif "who is" in command or "what is" in command:
        return "Try searching on Google for detailed info"

    else:
        return "Sorry, I didn't understand that"