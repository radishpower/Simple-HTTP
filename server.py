import BaseHTTPServer
import httplib
import urlparse
import shutil
import mimetypes

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_GET(self):
	action = 'home.html'
	resp = open(action, 'r')
	resp.seek(0, 2)
	resplen = resp.tell()
	resp.seek(0, 0)
	self.send_response(httplib.OK)
	self.send_header('Content-Type', mimetypes.guess_type(action))
	self.send_header('Content-Length', resplen)
	self.end_headers()
	shutil.copyfileobj(resp, self.wfile)
	self.wfile.close()

def main(args):
  if len(args) > 1:
    port = int(args[1])
  else:
    port = 8000
  server_address = ('', port)
  httpd = BaseHTTPServer.HTTPServer(server_address, RequestHandler)
  httpd.serve_forever()

if __name__ == '__main__':
  import sys
  main(sys.argv)
