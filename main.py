from aiohttp import web

from app import migrations


def setup_routes(applicaion) -> None:
    from app.notes.routes import get_routes as notes_routes
    from app.users.routes import get_routes as auth_routes
    routes = [*auth_routes(), *notes_routes()]
    applicaion.add_routes(routes)


if __name__ == "__main__":
    # migrations.migrate()
    app = web.Application()
    setup_routes(app)
    web.run_app(app)
