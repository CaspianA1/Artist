# encoding: utf-8

import get_links as gl
import get_ascii_image as ga
import formatting as frm
import os
import sys

frm.clear_screen()

query = gl.get_query()

query_link = gl.get_link(query)


color_response = ga.get_color()

frm.drawing_msg()

ga.get_ascii(color_response, query_link)

os.system("cat art.txt")
