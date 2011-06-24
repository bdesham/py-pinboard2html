# py-pinboard2html

This is a simple Python script to convert your [Pinboard](http://pinboard.in) bookmarks into the [standard HTML-ish bookmarks file format](http://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx).

This script was written by [Benjamin Esham](http://www.bdesham.info) ([e-mail](mailto:bdesham@gmail.com)). The project page is [hosted on GitHub](https://github.com/bdesham/py-abemails).

## Usage

The script needs to know your Pinboard username and password. You can give it this information either by editing the Python script or by passing options to the script. In the former case, open `py-pinboard2html.py` in your favorite text editor and replace the values on lines 16 and 17 with your username and password.  You can then do

    python py-pinboard2html.py [output-file]

Output will go to stdout if you do not specify an output file name.

If you want to pass your username and password as command-line options, run the script like

    python py-pinboard2html.py -u username -p password [output-file]

If you take this approach you must specify *both* a username and a password on the command line. The `-u` and `-p` flags override the username and password set in the script file. Again, output will go to stdout if you do not specify an output file name.

## Version history

* 1.1 (2011-06-24): Changed my mind and renamed the project from pinboard2bookmarks to py-pinboard2html.
* 1.0 (2011-06-24): Initial release.

## License

Copyright © 2011, Benjamin Esham.  This software is released under the following version of the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following condition: the above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.**
