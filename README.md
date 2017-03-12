# Pixel2ANSI
__pixel2ANSI__ - is simple python-script that can transform simple pixel png image to ANSI escape codes for show it in terminal.
It is very simple!

Script takes one of two parametres from terminal and returns file with escape code. Command will be looks some like this:
```Bash
$ ./p2A.py [image_name] [result_file name]
```
Where `image_name` is is required parametr, that specifies the chosen image to the program.
And second parametr is optional. It specifies the name of the result file. By default it will be like `image_name`_result.


:grey_exclamation: For working you need to install [Pillow](https://pillow.readthedocs.io) library.


Now it can work with all 8 Bit colors. Detailed list of supported colors you can see [here] (https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg).
