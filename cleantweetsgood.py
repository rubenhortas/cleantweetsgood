import argparse
import signal

from application.cleantweetsgood import check_config
from application.cleantweetsgood import delete_blacklisted, delete_all_dms, unfollow, delete_ids
from application.helpers.tweepyHelper import get_api
from application.helpers.tweepyHelper import login
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.cleantweetsgood_messages import print_configuration_help
from crosscutting.condition_messages import print_error, print_info
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from presentation.utils.screen import clear_screen

if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    parser = argparse.ArgumentParser(prog="CleanTweetsGood")
    parser = argparse.ArgumentParser(description="Clean your twitter account")
    parser.add_argument("-t", "--test", dest="testing", action="store_true",
                        help="Run a single test showing the expected output")
    parser.add_argument("-log", "--log", dest="logging", action="store_true",
                        help="Saves the output into a plain text file")
    parser.add_argument("-bl", "--blacklist", dest="delete_blacklist", action="store_true",
                        help="Deletes the tweets that contain blacklisted words")
    parser.add_argument("-dm", "--direct_messages", dest="delete_dms", action="store_true",
                        help="Deletes *ALL* the direct messages")
    parser.add_argument("-u", "--unfollow", metavar="USER", nargs="+",
                        help="Users to unfollow")
    parser.add_argument("-id", nargs="+", help="Tweet IDs to delete")
    args = parser.parse_args()

    testing = args.testing
    logging = args.logging

    clear_screen()

    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:
        clear_screen()
        print_info("CleanTweetsGood")

        if check_config():
            print_info("Log in...")
            auth = login()
            api = get_api(auth)

            if args.delete_blacklist:
                delete_blacklisted(api, logging, testing)

            if args.delete_dms:
                delete_all_dms(api, logging, testing)

            if args.unfollow:
                unfollow(api, args.unfollow)

            if args.id:
                delete_ids(api, args.id, logging, testing)
        else:
            print_configuration_help()
            exit(0)

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
