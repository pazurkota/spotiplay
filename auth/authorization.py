import pkce, webbrowser
from http.server import HTTPServer
from api_data.request_handler import RequestHandler


# https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
class Authorization:
    CLIENT_ID = "d0e60eac862e474ba69236d407f6023a"
    REDIRECT_URL = "http://localhost:3000/callback"
    SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
    AUTH_URL = "https://accounts.spotify.com/authorize"
    CODE_CHALLENGE_METHOD = "S256"

    def __init__(self):
        self.code_verifier = pkce.generate_code_verifier(128)
        self.code_challenge = pkce.get_code_challenge(self.code_verifier)

    def get_authorization_url(self):
        return (
            f"{self.AUTH_URL}?response_type=code&client_id={self.CLIENT_ID}&redirect_uri={self.REDIRECT_URL}"
            f"&scope={self.SCOPE}&code_challenge_method={self.CODE_CHALLENGE_METHOD}&code_challenge={self.code_challenge}"
        )

    def request_user_authorization(self):
        auth_url = self.get_authorization_url()
        webbrowser.open(auth_url)

    def run_server(self):
        server_address = ('', 8080)
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.code_verifier = self.code_verifier
        httpd.serve_forever()
