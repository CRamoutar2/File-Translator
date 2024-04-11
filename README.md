# File-Translator
Can translate pdfs or txt files from any language to any language.

To use:

- Download the repository ( Code > Download Zip ) or open the repo files with whatever method you please.

- Insert the files you want to be translated into the "To translate" folder.

- Run 'file translator.py' and follow the steps on the screen.

- After the Python file closes, navigate to the "Translated" folder and open your specified file.

- This file will always be in the form of a txt file.

__

Bugs: 

Will return an error when the code is confronted with abnormal characters and invisible spaces, but fixed by removing said character from the original file.

Can return an error about running into a NoneType, however, still check the resulting txt file to make sure that your requested translation is there.

The resulting file is specified to always be a txt file because of issues writing to a PDF file. 
