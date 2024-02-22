import tkinter as tk
from tkinter import font

codes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encoding_message(input_string):
    encoded_message = ""
    for i in input_string:
        i = i.lower()
        if i in codes:
            indexes = codes.index(i)
            en_indexes = (indexes + 3)
            encoded_char = codes[en_indexes]
            encoded_message += encoded_char
    return encoded_message
def decoding_message(encoded_message):
    decoded_message = ""
    for i in encoded_message:
        i = i.lower()
        if i in codes:
            indexes = codes.index(i)
            en_indexes = (indexes - 3) 
            decoded_char = codes[en_indexes]
            decoded_message += decoded_char
    return decoded_message
def encode_and_display():
    input_string = entry.get()
    encoded_message = encoding_message(input_string)
    result_label.config(text="Encoded Message: " + encoded_message)
def decode_and_display():
    encoded_message = entry.get()
    decoded_message = decoding_message(encoded_message)
    result_label.config(text="Decoded Message: " + decoded_message)
root = tk.Tk()
root.title("Encoder And Decoder")
root.geometry("450x450")
root.configure(bg="lightblue")
entry_label = tk.Label(root, text="Enter your message", bg="lightblue", fg="darkblue", font=("Helvetica", 12, "bold"))
entry_label.pack(pady=20)
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=10)
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)
button_font = font.Font(family="Helvetica", size=12)
encode_button = tk.Button(button_frame, text="Encode", command=encode_and_display, bg="white", fg="darkblue", font=button_font)
encode_button.pack(side=tk.LEFT, padx=5)
decode_button = tk.Button(button_frame, text="Decode", command=decode_and_display, bg="white", fg="darkblue", font=button_font)
decode_button.pack(side=tk.LEFT, padx=5)
result_label = tk.Label(root, text="", bg="lightblue", fg="darkblue", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)
root.mainloop()