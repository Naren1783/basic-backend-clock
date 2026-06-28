from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import json

class SimpleClockAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        current_moment = datetime.now()
        time_string = current_moment.strftime("%I:%M:%S %p")

        response_payload = {"time": time_string}
        self.wfile.write(json.dumps(response_payload).encode('utf-8'))

print("Server is awake! Ticking away at http://localhost:3000 ⏰")
HTTPServer(('localhost', 3000), SimpleClockAPI).serve_forever()