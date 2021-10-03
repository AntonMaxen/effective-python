import uuid

def objects_by_attribute(func, objects, attribute, value, insensitive=True):
    matches = []
    for obj in objects:
        obj_value = getattr(obj, attribute)

        value = str(value).lower() if insensitive else str(value) 
        obj_value = str(obj_value).lower() if insensitive else str(obj_value)

        if func(value, obj_value):
            matches.append(obj)

    return matches


def get_exact_matches_by_attribute(objects, attr, value, insensitive=True):
    return objects_by_attribute(
        lambda a, b: a == b,
        objects,
        attr,
        value,
        insensitive=insensitive
    )


def get_part_matches_by_attribute(objects, attr, value, insensitive=True):
    return objects_by_attribute(
        lambda a, b: a in b,
        objects,
        attr,
        value,
        insensitive=insensitive
    )


def get_class_str_attributes(class_obj):
    return [a for a in class_obj.__dict__.keys() if isinstance(a, str)]


def generate_unique_id(objects, attr):
    unique = False
    while not unique:
        unique_id = uuid.uuid4()
        matches = get_exact_matches_by_attribute(objects, attr, unique_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else []
        unique = True if not match else False

    return unique_id


def all_is_instance_of(loo, obj):
    return len([o for o in loo if isinstance(o, obj)]) == len(loo)
