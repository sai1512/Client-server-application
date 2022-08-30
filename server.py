import asyncio
from importlib import import_module

import sqlalchemy

from constants import HOST, PORT


def execute(user, command):
    args = command.split()
    try:
        module = import_module(f'commands.{args[0]}')
        function = getattr(module, args[0])
        result = function(user, args[1:])
    except Exception as e:
        result = "Invalid Command"
        print(e)
    return result


async def callback(reader, writer):
    user = [None]
    while True:
        command = await reader.read(512)
        command = command.decode()

        if command == 'quit':
            break

        result = execute(user, command)
        writer.write(result.encode())


async def server():
    srvr = await asyncio.start_server(callback, HOST, PORT)
    async with srvr:
        await srvr.serve_forever()

if __name__ == '__main__':
    asyncio.run(server())
