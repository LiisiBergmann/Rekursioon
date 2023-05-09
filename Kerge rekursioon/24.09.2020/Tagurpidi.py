

def tagurpidi(list):

    if len(list) == 0:
        return list
    else:
        return tagurpidi(list[1:]) + [list[0]]

print(tagurpidi(["mesi", "kana", "jaanalind"]))