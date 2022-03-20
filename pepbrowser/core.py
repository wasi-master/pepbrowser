import requests

from rich_rst import RST
from rich.console import Console

from .cli import get_args

console = Console()

def get_content(pep_number, ext):
    url = f"https://raw.githubusercontent.com/python/peps/main/pep-{pep_number}.{ext}"
    with requests.get(url) as resp:
        if resp.status_code != 200:
            return None
        return resp.text

def main():
    args = get_args()
    with console.status("Getting pep content (1st try)"):
        content = get_content(args.pep, ext="txt")
    if content is None:
        with console.status("Getting pep content (2nd try)"):
            content = get_content(args.pep, ext="rst")
            if content is None:
                print("No pep found with the specified number")
    console.print(RST(content, code_theme=args.theme, show_errors=False))
