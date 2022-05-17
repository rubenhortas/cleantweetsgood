from crosscutting.cleantweetsgood_messages import print_blacklisted
from crosscutting.constants import ENCODING


class DM:
    id = None
    text = None

    def __init__(self, dm_id, text):
        self.id = dm_id
        self.text = "{0}\n".format(text.replace("\n", " ").lower().encode(ENCODING))

    def print_info(self):
        print_blacklisted(self.text)
