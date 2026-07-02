def search_living_room(x):
    """Search in the living room."""
    print("Searching living room... ", end="")
    items=['sofa', 'paintings', 'TV', 'mat']
    if x in items:
        return True
    else:
        return False

def watchTV():
    print("Watching TV from LR")
    