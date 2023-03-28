import datetime
import logging
import http.server
import os
import socketserver
import log_conf

logger = logging.getLogger('server')
PORT = int(os.getenv('SERVER_PORT', 8000))


class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            response = f"Server time: {str(datetime.datetime.now())}"
            self.wfile.write(response.encode('utf-8'))
            self.wfile.flush()
            logger.info(self.headers)
        except:
            logger.exception('Произошла ошибка')


Handler = HTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    logger.info(f"Serving at port {PORT}")
    httpd.serve_forever()



