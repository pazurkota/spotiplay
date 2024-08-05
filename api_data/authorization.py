import pkce


# https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
class Authorization:
    # spotiplay public client id
    CLIENT_ID = "d0e60eac862e474ba69236d407f6023a"

    @staticmethod
    def get_code_verifier():
        return pkce.generate_code_verifier(128)

    @staticmethod
    def get_code_challenge():
        return pkce.get_code_challenge(Authorization.get_code_challenge())
