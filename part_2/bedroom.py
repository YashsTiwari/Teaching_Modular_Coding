def search_bedroom(x):
    """Search in the bedroom."""
    print("Searching bedroom... ", end="")
    items=['books', 'lamp', 'pillow', 'bed']
    if x in items:
        return True
    else:
        return False

def watchTV():
    print("Watching TV from Bedroom")