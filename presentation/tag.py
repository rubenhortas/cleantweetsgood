from presentation.color import Color


class Tag:
    """
    Defines the tags for each message shown in the output.
    """

    debug = ">>"
    error = "[{0}ERROR{1}]".format(Color.bold_red, Color.end)
    exception = "[{0}EXCEPTION{1}]".format(Color.bold_red, Color.end)
    info = "[{0}*{1}]".format(Color.green, Color.end)
    warning = "[{0}Warning{1}]".format(Color.bold_orange, Color.end)
    black_list = "{0}✗{1}".format(Color.bold_red, Color.end)
    white_list = "{0}✓{1}".format(Color.bold_green, Color.end)
