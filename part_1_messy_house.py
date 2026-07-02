# ============================================================================
# PART 1: THE MESSY HOUSE - EVERYTHING IN ONE FILE
# ============================================================================
# This is what happens when you put EVERYTHING in a single file.
# No organization. No structure. Just CHAOS.
# 
# Warning: This will make you want to scream. That's the point! 😱
# ============================================================================

from datetime import datetime
import random

# Global variables everywhere (BAD!)
toothbrush_found = False
coffee_found = False
book_found = False
keys_found = False
phone_found = False
wallet_found = False

# More random global variables
person_emotion = "😐"
search_count = 0
total_frustration = 0

# Functions with terrible names doing multiple things
def do_stuff_1(item_name):
    """This function does... what exactly?"""
    global toothbrush_found, coffee_found, book_found, person_emotion, total_frustration
    
    if item_name == "toothbrush":
        if random.random() > 0.3:
            print("Found toothbrush in the kitchen!")
            toothbrush_found = True
            return True
        else:
            print("Not in the kitchen...")
            total_frustration += 1
            return False
    
    if item_name == "coffee":
        if random.random() > 0.4:
            print("Found coffee on the table!")
            coffee_found = True
            return True
        else:
            print("Not on the table...")
            total_frustration += 1
            return False
    
    if item_name == "book":
        if random.random() > 0.5:
            print("Found book on the couch!")
            book_found = True
            return True
        else:
            print("Not on the couch...")
            total_frustration += 1
            return False


def do_stuff_2(x):
    """Another poorly named function."""
    global person_emotion, total_frustration
    
    if total_frustration == 0:
        person_emotion = "😐"
    elif total_frustration == 1:
        person_emotion = "😕"
    elif total_frustration == 2:
        person_emotion = "😤"
    elif total_frustration >= 3:
        person_emotion = "😡"
    
    print(f"Emotion: {person_emotion}")


def search_for_toothbrush():
    """Search for toothbrush in MANY places."""
    global search_count
    
    locations = ["kitchen", "bathroom", "bedroom", "living room", "basement"]
    
    for loc in locations:
        search_count += 1
        print(f"Searching {loc} for toothbrush... ", end="")
        
        if random.random() > 0.6:
            print("FOUND!")
            return True
        else:
            print("Not here")
    
    return False


def search_for_coffee():
    """Search for coffee in MANY places."""
    global search_count
    
    places = ["kitchen", "table", "fridge", "pantry", "counter"]
    
    for place in places:
        search_count += 1
        print(f"Searching {place} for coffee... ", end="")
        
        if random.random() > 0.5:
            print("FOUND!")
            return True
        else:
            print("Not here")
    
    return False


def search_for_book():
    """Search for book in MANY places."""
    global search_count
    
    spots = ["couch", "bed", "shelf", "table", "desk"]
    
    for spot in spots:
        search_count += 1
        print(f"Searching {spot} for book... ", end="")
        
        if random.random() > 0.5:
            print("FOUND!")
            return True
        else:
            print("Not here")
    
    return False


# Copy-paste the search functions (BAD PRACTICE!)
def search_for_keys():
    """This is just a copy of the search functions!"""
    global search_count
    
    spots = ["pocket", "table", "drawer", "desk", "counter"]
    
    for spot in spots:
        search_count += 1
        print(f"Searching {spot} for keys... ", end="")
        
        if random.random() > 0.5:
            print("FOUND!")
            return True
        else:
            print("Not here")
    
    return False


def search_for_phone():
    """Another copy-paste!"""
    global search_count
    
    spots = ["pocket", "table", "bed", "desk", "shelf"]
    
    for spot in spots:
        search_count += 1
        print(f"Searching {spot} for phone... ", end="")
        
        if random.random() > 0.5:
            print("FOUND!")
            return True
        else:
            print("Not here")
    
    return False


def search_for_wallet():
    """And another!"""
    global search_count
    
    spots = ["pocket", "drawer", "desk", "table", "shelf"]
    
    for spot in spots:
        search_count += 1
        print(f"Searching {spot} for wallet... ", end="")
        
        if random.random() > 0.5:
            print("FOUND!")
            return True
        else:
            print("Not here")
    
    return False


