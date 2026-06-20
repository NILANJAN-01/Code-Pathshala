import asyncio
from code_pathshala.labs.kata_professional import fetch_item_details


def test_fetch_item_details_concurrent():
    async def mock_fetch(item_id: int) -> str:
        await asyncio.sleep(0.01)
        return f"Data for {item_id}"

    # Run the async code inside standard asyncio event loop
    results = asyncio.run(fetch_item_details(4, mock_fetch))

    assert len(results) == 4
    assert results == [
        "Data for 1",
        "Data for 2",
        "Data for 3",
        "Data for 4",
    ]
