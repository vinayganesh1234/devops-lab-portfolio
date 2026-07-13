from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Payment Processing Service</h1>
            <h2>Status: Running</h2>
            <p>Containerized with Docker</p>
            <p>Environment: Production</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    print('Server running on port 8080...')
    server.serve_forever()
