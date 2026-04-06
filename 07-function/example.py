# Example 1
def apply_discount(price, discount):

    if not isinstance(price,(int,float)):
        return("The price should be a number")

    elif not isinstance(discount,(int,float)):
        return("The discount should be a number")

    elif price <= 0:
        return("The price should be greater than 0")

    elif discount < 0 or discount > 100:
        return("The discount should be between 0 and 100")

    final_price = price - ((price * discount) /  100)
    return final_price

print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(0, 100))
print(apply_discount(74.5, 20.0))

 # Example 2
full_dot = '●'
empty_dot = '○'

def create_character(name, strength , intelligence, charisma):
    if not isinstance(name , str):
        return "The character name should be a string"
        
    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    stats = {'STR': strength,'INT': intelligence, 'CHA': charisma}
    for stat in stats.values():
        if not isinstance(stat, int):
            return "All stats should be integers"

    for stat in stats.values():
        if stat < 1:
            return "All stats should be no less than 1"

    for stat in stats.values():
        if stat > 4:
            return "All stats should be no more than 4"

    if sum(stats.values()) != 7 :
        return "The character should start with 7 points"

    def stat_line(label, value):
        return f"{label} " + "●" * value + "○" * (10 - value)
    

    result = (
        f"{name}\n"
        f"{stat_line('STR', strength)}\n"
        f"{stat_line('INT', intelligence)}\n"
        f"{stat_line('CHA', charisma)}"
    )
    
    return result
print(create_character('ren', 4, 2, 1))










