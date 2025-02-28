import requests
from rich import print as printf
from rich.panel import Panel
from rich.console import Console

console = Console()

banner = Panel(
    "[bold yellow]FACEBOOK AUTO COMMENT SCRIPT[/bold yellow]", 
    width=60, 
    title="[bold cyan]Auto Comment Bot[/bold cyan]", 
    border_style="blue",
    expand=False
)
console.print(banner)

access_token = input("\nEnter your access token: ")
post_id = input("Enter your post ID: ")
comment_message = input("Enter comment message: ")
comment_limit = int(input("Enter comment limit: "))

comment_url = f'https://graph.facebook.com/{post_id}/comments'

def post_comment(message, access_token):
    data = {
        'message': message,
        'access_token': access_token
    }
    response = requests.post(comment_url, data=data)
    return response

console.print("\n[bold yellow]Processing...[/bold yellow]\n")

for i in range(comment_limit):
    response = post_comment(comment_message, access_token)
    if response.status_code == 200:
        console.print(Panel(f'[green]Comment {i+1} posted successfully.[/green]', width=60, border_style="green"))
    else:
        console.print(Panel(f'[red]Error posting comment {i+1}: {response.status_code} {response.text}[/red]', width=60, border_style="red"))
