# py-pinboard2html

This is a simple Python script to download your [Pinboard](https://pinboard.in) bookmarks and write them in the [standard HTML-ish bookmarks file format](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753582%28v=vs.85%29).

## Usage

This script requires Python 3.7 or later.

The script can be invoked like

    python3 py-pinboard2html.py -u USERNAME -t TOKEN OUTPUT_FILE

Here `USERNAME` is your Pinboard username, `TOKEN` is your Pinboard API token (shown in [the “password” section of your Pinboard preferences][password]), and `OUTPUT_FILE` is the filename where the bookmarks should be saved. Specifying `-` as the `OUTPUT_FILE` will print the HTML to the standard output.

[password]: https://pinboard.in/settings/password

## Version history

* 2.0 (2024-07-22)
    - The script has been completely rewritten. It now requires Python 3.7 or later.
    - Hard-coding the username and password in the script file is no longer supported. The `-u` and `-t` command-line arguments are now mandatory.
    - The `OUTPUT_FILE` command-line argument is now mandatory. If you want to send the output to the standard output, you must now supply a value of `-` for `OUTPUT_FILE` instead of omitting the argument.
    - Non-ASCII characters are no longer HTML-escaped in the output. (HTML special characters are, of course, still escaped.)
    - The script no longer expands `~` in the `OUTPUT_FILE` argument into a reference to the home directory. This was always a misfeature; this kind of expansion is done by the shell and generally should not be done by other programs.
* 1.2 (2012-08-01)
	- This version no longer stores or accepts passwords, but rather uses the API tokens described in [this blog post](https://blog.pinboard.in/2012/07/api_authentication_tokens/). To use this version, obtain your token (something like "username:2AB96390C7DBE34") from [your Pinboard settings](https://pinboard.in/settings/password). The part after the colon is your API token, which can be set on line 20 of the script or passed in with the `-t` argument.
    - Don't overwrite an existing bookmarks file if we get a bad response from the server.
* 1.1 (2011-06-24): Changed my mind and renamed the project from pinboard2bookmarks to py-pinboard2html.
* 1.0 (2011-06-24): Initial release.

## Author

This script was written by [Benjamin Esham](https://esham.io).

This project is [hosted on GitHub](https://github.com/bdesham/py-pinboard2html). Please feel free to submit pull requests.

## License

Copyright © 2011–2012, 2024 Benjamin D. Esham. This program is released under the ISC license, which you can find in the file LICENSE.md.
