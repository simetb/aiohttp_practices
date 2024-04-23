from aiohttp import web
import json

# Initialize our web app variable
app = web.Application()

# Function to handle the base route request
async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))


# Function to create a new user (Example) with post request
async def new_user(request):
    try:
        data = await request.json()
        
        # Happy path where name is set
        frase = data['frase']
        user = request.query['name']
        
        print("Creating a new user with the name {} and frase {}".format(user, frase))
        
        # Return a success json response with a status code 200 i.e 'ok'
        response_obj = { 'status' : 'success' }
        return web.Response(text=json.dumps(response_obj), status=200)
        
    
    except Exception as e:
        # Bad path where name is not set
        response_obj = {'status': 'failed','reason': str(e)}
        # Response failed with a status code of 500 i.e 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)



# Get routes
app.router.add_get('/', handle)

# Post routes
app.router.add_post('/user', new_user)

# Run the app
web.run_app(app)