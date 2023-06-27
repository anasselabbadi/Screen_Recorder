import tkinter as tk
from tkinter import filedialog
import cv2
import pyautogui
import numpy as np
import threading
import PIL.Image, PIL.ImageTk

class ScreenRecorderGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Recorder")
        self.root.geometry("400x400")

        # Configure dark mode
        self.dark_mode = False
        self.root.configure(bg="white")
        self.root.option_add("*foreground", "black")
        self.root.option_add("*background", "white")

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording, width=15, height=2, relief=tk.RAISED)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED, width=15, height=2, relief=tk.RAISED)
        self.stop_button.pack(pady=10)

        self.dark_mode_button = tk.Button(self.root, text="Dark Mode", command=self.toggle_dark_mode, width=15, height=2, relief=tk.RAISED)
        self.dark_mode_button.pack(pady=10)

        self.preview_label = tk.Label(self.root)
        self.preview_label.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.recording = False
        self.preview_thread = None

    def start_recording(self):
        self.recording = True

        # Disable start button and enable stop button
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Create a thread for recording
        recording_thread = threading.Thread(target=self.record_screen)
        self.preview_thread = threading.Thread(target=self.update_preview)
        recording_thread.start()
        self.preview_thread.start()

    def stop_recording(self):
        self.recording = False

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.root.configure(bg="black")
            self.root.option_add("*foreground", "white")
            self.root.option_add("*background", "black")

            self.start_button.config(bg="gray25", fg="white")
            self.stop_button.config(bg="gray25", fg="white")
            self.dark_mode_button.config(bg="gray25", fg="white")

            self.preview_label.config(bg="gray25", fg="white")
        else:
            self.root.configure(bg="white")
            self.root.option_add("*foreground", "black")
            self.root.option_add("*background", "white")

            self.start_button.config(bg="SystemButtonFace", fg="black")
            self.stop_button.config(bg="SystemButtonFace", fg="black")
            self.dark_mode_button.config(bg="SystemButtonFace", fg="black")

            self.preview_label.config(bg="white", fg="black")

    def record_screen(self):
        # Define the screen resolution
        screen_width, screen_height = pyautogui.size()

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_file = filedialog.asksaveasfilename(defaultextension='.mp4')
        out = cv2.VideoWriter(output_file, fourcc, 20.0, (screen_width, screen_height))

        while self.recording:
            # Capture the screen image
            img = pyautogui.screenshot()

            # Convert the image to a numpy array representation
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # Write the frame to the output video file
            out.write(frame)

        # Release the VideoWriter and destroy any OpenCV windows
        out.release()
        cv2.destroyAllWindows()

        # Enable start button and disable stop button after recording is stopped
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_preview(self):
        while self.recording:
            # Capture the screen image
            img = pyautogui.screenshot()

            # Convert the image to a PIL Image object
            img_pil = PIL.Image.fromarray(np.array(img))

            # Resize the image to fit the preview window
            img_pil = img_pil.resize((360, 240), PIL.Image.LANCZOS)

            # Convert the PIL Image to a PhotoImage object
            img_tk = PIL.ImageTk.PhotoImage(img_pil)

            # Update the label with the new image
            self.preview_label.config(image=img_tk)
            self.preview_label.image = img_tk

    def on_closing(self):
        if self.recording:
            self.recording = False
            self.root.after(100, self.on_closing)
        else:
            self.root.destroy()

    def run(self):
        self.root.mainloop()

# Create an instance of the ScreenRecorderGUI and run the application
gui = ScreenRecorderGUI()
gui.run()
