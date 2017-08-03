#import http.server
#from threading import thread
#
##filepath="temp.txt"
#
#class Handler( http.server.BaseHTTPRequestHandler ):
#    
#    def do_GET( self ): # Reading
#        if self.path=="/download":
#            self.send_response(200)
#            self.send_header( 'Content-type', 'text/html' )
#            self.end_headers()
#            message = "Hello world!"
#            print("Hello world!")
#            self.wfile.write(bytes(message, "utf8"))
#            
#        else:
#            self.send_response(404)
#            self.send_header( 'Content-type', 'text/html' )
#            self.end_headers()
#            message = "Unknown Request"
#            self.wfile.write(bytes(message, "utf8"))
#    
#    def do_POST( self ): # Updating the file
#    
#        if self.path=="/upload":
#            self.send_response(200)
#            self.send_header( 'Content-type', 'text/html' )
#            self.end_headers()
#            
#            #content_len = int(self.headers.getheader('content-length', 0))
#            content_length = int(self.headers['Content-Length'])
#            self.post_data = (self.rfile.read(content_length)).decode()
#            print(self.post_data)
##            self.ParseData(self.post_data)
#
#        else:
#            self.send_response(404)
#            self.send_header( 'Content-type', 'text/html' )
#            self.end_headers()
#            self.wfile.write("Unknown request")
#    
#
#httpd = http.server.HTTPServer( ('', 80), Handler )
#httpd.serve_forever()




import http.server

class Handler( http.server.BaseHTTPRequestHandler):

    
    def do_GET( self ): # Reading
        if self.path=="/download":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            message = "Hello world!"
            print("Hello world!")
            self.wfile.write(bytes(message, "utf8"))
            
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
            
            file_handle = open("Receiver_Output.txt", "w")
            file_handle.write( self.post_data)
            file_handle.close()
            
            print(self.post_data)
#            self.ParseData(self.post_data)
        elif self.path=="/upload2":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            
            #content_len = int(self.headers.getheader('content-length', 0))
            content_length = int(self.headers['Content-Length'])
            self.post_data = (self.rfile.read(content_length)).decode()
            file_handle = open("Receiver_Output2.txt", "w")
            file_handle.write( self.post_data)
            file_handle.close()
            
            print(self.post_data)
#            self.ParseData(self.post_data)

        else:
            self.send_response(404)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            self.wfile.write("Unknown request")

httpd = http.server.HTTPServer( ('', 80), Handler )
httpd.serve_forever()