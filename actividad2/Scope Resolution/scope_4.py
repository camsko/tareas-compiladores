variable = "global"

def exterior():
    variable = "enclosing"

    def interior():
        nonlocal variable
        variable = "modificado"
        return variable

    interior()
    return variable

print(exterior())
print(variable)