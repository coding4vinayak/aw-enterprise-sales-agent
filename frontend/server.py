#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse

# Port to serve on
PORT = 3000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Parse the URL and get the path
        url_parsed = urlparse(path)
        path = url_parsed.path

        # Check if the file exists
        full_path = os.path.join(self.directory or '.', path.lstrip('/'))
        
        # If the file doesn't exist and it's not a file with an extension,
        # serve index.html (for client-side routing)
        if not os.path.exists(full_path) and '.' not in os.path.basename(path):
            return os.path.join(self.directory or '.', 'public', 'index.html')
        
        return full_path

# Set the directory to serve from (public)
os.chdir('/workspaces/aw-enterprise-sales-agent/frontend/public')
    
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()