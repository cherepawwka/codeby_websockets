import asyncio
import websockets
import base64


async def codeby():
    async with websockets.connect('ws://62.173.140.174:16011/ws') as websocket:  # creating socket
        for i in range(0, 50):  # cycle for task
            response = await websocket.recv()  # wait for data from server
            print(response)
            if i == 0:
                data = response[response.find(":") + 2:]  # select substing in base64 in first iteration
            else:
                data = response[
                       response.find(":") + 2:response.find("(") - 1]  # select substring in base64 in other iterations
            decoded_data = base64.b64decode(data).decode('utf-8')  # decode data from base64
            print(f"Decoded from base64: " + decoded_data)
            expression = decoded_data[4:]  # math preparation
            result = eval(expression)  # counting
            print(result)
            await websocket.send(str(result))  # send data to socket

        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(codeby())
