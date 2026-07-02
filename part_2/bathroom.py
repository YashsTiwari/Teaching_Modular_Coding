def search_bathroom(x):
    """Search in the bathroom."""
    print("Searching bathroom... ", end="")
    items=['brush', 'toothpaste', 'towel', 'soap']
    if x in items:
        return True
    else:
        return False
