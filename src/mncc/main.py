import click

import requests
import time

from rich import print
from rich.console import Console


c = Console()


@click.command()
@click.option("-u", "--user_id", type=int, help="user id", required=True)
@click.option("-t", "--t_id", type=int, help="thread id for your chat")
@click.option("-r", "--role", default="user", help="chat content")
@click.option("-cct", "--config_client_type", help="config the ai client type, from client side")
@click.argument("content")
def chat(content, *, user_id, t_id, role, config_client_type):
    response = requests.post(
        "http://100.99.103.12:5010/chat",
        json={"user_id": user_id, "t_id": t_id, "client_type": config_client_type, "content": content},
        stream=True,
    )

    for line in response.iter_lines():
        if line:
            time.sleep(0.01)

            c.print(line.decode("utf8"), style="#93c47d")
            # print("1", end="", flush=True)
            # print(line.decode("utf8"), flush=True)


if __name__ == "__main__":
    chat()

# for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
#     if chunk:
#         time.sleep(1)
#         print(chunk, end="")
