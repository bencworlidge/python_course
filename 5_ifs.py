sky_is_blue = True
sky_is_above = True

if sky_is_blue and sky_is_above:
    print("The sky is blue and it's above me.")
# Not variable needs to be in parenthesis
elif sky_is_blue and not(sky_is_above):
    print("Why am I upside down?")
elif not(sky_is_blue) and sky_is_above:
    print("Shepard's delight")
else:
    print("The hell is going in?")

# IF STATEMENTS AND COMPARISONS


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(93, 456, 1))
