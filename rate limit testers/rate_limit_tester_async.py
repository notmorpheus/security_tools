
import aiohttp
import asyncio
import time
import argparse


parser = argparse.ArgumentParser(usage='A simple rate timit test for the API gateways')
parser.add_argument('--req_count', metavar='number_of_requests', type=int, required=True, help='Total targeted request count')
parser.add_argument('--url', metavar='url',type=str, required=True, help='Target API endpoint')
parser.add_argument('--token', metavar='API TOKEN', type=str, required=True, help='API Token')
args=parser.parse_args()
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            if(response.status != 200):
                print(f"Response changed from 200: Response received : {response.status}")
            text = await response.text()
            return text, url
    except Exception as e:
        print(str(e))


async def main(target_count: int):
    tasks = []
    url = args.url
    if("v4" in url):
        headers = {"Authorization": f"Bearer {args.token}"}
    else:
        headers ={}
    async with aiohttp.ClientSession(headers=headers) as new_session:

        for _ in range(target_count): 
            tasks.append(asyncio.create_task(fetch(new_session, url)))

        original_result = await asyncio.gather(*tasks)
        #print last element of the tuple to read body of the last request
        print(f" Body of the last request: \n{original_result[len(original_result)-1]}")
#        for res in original_result: 
#            print(res)   

if __name__ == "__main__":

    total = args.req_count
    start_time = time.time()
    asyncio.run(main(total))
    print(f"\nTotal Time took: {time.time()-start_time} seconds\n\n Rate: {float(total/(time.time()-start_time))} r/s")

