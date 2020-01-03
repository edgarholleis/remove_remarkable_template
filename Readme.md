# remove_remarkable_template

This is script to remove the ReMarkable template or background from a PDF downloaded from the remarkable. It uses the Python *pdfrw* library to walk the PDF datastructure and replace those parts that represent the page's template with the corresponding part of the *blank* template.

Usage:

     remove_remarkable_template.py in.pdf out.pdf

