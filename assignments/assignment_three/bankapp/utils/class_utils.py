import uuid


def objects_by_attribute(func, objects, attribute, value):
    """
    matches object attributes with value with the help of a function.

    Args:
        func: function to compare a with b.
        objects: list of objects.
        attribute: attribute to check in the objects.
        value: value that is used to compare with the object attribute.
    Returns:
        matches: list of matched objects

    """
    matches = []
    for obj in objects:
        if hasattr(obj, attribute):
            obj_value = getattr(obj, attribute)

            if func(value, obj_value):
                matches.append(obj)

    return matches


def get_exact_matches_by_attribute(objects, attr, value, insensitive=True):
    """
    matches objects attributes that value is equal of.

    Args:
        objects: list of objects.
        attr: attribute to check in the objects.
        value: value that is used to compare with the object attribute.
        insensitive: does insensitive search if True.
    Returns:
        list of matched objects.

    """
    def condition(a, b):
        a = str(a).lower() if insensitive else str(a)
        b = str(b).lower() if insensitive else str(b)

        return a == b

    return objects_by_attribute(
        condition,
        objects,
        attr,
        value
    )


def get_part_matches_by_attribute(objects, attr, value, insensitive=True):
    """
    matches object attributes that value is a part of.

    Args:
        objects: list of objects.
        attr: attribute to check in the objects.
        value: value that is used to compare with the object attribute.
        insensitive: does insensitive search if True.
    Returns:
        list of matched objects.

    """
    def condition(a, b):
        a = str(a).lower() if insensitive else str(a)
        b = str(b).lower() if insensitive else str(b)

        return a in b

    return objects_by_attribute(
        condition,
        objects,
        attr,
        value
    )


def get_bigger_then_by_attribute(objects, attr, value, inclusive=False):
    """
    matches object attributes where attribute is bigger then value.

    Args:
        objects: list of objects.
        attr: attribute to check in the objects.
        value: value that is used to compare with the object attribute.
        inclusive: does inclusive match if True.
    Returns:
        list of matched objects.

    """
    not_inclusive_c = lambda a, b: float(b) > float(a)
    inclusive_c = lambda a, b: float(b) >= float(a)

    return objects_by_attribute(
        inclusive_c if inclusive else not_inclusive_c,
        objects,
        attr,
        value
    )


def get_smaller_then_by_attribute(objects, attr, value, inclusive=False):
    """
    matches object attributes where attribute is smaller then value.

    Args:
        objects: list of objects.
        attr: attribute to check in the objects.
        value: value that is used to compare with the object attribute.
        inclusive: does inclusive match if True.
    Returns:
        list of matched objects.

    """
    not_inclusive_c = lambda a, b: float(b) < float(a)
    inclusive_c = lambda a, b: float(b) <= float(a)

    return objects_by_attribute(
        inclusive_c if inclusive else not_inclusive_c,
        objects,
        attr,
        value
    )


def get_class_str_attributes(class_obj):
    """
    returns all string attributes of a class object.

    Args:
        class_obj: The class object to check.
    Returns:
        list of string attributes.

    """
    return [a for a in class_obj.__dict__.keys() if isinstance(a, str)]


def generate_unique_id(objects, attr):
    """
    Generate a uuid object that is unique in the context of objects passed to
    the function.

    Args:
        objects: list of objects to check.
        attr: name of the id attribute.
    Returns:
        unique_id: a unique uuid object.

    """
    unique = False
    while not unique:
        unique_id = uuid.uuid4()
        matches = get_exact_matches_by_attribute(objects, attr, unique_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else []
        unique = True if not match else False

    return unique_id


def all_is_instance_of(loo, obj):
    """
    Returns true if all objects in list of objects is equal to the passed
    object.

    Args:
        loo: list of objects.
        obj: obj to use as checker.
    Returns:
        Boolean that tells if the list if in same type.

    """
    return len([o for o in loo if isinstance(o, obj)]) == len(loo)
