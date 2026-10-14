import os
import sys
import asyncio

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import database as db


async def main():
    await db.db_init()
    print('DB ready')


if __name__ == '__main__':
    asyncio.run(main())
