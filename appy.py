import flet as ft
from routes import setup_routes

def main(page: ft.Page):
    setup_routes(page)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)