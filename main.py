#Pseudocode
#hardcode menu options
#set up input from user. Ask what ingredients do you have 3 items at a time. Write 'done' when finished
#add ingredients to a list
#print menu list. loop ingredients list through menu list and find common values to generate key
#print corresponding key - "you can make {} for dinner"
#build a show menu function
#build a quit function
#build greater function that calls show, add, quit

menu = {
    "grilled_cheese": ["bread","cheese"],
    "BLT": ["bread","bacon","lettuce","tomato"],
    "veggie_pasta": ["pasta","mushroom", "cheese"],
    "salad": ["lettuce", "tomato", "broccoli"],
    "cake": ["flour","sugar","eggs","baking powder"],
    "time-to-get-swole protein dinner": ["chicken", "broccoli"],
    "chili": ["beans","canned tomatoes", "cheese"],
    "a smoothie": ["frozen fruit","yogurt","juice"],
    "sandwich": ["bread","ham","cheese","tomato","lettuce"],
    "PB&J": ["bread","peanut butter","jelly"],
    "yogurt parfait": ["yogurt", "granola", "fruit"],
    "mac n' cheese": ["pasta", "cheese"]
    }

ingredients_list = []  
def get_ingredients():  
    ingredients_list.clear()
    while True:
        user_input = input("> ").lower()
        ingredients_list.append(user_input)
        
        if user_input == "done":
            ingredients_list.pop()
            print(ingredients_list)
            break

def check_dish(menu, get_ingredients):
    common_ingredients = []
    successful_matches_counter = 0
    for menu_item in menu:
        counter = 0
        for item in get_ingredients:
            if item in menu[menu_item]:
                counter += 1
        if counter == len(menu[menu_item]):
            successful_matches_counter += 1
            print("You can make", menu_item, "!")
    if successful_matches_counter == 0:
        print("Sorry, you don't have the ingredients to make anything for dinner =( ")

def show_menu(menu):
    for i in menu:
        print(i)

def play(menu):
    options = """
    (a) See menu
    (b) Input ingredients
    (q) Quit
    """
    print("Welcome to the Pandemic Dinner Idea Generator. I hope you're hungry.")
    while True:
        user_option = input(options)
        user_option = user_option.lower()
        if user_option == "q":
            print("goodbye!")
            break
        elif user_option == "a":
            show_menu(menu)
        elif user_option == "b":
            print("Please list at least 2 items you have in either your fridge or pantry, one a time. Type 'done' when you're finished.")
            get_ingredients()
            check_dish(menu, ingredients_list)       
        else:
            print("Sorry, please try again.")

play(menu)



