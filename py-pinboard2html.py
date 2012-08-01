#!/usr/bin/python

# py-pinboard2html
# 
# Convert your Pinboard bookmarks into an HTML bookmarks file
#
# (c) Benjamin Esham, 2011-12.  See the accompanying README.md for this file's
# license and other information.

import json, os, sys, subprocess

#
# Replace the following two strings with your login credentials:
#

username = "username"
password = "hunter2"

#
# OK! Leave the rest of the script alone ;-)
#


# print version and help information

script_version = "1.2"

def version_text():
	old_out = sys.stdout
	sys.stdout = sys.stderr

	print "py-pinboard2html", script_version
	print "(c) 2011-12, Benjamin Esham"
	print "https://github.com/bdesham/py-pinboard2html"

	sys.stdout = old_out

def help_text():
	version_text()

	old_out = sys.stdout
	sys.stdout = sys.stderr

	print
	print "usage: python py-pinboard2html.py [-u username -p password] [output-file]"

	sys.stdout = old_out


# functions

# html escaping code from http://wiki.python.org/moin/EscapingHtml

html_escape_table = {
	"&": "&amp;",
	'"': "&quot;",
	"'": "&#39;",
	">": "&gt;",
	"<": "&lt;",
	}

def html_escape(text):
	return ''.join(html_escape_table.get(c, c) for c in text)

def sanitize(string):
	res = ''
	string = html_escape(string)

	for i in range(len(string)):
		if ord(string[i]) > 127:
			res += '&#x%x;' % ord(string[i])
		else:
			res += string[i]

	return res

def html_bookmarks(bookmarks):
	return ''.join(html_bookmark(b) for b in bookmarks)

def html_bookmark(bookmark):
	return "<dt><a href=\"%s\">%s</a></dt>\n" % \
			(sanitize(bookmark['href']), sanitize(bookmark['description']))


# parse command-line arguments

args = sys.argv[1:]

if "-v" in args or "--version" in args:
	version_text()
	sys.exit(1)

if len(args) not in [0, 1, 4, 5] or "-h" in args or "--help" in args:
	help_text()
	sys.exit(2)

if "-u" in args and "-p" in args:
	ind = args.index("-u")

	try:
		username = args[ind+1]
	except IndexError, e:
		help_text()
		sys.exit(2)

	args.pop(ind)
	args.pop(ind)
	
	try:
		# wrap this in a try block in case we got something like "-u -p"
		ind = args.index("-p")
	except ValueError, e:
		help_text()
		sys.exit(2)

	try:
		password = args[ind+1]
	except IndexError, e:
		help_text()
		sys.exit(2)
	
	args.pop(ind)
	args.pop(ind)
elif "-u" in args or "-p" in args:
	# user gave a username but not a password, or vice versa
	help_text()
	sys.exit(2)

# get the data from pinboard

pipe = subprocess.Popen(["curl", "-s", "-u", "%s:%s" % (username, password), \
		"https://api.pinboard.in/v1/posts/all?format=json"], \
		stdout = subprocess.PIPE)
data = pipe.communicate()[0]

if len(data) == 0:
	print >> sys.stderr, "py-pinboard2html: Pinboard response was empty."
	sys.exit(1)

try:
	bookmarks = json.loads(data)
except ValueError, e:
	print >> sys.stderr, "py-pinboard2html: error parsing JSON. " + \
			"Did you enter the right password?"
	print >> sys.stderr, e
	sys.exit(1)

# write out the html file

if len(args):
	try:
		out = open(os.path.expanduser(args[0]), 'w')
	except IOError, e:
		print >> sys.stderr, "py-pinboard2html: error opening the output file."
		print >> sys.stderr, e
		sys.exit(1)
	output_to_file = True
else:
	out = sys.stdout
	output_to_file = False

print >> out, '<html xmlns:NC="http://home.netscape.com/NC-rdf#">'
print >> out, '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>'
print >> out, "<dl>\n%s</dl>" % html_bookmarks(bookmarks)
print >> out, '</html>'

# clean up

if output_to_file:
	out.close()
