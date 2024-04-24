def estimate_reading_time(text):
    if text == "":
        raise Exception("Can't estimate reading time for empty text")
    words = text.split()
    count = len(words) / 200
    return count 