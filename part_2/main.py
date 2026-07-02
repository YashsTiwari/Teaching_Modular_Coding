# Import functions from each room
from kitchen import search_kitchen
from bathroom import search_bathroom
from bedroom import search_bedroom, watchTV as bedroom_tv
from living_room import search_living_room, watchTV as LR_tv

bedroom_tv()

# Show intro
print("\n" + "🏠 "*20)
print("FINDING MY STUFF!")
print("🏠 "*20 + "\n")

stuff='books'
# Search in each room
print("--- LOOKING FOR ITEM ---")
if search_kitchen(stuff):
    print("✅ Found it in kitchen!")
elif search_bathroom(stuff):
    print("✅ Found it in bathroom!")
elif search_bedroom(stuff):
    print("✅ Found it in bedroom!")
elif search_living_room(stuff):
    print("✅ Found it in living room!")
else:
    print("❌ Not found anywhere!")

print("\n" + "="*50)
