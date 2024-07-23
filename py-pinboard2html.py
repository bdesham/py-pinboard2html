#!/usr/bin/env python3

# py-pinboard2html
#
# Fetch your bookmarks from Pinboard and save them into an HTML bookmarks file
#
# Copyright (c) 2011-2012, 2024 Benjamin D. Esham. This program is released
# under the ISC license, which you can find in the file LICENSE.md.

import argparse
from contextlib import nullcontext
import html
import json
from sys import exit, stderr, stdout
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def printerr(message):
    print(message, file=stderr)


parser = argparse.ArgumentParser(
    description="Fetch your bookmarks from Pinboard and save them into an HTML bookmarks file."
)

parser.add_argument("--version", action="version", version="py-pinboard2html 2.0")
parser.add_argument("-u", dest="username", required=True, help="Your Pinboard username")
parser.add_argument(
    "-t",
    dest="token",
    required=True,
    help="Your Pinboard API token (shown at https://pinboard.in/settings/password)",
)
parser.add_argument(
    "output_file",
    metavar="OUTPUT_FILE",
    help='Filename for the HTML file, or "-" for standard output',
)

args = parser.parse_args()

token = args.username + ":" + args.token
url = f"https://api.pinboard.in/v1/posts/all?format=json&auth_token={token}"
try:
    with urlopen(url) as response:
        bookmarks = json.load(response)
except URLError as err:
    printerr(f"py-pinboard2html: Could not connect to Pinboard: {err.reason}")
    printerr("Please double-check your network connection.")
    exit(1)
except HTTPError as err:
    printerr(
        f"py-pinboard2html: The Pinboard server returned an error: HTTP {err.code} {err.reason}"
    )
    if err.code == 401:
        printerr("Please double-check your username and API token.")
    exit(1)

if args.output_file == "-":
    output_context = nullcontext(stdout)
else:
    output_context = open(args.output_file, "w")

with output_context as f:
    f.write('<html xmlns:NC="http://home.netscape.com/NC-rdf#">\n')
    f.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>\n')
    f.write("<dl>\n")
    for bookmark in bookmarks:
        escaped_url = html.escape(bookmark["href"])
        escaped_name = html.escape(bookmark["description"])
        f.write(f'<dt><a href="{escaped_url}">{escaped_name}</a></dt>\n')
    f.write("</dl>\n")
    f.write("</html>\n")
