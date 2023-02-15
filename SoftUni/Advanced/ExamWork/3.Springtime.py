
def start_spring(**kwargs):

    spring_dict = {}
    for key, value in kwargs.items():
        if value not in spring_dict:
            spring_dict[value] = [key]
        else:
            spring_dict[value].append(key)
    sorted_dict = {}
    sorted_keys = sorted(spring_dict, key=lambda x: (-len(spring_dict[x]), x))
    for key in sorted_keys:
        sorted_dict[key] = sorted(spring_dict[key])
    result = ""

    for key in sorted_dict:
        result += f"{key}:\n"
        for item in sorted_dict[key]:
            result += f"-{item}\n"

    return result





example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))