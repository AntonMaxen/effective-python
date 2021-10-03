import uuid

def objects_by_attribute(func, objects, attribute, value):
    matches = []
    for obj in objects:
        if hasattr(obj, attribute):
            obj_value = getattr(obj, attribute)

            if func(value, obj_value):
                matches.append(obj)

    return matches


def get_exact_matches_by_attribute(objects, attr, value, insensitive=True):
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
    not_inclusive_c = lambda a, b: float(b) >  float(a)
    inclusive_c     = lambda a, b: float(b) >= float(a) 


    return objects_by_attribute(
        inclusive_c if inclusive else not_inclusive_c,
        objects,
        attr,
        value
    )

def get_smaller_then_by_attribute(objects, attr, value, inclusive=False):
    not_inclusive_c = lambda a, b: float(b) <  float(a)
    inclusive_c     = lambda a, b: float(b) <= float(a) 


    return objects_by_attribute(
        inclusive_c if inclusive else not_inclusive_c,
        objects,
        attr,
        value
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
