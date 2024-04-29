def get_most_common_letter(text):
    counter = {}
    non_spaced_text = text.replace(" ", "")
    for char in non_spaced_text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")