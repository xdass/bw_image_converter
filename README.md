Exercise
In order to get comfortable with ProcessPoolExecutors, I suggest you try to write a program that creates
black and white versions of a large number of different photos. For this task, I recommend you
download Pillow, which is a fork of the Python Imaging Library.
Image processing is computationally expensive, as each pixel within the image has to be processed and
recalculated when converting to black and white.
The main requirements are as follows:
The process must utilize the ProcessPoolExecutor class
The project should be able to process multiple images in parallel, but ensure it does not process the
same image on two different processes