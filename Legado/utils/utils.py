

def contain_str(source, check_list):
    for ch in check_list:
        if ch in source:
            return True
    return False