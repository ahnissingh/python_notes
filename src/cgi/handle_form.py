#!/usr/bin/env python3
import cgi
import html

# Set the content type to be HTML
print("Content-type: text/html\n")

# Retrieve form data
form = cgi.FieldStorage()

# Get the 'name' and 'age' from the form data
name = form.getvalue("name", "Not Provided")
age = form.getvalue("age", "Not Provided")

# Print the HTML output
print(f"<html><body>")
print(f"<h1>Hello, {html.escape(name)}!</h1>")
print(f"<p>Your age is {html.escape(age)}.</p>")
print(f"</body></html>")
