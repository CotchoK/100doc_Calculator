def calc_string(arithmetic):
    a_calc_string = ''
    for i in range(len(arithmetic)):
        if i == 0:
            a_calc_string += f'{arithmetic[i]}'
        else:
            a_calc_string += f' {arithmetic[i]}'

    return a_calc_string