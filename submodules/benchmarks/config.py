price_error_tolerance = 0.01 # 1% error tolerance
mcap_error_tolerance = 0.01 # 1% error tolerance

coins = [
    {
        "coingecko_id": "bitcoin",
        "names": ["bitcoin", "Bit coin", "expected_to_fail"]
    },
    {
        "coingecko_id": "ripple",
        "names": ["xrp", "ripple"]
    },
    {
        "coingecko_id": "litecoin",
        "names": ["litecoin", "ltc"]
    },
    {
        "coingecko_id": "expected_to_fail",
        "names": ["bitcoin"]
    },
]

price_prompts = [
    "What is the price of {}?",
    "How much does {} cost?",
]

mcap_prompts = [
    "What is the market capitalization of {}?",
    "Whats {}'s market cap?",
]
