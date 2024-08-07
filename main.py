import typer
from api_data.authorization import Authorization

def main(name: str):
    print(f"Hello, {name}")


if __name__ == "__main__":
    auth = Authorization()
    auth.request_user_authorization()
    auth.run_server()
