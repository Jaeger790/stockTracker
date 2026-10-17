# Stock Tracker

Small Python experiment for downloading daily stock aggregates from Polygon.

## Setup

Create and activate a Python virtual environment, then run:

```sh
python -m pip install -r requirements.txt
```

Set `POLYGON_API_KEY` in your shell, then:

```sh
python StockTracker.py --ticker GME --start 2023-04-14 --end 2023-04-14 --output stock-data.json
```

The output is JSON. The original script wrote CSV into a `.json` file; the cleanup makes the format match the extension. `gmeData.json` is retained as an original sample and may use that older format.

## Configuration

`.env.example` lists the required variable; the script reads shell environment variables and does not load `.env` automatically. The API key previously committed in source must be rotated in the provider account. Removing it from the current file does not remove it from Git history.

## Status

API experiment, not a trading system. Requires a valid API account and access to the requested data. Network calls and provider permissions were not tested in this review.
## Related projects

See the [project index](https://github.com/Jaeger790#projects) for the rest of my work.
