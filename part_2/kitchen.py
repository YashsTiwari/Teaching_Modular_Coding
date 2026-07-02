def search_kitchen(x):
    """Search in the kitchen."""
    print("Searching kitchen... ", end="")
    items = ["knife", "spoons", "plates", "glasses"]
    if x in items:
        return True
    else:
        return False
