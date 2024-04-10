import tkinter as tk
import sounddevice as sd
import numpy as np

def measure_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    volume_int = int(volume_norm)
    volume_label.config(text=str(volume_int))

root = tk.Tk()
root.title("Измерение громкости микрофона")

volume_label = tk.Label(root, text="0", font=("Helvetica", 48))
volume_label.pack()

sample_rate = 44100
block_size = 1024
stream = sd.InputStream(callback=measure_volume, channels=1, samplerate=sample_rate, blocksize=block_size)
stream.start()

root.mainloop()
stream.stop()
