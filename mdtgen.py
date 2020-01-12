#!/usr/bin/python3
# simple markdown post template generator
import sys
from datetime import datetime

post_directory = "_posts/"

def get_name_of_article(argument, char):
    argument_o = ""
    for i in argument[1:]:
        if i==argument[-1]:
            argument_o+=i
        else:
            argument_o+=i+char
    return argument_o




name_of_file = str(datetime.today().strftime('%Y-%m-%d')) + "-" + get_name_of_article(sys.argv,"-") + ".md"
try:
    with open(post_directory+name_of_file, "w") as stream:
        stream.write("---")
        stream.write("\nlayout: post")
        stream.write(f"\ntitle: \"{get_name_of_article(sys.argv,' ')}\"")
        stream.write(f"\ndate: {str(datetime.today().strftime('%Y-%m-%d'))}")
        stream.write("\ncategories:")
        stream.write("\n---")
        stream.close()
        print("[+]Post generated")
except:
    print("[-]An error occured")
# print(get_name_of_article(sys.argv,"_"))
