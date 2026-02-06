
# ============================
# TODO:Question 1
# ============================
def split_coords(coordinates: list) -> tuple:
    x_list = []
    y_list = []

    for coords in coordinates:
        x, y = coords
        x_list.append(x)
        y_list.append(y)
    
    return x_list, y_list


# ============================
# TODO:Question 2
# ============================
def create_id_lookup(user_data: list) -> dict:
    res = {}

    for idx, name in enumerate(user_data):
        res[name] = idx

    return res


# ============================
# TODO:Question 3
# ============================
def extract_unique_tags(posts: list) -> set:
    res = set()

    for post in posts:
        res.add(post.lower())
    
    return res


# ============================
# TODO:Question 4
# ============================
def group_by_category(items: list) -> dict:
    res = {}

    for item in items:
        if item["type"] not in res:
            res[item["type"]] = [item["name"]]
        else:
            res[item["type"]].append(item["name"])
    
    return res

print(group_by_category([{"name": "Boerewors", "type": "Meat"}, {"name": "Charcoal", "type": "Hardware"}, {"name": "Lamb Chops", "type": "Meat"}, {"name": "Chakalaka", "type": "Canned Goods"}]))

# ============================
# TODO:Question 5
# ============================
def batch_api_dispatcher(user_ids: list | tuple) -> list:
    pass


# ============================
# TODO:Question 6
# ============================
def social_graph_inverter(following_list: dict) -> dict:
    pass


# ============================
# TODO:Question 7
# ============================
def fibonacci_generator(n: int) -> list:
    pass

