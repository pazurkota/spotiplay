import typer
from api_data import authorization as auth

def main(name: str):
    print(f"Hello, {name}")


if __name__ == "__main__":
    auth.Authorization.request_user_authorization(auth.Authorization())

