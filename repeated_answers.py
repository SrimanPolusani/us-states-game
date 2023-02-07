def detect_repeated_ans(list_to_check, answer):
    if len(list_to_check) == 0:
        return None

    elif len(list_to_check) > 0:
        for element in list_to_check:
            if element.lower() == answer:
                return True
