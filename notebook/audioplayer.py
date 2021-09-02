from IPython.display import Audio

def play(filename):
    try:
        return Audio(f"../recording/{filename}", autoplay=False)
    except ValueError:
        return "Please check the presence of audio file under recording folder (or) audio file name and extenstion"