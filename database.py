import discord
import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='Space', password='hellowo',
                                 database='Space', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM mytable''')
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
