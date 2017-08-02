#import requests

#r=requests.post('http://35.176.110.188/upload',data={'data':'0x09,0x08,0x00,0x00'})

#print(r.status_code,r.reason)
#print(r.text)
#print(r)
import http.server

#filepath="temp.txt"

class Handler( http.server.BaseHTTPRequestHandler ):
    
    def do_GET( self ): # Reading
        if self.path=="/download":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            message = "Hello world!"
            print("Hello world!")
            self.wfile.write(bytes(message, "utf8"))
#            filehandle = open(filepath, "r")
#            self.wfile.write("Data:<br/><br>" + filehandle.read() + "\n\n")
#            filehandle.close()
        else:
            self.send_response(404)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            message = "Unknown Request"
            self.wfile.write(bytes(message, "utf8"))
    
    def do_POST( self ): # Updating the file
    
        if self.path=="/upload":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            
            #content_len = int(self.headers.getheader('content-length', 0))
            content_length = int(self.headers['Content-Length'])
            self.post_data = (self.rfile.read(content_length)).decode()
#            self.ParseData(self.post_data)

        else:
            self.send_response(404)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            self.wfile.write("Unknown request")
    
#    def ParseData(self,data):
#        global post_data
#        post_data=data
#        print(post_data)

httpd = http.server.HTTPServer( ('', 80), Handler )
#print("Hello world!")
httpd.serve_forever()
