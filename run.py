#!/home/webuser/venv/bin/python3
# -*- coding: utf-8 -*-

import mistune
import argparse
import http.server
import socketserver
import os

def generate():
    infile = open('./source/resume.md', 'r', encoding='utf-8')
    text = infile.read()
    infile.close()
    
    css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><link rel="stylesheet" href="./style/style.css">'''
    
    md = mistune.Markdown()
    html = md(text)
    
    outfile = open('./docs/index.html', 'w', encoding='utf-8')
    outfile.write('<html><head>' + css + '</head><body>' + html + '</body></html>')
    outfile.close()
    print("static files are generated is ./docs folder")

def serve():
    port = 8080
    web_dir = os.path.join(os.path.dirname(__file__), 'docs')
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print('serving at port:', port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.shutdown()
    httpd.server_close()


def hello():
    print('hello resume!!')

if __name__ == '__main__':
    func_list = [hello, generate, serve]
    func_name = [f.__name__ for f in func_list]
    func_dict = dict(zip(func_name, func_list))

    parser = argparse.ArgumentParser()
    parser.add_argument('func',  help='please specify the task to do', choices=func_name)
    args = parser.parse_args()
    f = func_dict[args.func]
    f()

