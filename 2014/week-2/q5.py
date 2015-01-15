#!/usr/bin/python3
import re
import urllib.parse

markup_file = open("post.md").read()
references = re.findall("\[(.*)\]:\s+(.*)",markup_file)
markup_file = re.sub("\[(.*)\]:\s+(.*)","",markup_file)
for reference in references:
	mod = urllib.parse.urljoin("https://google.com",reference[1],True)
	parts = urllib.parse.urlsplit(mod)
	if parts.scheme or parts.netloc:
		markup_file = re.sub("\["+re.escape(reference[0])+"\]","("+mod+")",markup_file)

matches = re.findall("\[.*?\]\s*\(\s*([^)\s]+)\s*\)",markup_file)
fragments = []
for match in matches:
	fragment = urllib.parse.urlparse(match).fragment
	if fragment:
		fragments.append(fragment)
if (fragments):
	print(" ".join(fragments))

