from aiohttp import web


def setup_routes(applicaion) -> None:
    from app.notes.routes import get_routes as notes_routes
    from app.users.routes import get_routes as auth_routes
    routes = [*auth_routes(), *notes_routes()]
    app.add_routes(routes)


if __name__ == "__main__":
    app = web.Application()
    setup_routes(app)
    web.run_app(app)