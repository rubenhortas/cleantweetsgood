from crosscutting.condition_messages import print_exception


def handle_exception(function, e):
    print_exception("{0}: {1}".format(function, e))
    exit(2)
