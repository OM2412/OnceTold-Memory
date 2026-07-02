import asyncio
from cognee_client import remember, recall

async def main():
    print(await remember("Customer reported a billing issue in March 2026, resolved with a $20 refund.", customer_id="cust_001"))
    status, results = await recall("What billing issues has this customer had?", customer_id="cust_001")
    print(status)
    print(results)

asyncio.run(main())