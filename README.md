# Screen_Recorder
code is a Python implementation of a screen recording application using the tkinter library.
the code is Python implementation of a screen recording application using the tkinter library for creating the graphical user interface (GUI) and other libraries such as OpenCV, pyautogui, numpy, and PIL for screen capturing, video processing, and image manipulation.

The application features a simple GUI with three buttons: "Start Recording," "Stop Recording," and "Dark Mode." The "Start Recording" button initiates the screen recording process, while the "Stop Recording" button stops the recording. The "Dark Mode" button allows the user to switch between light and dark themes.

When the "Start Recording" button is clicked, a separate thread is created to continuously capture the screen using the pyautogui library. The captured screen frames are then converted into a numpy array and written to an output video file using OpenCV's VideoWriter object.

Simultaneously, another thread updates a preview window, which displays the real-time screen capture using tkinter's Label widget. The captured screen frames are converted into a PIL Image object, resized to fit the preview window, and then displayed in the tkinter interface.

The "Stop Recording" button terminates the recording thread and stops writing frames to the output video file. The "Dark Mode" button toggles between a light and dark theme for the GUI, modifying the background color and text color of the tkinter window and buttons.

The application also handles the closing of the tkinter window by implementing the "WM_DELETE_WINDOW" protocol. If recording is in progress, it stops the recording and waits for a brief period before attempting to close the window again. Once the recording is stopped, the tkinter window is destroyed.

To use this application, you need to have the required libraries (tkinter, OpenCV, pyautogui, numpy, and Pillow) installed in your Python environment. Running the code will launch the screen recording application, allowing you to start and stop recording your screen and preview the capture in real time.
