import asyncio

from constants import HOST, PORT


async def callback(reader, writer):
    while True:
        _input = input('-> ')
        writer.write(_input.encode())

        if _input == 'quit':
            break

        message = await reader.read(512)
        message = message.decode()
        print(message)

    writer.close()


async def client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await callback(reader, writer)

asyncio.run(client())
