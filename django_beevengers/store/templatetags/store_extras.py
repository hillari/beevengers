from django import template

register = template.Library()


@register.filter(name='row_start_modulo')
def row_start_modulo(value, arg):
    if isinstance(arg, int):
        # return true if equal to 1 to get first row started no matter what
        # -1 is used to offset the open row tags
        return ((value - 1) % arg) == 0

    else:
        TypeError("Not the right type of value was used. Need int")


@register.filter(name='row_end_modulo')
def row_end_modulo(value, arg):
    if isinstance(arg, int):
        # return true if equal to 1 to get first row started no matter what
        return (value % arg) == 0

    else:
        TypeError("Not the right type of value was used. Need int")


@register.filter(name='num_empties')
def num_empties(value, arg):
    if isinstance(arg, int):
        # return a list of how many loop are needed
        num_empties_needed = arg - (value % arg)
        num_empties_loop_list = []
        if num_empties_needed == arg: # no empties are needed, row is full
            return num_empties_loop_list
        else:

            # list will be used by for loop to decide how many loops to take
            i = 0
            while i != num_empties_needed:
                num_empties_loop_list.append(i)
                i += 1

            return num_empties_loop_list

    else:
        TypeError("Not the right type of value was used. Need int")

