import asyncio
import aiohttp
import time
import os

# Get the API key from the environment variable
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY') 

# Define the symbols to get data for
SYMBOLS = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']

# Define the URL to get the data from
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

# Create a list to store the results
results = []

# Create a list of tasks to get the data for each symbol
def get_tasks(session):
    tasks = []
    for symbol in SYMBOLS:
        tasks.append(asyncio.create_task(session.get(url.format(symbol, API_KEY), ssl=False)))
    return tasks

# Define a function to get the data for each symbol
async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())

# Start a timer
start = time.time()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_symbols())

# end a timer
end = time.time()

# Calculate the total time taken to get the data
total_time = end - start

# Output the results and the total time taken
print("It took {} seconds to make {} API calls".format(total_time, len(SYMBOLS)))
print('You did it!')


        