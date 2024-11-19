import tkinter as tk
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source)
            text = recognizer.recognize_google(audio_data)
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, text)
        except sr.UnknownValueError:
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, "Speech Unrecognizable")
        except sr.RequestError:
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, "Request Failed")

app = tk.Tk()
app.title('Speech to Text')

text_output = tk.Text(app, height=10, width=50)
text_output.pack()

recognize_button = tk.Button(app, text='Speak and Recognize', command=recognize_speech)
recognize_button.pack()

app.mainloop()