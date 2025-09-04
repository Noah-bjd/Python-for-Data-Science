def NULL_not_found(object: any) -> int:
    Object_type = type(object)
    if object is None:
        print(f"Nothing : {Object_type}")
    elif Object_type is float and str(object) == 'nan':
        print(f"Garlic: nan {Object_type}")
    elif object == 0 and Object_type is int:
        print(f"Zero: 0 {Object_type}")
    elif object == '' and Object_type is str:
        print(f"Empty: {Object_type}")
    elif object is False and Object_type is bool:
        print(f"Fake: False {Object_type}")
    else:
        print("Type not Found")
        return 1
    return 0
