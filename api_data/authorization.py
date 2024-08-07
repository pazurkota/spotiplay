import pkce, webbrowser
import requests as req


# https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
class Authorization:
    CLIENT_ID = "d0e60eac862e474ba69236d407f6023a"
    REDIRECT_URL = "http://localhost:3000"
    SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
    RESPONSE_TYPE = "code"
    STATE = "34fFs29kd09"
    CODE_CHALLENGE_METHOD = "S256"

    @staticmethod
    def get_code_verifier():
        return pkce.generate_code_verifier(128)

    @staticmethod
    def get_code_challenge(code_verifier):
        return pkce.get_code_challenge(code_verifier)

    def request_user_authorization(self):
        code_verifier = self.get_code_verifier()
        code_challenge = self.get_code_challenge(code_verifier)
        auth_url = (
            f"https://accounts.spotify.com/authorize?client_id={self.CLIENT_ID}"
            f"&response_type={self.RESPONSE_TYPE}"
            f"&redirect_uri={self.REDIRECT_URL}"
            f"&code_challenge_method={self.CODE_CHALLENGE_METHOD}"
            f"&code_challenge={code_challenge}"
            f"&state={self.STATE}"
            f"&scope={self.SCOPE}"
        )

        webbrowser.open(auth_url)
        return code_verifier
