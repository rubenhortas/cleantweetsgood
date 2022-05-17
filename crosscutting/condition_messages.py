from presentation.tag import Tag


def print_debug(msg):
    """
    print_debug(msg)
        Prints a debug message.
    Arguments:
        msg: (string) Debug message.
    """

    print("{0} {1}".format(Tag.debug, msg))


def print_error(msg):
    """
    print_error(msg)
        Prints an error message.
    Arguments:
        msg: (string) Error message.
    """

    print("{0} {1}".format(Tag.error, msg))


def print_exception(msg):
    """
    print_exception(msg)
        Prints an exception message.
    Arguments:
        msg: (string) System exception message.
    """

    print("{0} {1}".format(Tag.exception, msg))


def print_warning(msg):
    """
    print_warning(msg)
        Prints a warning message.
    Arguments:
        msg: (string) Warning message.
    """

    print("{0} {1}".format(Tag.warning, msg))


def print_info(msg):
    """
    print_info(msg)
        Prints an information message.
    Arguments:
        msg: (string) Information message.
    """

    print("{0} {1}".format(Tag.info, msg))
