import flet as ft

def home_view(page):
    page.views.clear()
    page.views.append(ft.View(
        controls=[
            ft.Text("Bienvenido a la lista de tareas y recordatorios"),
            ft.NavigationLink("/tareas", "Tareas"),
            ft.NavigationLink("/recordatorios", "Recordatorios")
        ]
    ))

def tareas_view(page):
    page.views.clear()
    page.views.append(ft.View(
        controls=[
            ft.Text("Lista de Tareas"),
            ft.TextButton("Agregar Tarea", on_click=lambda e: page.go("/agregar_tarea"))
        ]
    ))

def recordatorios_view(page):
    page.views.clear()
    page.views.append(ft.View(
        controls=[
            ft.Text("Lista de Recordatorios"),
            ft.TextButton("Agregar Recordatorio", on_click=lambda e: page.go("/agregar_recordatorio"))
        ]
    ))
