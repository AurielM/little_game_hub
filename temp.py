# def simple_function(variable):
#     print(variable)


# def with_keyword_arguments(variable="default"):
#     print(variable)

def with_both_correctly(variable1,
                        variable2="default",
                        variable3="default2"):
    print(variable1, variable2, variable3)


with_both_correctly(variable3="plop2", "plop")

# def variable_amount_of_args(*args):
#     for string in args:
#         print(string)

# def variable_amount_of_keyword_args(**kwargs):
#     for string in kwargs:
#         print(string)

# def incorrect_thing(variable="default", regular):
#     pass