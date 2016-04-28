# py-pinboard2html

This is a simple Python script to convert your [Pinboard](http://pinboard.in) bookmarks into the [standard HTML-ish bookmarks file format](http://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx).

## Usage

The script needs to know your Pinboard username and the associated API token. You can give it this information either by editing the Python script or by passing options to the script. In the former case, open `py-pinboard2html.py` in your favorite text editor and replace the values on lines 19 and 20 with your username and token.  You can then do

    python py-pinboard2html.py [output-file]

Output will go to stdout if you do not specify an output file name.

If you want to pass your username and password as command-line options, run the script like

    python py-pinboard2html.py -u username -t token [output-file]

If you take this approach you must specify *both* a username and a token on the command line. The `-u` and `-t` flags override the username and password set in the script file. Again, output will go to stdout if you do not specify an output file name.

## Version history

* 1.2 (2012-08-01)
	- This version no longer stores or accepts passwords, but rather uses the API tokens described in [this blog post](http://blog.pinboard.in/2012/07/api_authentication_tokens/). To use this version, obtain your token (something like "username:2AB96390C7DBE34") from [your Pinboard settings](http://pinboard.in/settings/password). The part after the colon is your API token, which can be set on line 20 of the script or passed in with the `-t` argument.
    - Don't overwrite an existing bookmarks file if we get a bad response from the server.
* 1.1 (2011-06-24): Changed my mind and renamed the project from pinboard2bookmarks to py-pinboard2html.
* 1.0 (2011-06-24): Initial release.

## Author

This script was written by [Benjamin Esham](https://esham.io).

This project is [hosted on GitHub](https://github.com/bdesham/py-pinboard2html). Please feel free to submit pull requests.

## License

Copyright © 2011–2012 Benjamin D. Esham. This program is released under the ISC license, which you can find in the file LICENSE.md.
