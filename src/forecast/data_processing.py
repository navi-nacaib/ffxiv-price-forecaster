from datetime import datetime

import requests


def fetch_data():
    # Example item ID, change as needed
    item_id = '44162'

    # The amount of time before now to calculate stats over, in milliseconds
    starts_within = '2592000000'  # 30 days in milliseconds

    # The amount of time before entriesUntil or now to take entries within, in seconds.
    entries_within = '2592000'  # 30 days in seconds

    # Max amount of entries to return per request
    entries_to_return = 99999

    # World or data center to retrieve data for
    region = "Aether"

    # Max sale price, set a value to ignore any higher values
    max_sale_price = 35000

    all_entries = []  # List to store all fetched entries
    last_timestamp = None  # Track the latest timestamp fetched to detect if new data stops coming in

    while True:
        # Build the API URL with the updated `starts_within` parameter
        url = (
            f"https://universalis.app/api/v2/history/{region}/{item_id}"
            f"?entriesToReturn={entries_to_return}"
            f"&statsWithin={starts_within}"
            f"&entriesWithin={entries_within}"
            f"&maxSalePrice={max_sale_price}"
        )

        # Fetch data from the API
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to fetch data from Universalis API")

        # Parse the response
        entries = response.json().get('entries', [])

        # If no entries were fetched, break out of the loop
        if not entries:
            print("No more entries found.")
            break

        # Append new entries to the cumulative list
        all_entries.extend(entries)

        # Find the earliest and latest timestamps in this batch
        current_earliest_timestamp = min(entry['timestamp'] for entry in entries)
        current_latest_timestamp = max(entry['timestamp'] for entry in entries)

        # Convert timestamps to a readable format for debug output
        readable_earliest = datetime.fromtimestamp(current_earliest_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        readable_latest = datetime.fromtimestamp(current_latest_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Print debug information
        print(f"\nFetched {len(entries)} entries in this batch:")
        print(f"  - Earliest timestamp: {readable_earliest}")
        print(f"  - Latest timestamp: {readable_latest}")

        # If no new data has been retrieved, break the loop
        if last_timestamp is not None and current_latest_timestamp <= last_timestamp:
            print("No new data found in the latest batch. Stopping data fetch.")
            break

        # Update last_timestamp and starts_within to continue fetching data prior to this timestamp
        last_timestamp = current_latest_timestamp
        starts_within = str(current_latest_timestamp * 1000)  # Update `starts_within` for the next request

        # If fewer than the max requested entries were returned, assume all available data has been fetched
        if len(entries) < entries_to_return:
            print("Fewer than the maximum entries returned; assuming all data has been fetched.")
            break

    print(f"\nTotal entries fetched: {len(all_entries)}")
    return all_entries
