#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import query_eval
#import pri

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #try:
        if 'search' not in self.path:
        	return
    	qs = urlparse.urlparse(self.path)
    	print self.path
    	args = urlparse.parse_qs(qs.query)
    	print args
    	self.send_response(200)
    	self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8091')
    	self.end_headers()
    	self.wfile.write(query_eval.query_eval(args['q'][0], int(args['m'][0]), int(args['o'][0]), args['sb'][0], args['titles'][0]))
    	return    
    	#except Exception, e:
        self.send_error(500,'Fuck, something went wrong!<br>' + e.strerr)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

def main():
    try:
        server = HTTPServer(('', 8090), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
