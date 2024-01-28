import requests

from rich_rst import RST
from rich.console import Console

from .cli import get_args

console = Console()

def get_content(pep_number, ext):
    # Construct the URL for the PEP document
    url = f"https://raw.githubusercontent.com/python/peps/main/peps/pep-{pep_number}.{ext}"

    # Make a GET request to the URL
    with requests.get(url) as resp:
        # If the response status code is not 200 (OK), return None
        if resp.status_code != 200:
            return None
        # If the response status code is 200, return the text of the response
        return resp.text

def main():
    # Get command line arguments
    args = get_args()

    # Try to get the PEP content in text format
    with console.status("Getting pep content (1st try)"):
        content = get_content(args.pep, ext="txt")

    # If the content is not found, try to get it in reStructuredText format
    if content is None:
        with console.status("Getting pep content (2nd try)"):
            content = get_content(args.pep, ext="rst")

            # If the content is still not found, print an error message
            if content is None:
                print(f"No pep found with the specified number ({args.pep})")
                return

    # Print the PEP content with syntax highlighting
    console.print(RST(content, code_theme=args.theme, default_lexer="python", show_errors=False))
