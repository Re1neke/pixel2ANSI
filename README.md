# Pixel2ANSI
__pixel2ANSI__ - is tiny python-script translates image into chain of ANSI escape sequences for show it in terminal.
It's very simple!

![pixel2ansi](https://user-images.githubusercontent.com/17577699/49805152-1ae80800-fd5d-11e8-9c1b-8ffa0af90504.png)

Script takes one or two arguments from terminal and in result creates file with code, that shell can interpret. Command will be looks some like this:
```Bash
$ ./p2A.py octocat.png octocat.txt
```
Where `octocat.png` is required argument, that specifies a chosen image to the program. You can test it with picture of octocat which included in repository. ☺️
And second argument is optional. It specifies the name of the result file. By default it will be like `octocat_result` for our test picture.
