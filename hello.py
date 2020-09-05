def get_summ(one, two, delimiter='&'):
    one=str(one)
    two=str(two)
    result = one+delimiter+two
    result = result.upper()
    return result

print(get_summ("Learn","Python"))