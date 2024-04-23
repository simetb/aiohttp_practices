# Server example
from aiohttp import web
 
# @web.route('/')
async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)

# Initialize the application.
app = web.Application()

# Add the route to the application.
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
])

# Start the server and run the application.
if __name__ == '__main__':
    web.run_app(app)