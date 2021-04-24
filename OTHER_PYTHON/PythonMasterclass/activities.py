from random import choice
def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")

    ending = "because YOLO!"
    if is_healthy:
        ending = "because its Healthy food"
    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I didn't mean to oversleep"
    return f"I'm feeling refreshed after {num_hours} hour of nap"

def is_funny(name):
    if name == "tim":
        return f"{name} should not be funny"
    else:
        return f"{name} should be funny"

def laugh():
    return choice(("lol", "tehehe", "haha"))
