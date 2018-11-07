def get_formatted_name(frist_name, last_name, midlle_name=""):
    if midlle_name:
        full_name = frist_name + " "+midlle_name+" "+last_name
    else:
        full_name = frist_name + " "+last_name
    return full_name.title()
