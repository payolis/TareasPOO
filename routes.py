from views.vistas import home_view, tareas_view, recordatorios_view

def setup_routes(page):
    page.add_route("/", home_view)
    page.add_route("/tareas", tareas_view)
    page.add_route("/recordatorios", recordatorios_view)
