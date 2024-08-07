from http.server import BaseHTTPRequestHandler
import requests
import urllib.parse


class RequestHandler(BaseHTTPRequestHandler):
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    REDIRECT_URI = "http://localhost:3000/callback"
    CLIENT_ID = "d0e60eac862e474ba69236d407f6023a"

    def get_handler(self):
        if self.path.startswith("/callback"):
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            code = query_components.get("code")[0]
            token_response = requests.post(
                self.TOKEN_URL,
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": self.REDIRECT_URI,
                    "client_id": self.CLIENT_ID,
                    "code_verifier": self.server.code_verifier,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            token_json = token_response.json()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(token_json), "utf-8"))
            return
