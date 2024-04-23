# Client example
import aiohttp
import asyncio

# Function to get the status and content type of a URL
# In async programming, we use await to wait for the result of a coroutine
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as response:
            
            print("Status: ", response.status)
            print("Content-type: ", response.headers['Content-type'])
            
            html = await response.text()
            print("Body: ", html[:15], "...")

# Set the event loop policy to WindowsSelectorEventLoopPolicy
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Just in Windows
asyncio.run(main()) # Run the main function