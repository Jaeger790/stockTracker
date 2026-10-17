import argparse
import json
import os
from pathlib import Path

from polygon import RESTClient


API_KEY = None


def main():
    parser = argparse.ArgumentParser(description="Download daily stock aggregates.")
    parser.add_argument("--ticker", default="GME")
    parser.add_argument("--start", default="2023-04-14")
    parser.add_argument("--end", default="2023-04-14")
    parser.add_argument("--output", type=Path, default=Path("stock-data.json"))
    args = parser.parse_args()
    api_key = os.environ.get("POLYGON_API_KEY") or API_KEY
    if not api_key:
        parser.error("Set POLYGON_API_KEY before running.")

    with RESTClient(api_key) as client:
        aggregates = client.get_aggs(args.ticker, 1, "day", args.start, args.end)
    records = [vars(record) for record in aggregates]
    args.output.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(records)} records to {args.output}")


if __name__ == "__main__":
    main()
