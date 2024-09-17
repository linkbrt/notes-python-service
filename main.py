from aiohttp import web

routes = web.RouteTableDef()

def setup_routes(applicaion) -> None:
    from app.notes.routes import setup_routes as api_routes



@routes.get('/')
async def get_notes(request: web.Request) -> web.Response:
    return web.json_response(data={'some': 'data'})


@routes.post('/')
async def create_note(request: web.Request) -> web.Response:
    return


app = web.Application()
app.add_routes(routes)


if __name__ == "__main__":
    setup_routes(app)
    web.run_app(app)