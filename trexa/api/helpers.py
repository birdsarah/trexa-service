from itertools import islice

"""Helper methods for the API blueprint."""


def trim_csv(csv_file, count=None):
    """Return a generator for streaming the CSV response.

    {count} should come in a stringy int, if it doesn't then
    just treat it as None.
    """
    try:
        count = int(count)
    except (ValueError, TypeError):
        count = None
    with open(csv_file, 'r') as csv:
        for line in islice(csv, count):
            yield line
