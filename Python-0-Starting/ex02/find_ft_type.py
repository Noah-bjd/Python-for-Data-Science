def all_thing_is_obj(object: any) -> int:
    object_Type = type(object)
    if object_Type == list:
        print("List :", object_Type)
    elif object_Type == tuple:
        print("Tuple :", object_Type)
    elif object_Type == set:
        print("Set :", object_Type)
    elif object_Type == dict:
        print("Dict :", object_Type)
    elif object_Type == str:
        print(f"{object} is in the kitchen : {object_Type}")
    else:
        print("Type not found")
    return 42