# Functions with confusing logic
def process_toothbrush_task():
    """What does this do? Hard to tell!"""
    global toothbrush_found, person_emotion, total_frustration
    
    print("\n=== LOOKING FOR TOOTHBRUSH ===")
    
    # Try one way
    if do_stuff_1("toothbrush"):
        toothbrush_found = True
        print("Got it!")
    else:
        # Try another way (DUPLICATED LOGIC!)
        result = search_for_toothbrush()
        if result:
            toothbrush_found = True
        else:
            total_frustration += 1
    
    do_stuff_2(1)


def process_coffee_task():
    """Same confusing logic, repeated!"""
    global coffee_found, person_emotion, total_frustration
    
    print("\n=== LOOKING FOR COFFEE ===")
    
    if do_stuff_1("coffee"):
        coffee_found = True
        print("Got it!")
    else:
        result = search_for_coffee()
        if result:
            coffee_found = True
        else:
            total_frustration += 1
    
    do_stuff_2(1)


def process_book_task():
    """Copy-pasted again!"""
    global book_found, person_emotion, total_frustration
    
    print("\n=== LOOKING FOR BOOK ===")
    
    if do_stuff_1("book"):
        book_found = True
        print("Got it!")
    else:
        result = search_for_book()
        if result:
            book_found = True
        else:
            total_frustration += 1
    
    do_stuff_2(1)


def show_status():
    """Status... but WHERE is the data? Mixed with the logic!"""
    print("\n" + "="*50)
    print(f"Current emotion: {person_emotion}")
    print(f"Toothbrush found: {toothbrush_found}")
    print(f"Coffee found: {coffee_found}")
    print(f"Book found: {book_found}")
    print(f"Total searches: {search_count}")
    print(f"Total frustration level: {total_frustration}")
    print("="*50)


def show_final_stats():
    """Statistics scattered everywhere!"""
    print("\n" + "="*70)
    print("FINAL STATUS")
    print("="*70)
    
    items_found = 0
    if toothbrush_found:
        print("✅ Toothbrush - FOUND!")
        items_found += 1
    else:
        print("❌ Toothbrush - MISSING")
    
    if coffee_found:
        print("✅ Coffee - FOUND!")
        items_found += 1
    else:
        print("❌ Coffee - MISSING")
    
    if book_found:
        print("✅ Book - FOUND!")
        items_found += 1
    else:
        print("❌ Book - MISSING")
    
    print(f"\nItems found: {items_found}/3")
    print(f"Total searches: {search_count}")
    print(f"Average searches per item: {search_count / 3 if search_count > 0 else 0:.1f}")
    print(f"Final emotion: {person_emotion}")
    print("="*70)


# MAIN PROGRAM - EVERYTHING HERE TOO!
if __name__ == "__main__":
    print("\n" + "🏠 "*20)
    print("PART 1: THE MESSY HOUSE - WHERE'S MY STUFF?!?")
    print("🏠 "*20 + "\n")
    
    print("Starting the day. Need to find 3 items: toothbrush, coffee, book")
    print("Everything is scattered EVERYWHERE. This is going to be painful...\n")
    
    input("Press Enter to start looking for your stuff...\n")
    
    # Task 1: Find toothbrush
    process_toothbrush_task()
    show_status()
    input("Press Enter to continue...")
    
    # Task 2: Find coffee
    process_coffee_task()
    show_status()
    input("Press Enter to continue...")
    
    # Task 3: Find book
    process_book_task()
    show_status()
    input("Press Enter to see final results...")
    
    show_final_stats()
    
    print("\n😱 LOOK HOW MESSY THIS IS! 😱")
    print("\nProblems with this code:")
    print("  ❌ Everything in ONE file")
    print("  ❌ Copy-pasted functions (search_for_X repeated 3 times!)")
    print("  ❌ Global variables scattered everywhere")
    print("  ❌ Functions doing multiple unrelated things")
    print("  ❌ Confusing logic mixed with data")
    print("  ❌ Hard to find anything")
    print("  ❌ Hard to change anything")
    print("  ❌ Hard to test anything")
    print("  ❌ IMPOSSIBLE to maintain!")
    
    print("\n" + "="*70)
    print("In the NEXT part, you'll see how this should be organized...")
    print("Get ready to be RELIEVED! 😍")
    print("="*70)
