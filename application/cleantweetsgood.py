import csv
import os

from tweepy import TweepError

from application.handlers.error_handler import handle_error
from application.handlers.exception_handler import handle_exception
from configuration import ACCESS_TOKEN
from configuration import ACCESS_TOKEN_SECRET
from configuration import CONSUMER_KEY
from configuration import CONSUMER_SECRET
from crosscutting.cleantweetsgood_messages import print_unfollow
from crosscutting.condition_messages import print_info, print_error
from crosscutting.constants import DELETED, ARCHIVE, ARCHIVE_DELIMITER, ARCHIVE_QUOTECHAR, API_LIMIT
from domain.dm import DM
from domain.tweet import Tweet
from domain.username import UserName


def check_config():
    config_ok = True

    print_info("Checking config...")

    if CONSUMER_KEY == "" or CONSUMER_SECRET == "" or ACCESS_TOKEN == "" or ACCESS_TOKEN_SECRET == "":
        config_ok = False

    return config_ok


def delete_blacklisted(api, testing, logging):
    print_info("Deleting blacklisted tweets...")

    if os.path.isfile(ARCHIVE):

        blacklist = parse_archive()

        if blacklist:
            num_deleted = delete_tweets(api, blacklist, testing, logging)
            print_info("{0} tweets deleted".format(num_deleted))
    else:
        handle_error("{0} not found".format(ARCHIVE), True)


def delete_ids(api, tweet_ids, testing, logging):
    tweets = []

    print_info("Deleting tweets by ID...")

    for tweet_id in tweet_ids:
        tweets.append(Tweet(tweet_id))

    num_deleted = delete_tweets(api, tweets, testing, logging)

    print_info("{0} tweets deleted".format(num_deleted))


def delete_all_dms(api, logging, testing):
    print_info("Deleting sent direct messages...")
    sent = api.sent_direct_messages(count=API_LIMIT)
    delete_group_dms(api, sent, "sent", logging, testing)

    received = api.direct_messages(count=API_LIMIT)
    print_info("Deleting received messages...")
    delete_group_dms(api, received, "received", logging, testing)


def delete_group_dms(api, raw_dms, type, logging, testing):
    dms = []

    for dm in raw_dms:
        dms.append(DM(dm.id, dm.text))

    num_deleted = delete_dm(api, dms, logging, testing)
    print_info("{0} {1} direct messages deleted".format(num_deleted, type))


def unfollow(api, users):
    for element in users:
        user = UserName(element)
        user_id = user.get_user_id()
        try:
            api.destroy_friendship(user_id)
            print_unfollow(user.to_string())
        except TweepError:
            print_error("Can't unfollow {0}".format(element))


def parse_archive():
    blacklist = []

    try:
        print_info("Parsing archive...")
        archive = open(ARCHIVE, "r")

        reader = csv.reader(archive, delimiter=ARCHIVE_DELIMITER, quotechar=ARCHIVE_QUOTECHAR)

        for row in reader:
            tweet = Tweet(row[0], row[5])

            if tweet.isBlackListed:
                blacklist.append(tweet)

        return blacklist
    except Exception as e:
        handle_exception(parse_archive.__name__, e)


def delete_tweets(api, blacklist, testing, logging):
    num_deleted = 0

    try:
        if logging:
            log_deleted = open(DELETED, "w")

        for tweet in blacklist:
            tweet.print_info()

            if not testing:
                try:
                    api.destroy_status(tweet.id)
                    if logging:
                        log_deleted.write(tweet.text)
                    num_deleted = num_deleted + 1
                except TweepError:
                    pass

        if logging:
            log_deleted.close()

        return num_deleted

    except Exception as e:
        handle_exception(delete_tweets.__name__, e)


def delete_dm(api, dms, logging, testing):
    num_deleted = 0

    try:
        if logging:
            log = open(DELETED, "w")

        for dm in dms:
            dm.print_info()

            if not testing:
                try:
                    api.destroy_direct_message(dm.id)
                    if logging:
                        log.write(dm.text)
                    num_deleted = num_deleted + 1
                except TweepError:
                    print_error("Can't delete {0}".format(dm.text))

        if logging:
            log.close()

        return num_deleted

    except Exception as e:
        handle_exception(delete_dm.__name__, e)
