from IPython.display import Audio

def play(filename):
    return Audio(f"./recording/{filename}", autoplay=True)