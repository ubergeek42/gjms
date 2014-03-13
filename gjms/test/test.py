#coding: utf8

"""

    gjms.test.test

    A thorough unit test of the whole GJMS module.
    If you add a new feature, be sure to include a unit test
    for said feature and make sure the unit test passes.

"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

#Import nose-specific tools.
from nose.tools import assert_raises
from nose.tools import with_setup

# Import core modules.
import gjms.core.users as users
import gjms.core.games as games
import gjms.core.models as models
import gjms.core.events as events
import gjms.core.ratings as ratings
import gjms.core.platforms as platforms
import gjms.core.exceptions as exceptions

# Import util modules.
import gjms.util.url as url
import gjms.util.email as email
import gjms.util.password as password


def init():
    """ Turn off harmless SQLAlchemy warnings. """

    import warnings
    from sqlalchemy import exc as sa_exc

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=sa_exc.SAWarning)


def teardown():
    """ Provided for nosetests. No use. """
    pass

##
## START TESTING:
##


@with_setup(init, teardown)
def test_email_parsing_pass():
    """ Test if correct email passes parsing. """

    assert True == email.validate("user@example.com")


@with_setup(init, teardown)
def test_email_parsing_fail():
    """ Test if wrong email fails parsing. """

    assert_raises(exceptions.InvalidEmail, email.validate, "userexample.com")
    assert_raises(exceptions.InvalidEmail, email.validate, "user@examplecom")
    assert_raises(exceptions.InvalidEmail, email.validate, "userexamplecom")


@with_setup(init, teardown)
def test_url_parsing_pass():
    """ Test if correct URL passes parsing. """

    assert True == url.validate("http://example.com")
    assert True == url.validate("http://example.com/")
    assert True == url.validate("http://www.example.com")
    assert True == url.validate("http://www.example.com/")


@with_setup(init, teardown)
def test_url_parsing_fail():
    """ Test if wrong URL fails parsing. """

    assert_raises(exceptions.InvalidURL, url.validate, "example.com")
    assert_raises(exceptions.InvalidURL, url.validate, "examplecom")
    assert_raises(exceptions.InvalidURL, url.validate, "example;com")


@with_setup(init, teardown)
def test_password_hashing():
    """ Test if password is being hashed. """

    pwd = "password"
    hashed_pwd = password.encrypt(pwd)

    assert pwd != hashed_pwd


@with_setup(init, teardown)
def test_password_validation():
    """ Test if password validation works. """

    pwd = "password"
    hashed_pwd = password.encrypt(pwd)

    assert True == password.validate(pwd, hashed_pwd)


@with_setup(init, teardown)
def test_user_add_right():
    """ Test correct way of adding a user. """

    user = users.add("user", "password", "user@example.com")
    assert type(user) == models.User


@with_setup(init, teardown)
def test_user_add_wrong():
    """ Test wrong way of adding a user. """

    assert_raises(exceptions.InvalidEmail, users.add, "user2", "password", "userexample.com")
    assert_raises(exceptions.InvalidEmail, users.add, "user2", "password", "user@examplecom")
    assert_raises(exceptions.InvalidEmail, users.add, "user2", "password", "userexamplecom")


@with_setup(init, teardown)
def test_user_get():
    """ Test user getting. """

    user = None
    user = users.get("user")

    assert type(user) == models.User


def test_user_get_incorrect():
    """ Test incorrect getting of userss. """

    assert_raises(exceptions.NonExistentUser, users.get, 200)


@with_setup(init, teardown)
def test_user_update():
    """ Test user updating. """

    user = users.get("user")
    user.name = "test_user"

    assert user.name == "test_user"


def test_game_add():
    """ Test game adding. """

    game = games.add("Flingler", "LD26 physics game", "http://hostagamejam.com/flingler.png")
    game2 = games.add("Flingler II", "LD27 physics game", "hostagamejam.com/flingler.png")

    assert type(game) == models.Game
    assert type(game2) == models.Game


def test_game_get_correct():
    """ Test game getting. """

    game = games.get("Flingler")
    assert type(game) == models.Game


def test_game_get_incorrect():
    """ Test incorrect game getting """

    assert_raises(exceptions.NonExistentGame, games.get, 200)


def test_user_game_relation_user():
    """ Test user-game relationship from a user viewpoint. """

    user = users.get("test_user")
    game = games.get("Flingler")
    game2 = games.get("Flingler II")

    user.games.append(game)
    user.games.append(game2)

    assert game in user.games
    assert game2 in user.games


def test_user_game_relation_game():
    """ Test user-game relationship from a game viewpoint. """

    game = games.get("Flingler")

    assert game.author.name == "test_user"


def test_platform_add():
    """ Test platform adding. """

    windows = platforms.add("Windows", "http://hostagamejam.com/flingler.exe")
    android = platforms.add("Android", "hostagamejam.com/flingler.apk")

    assert type(windows) == models.Platform
    assert type(android) == models.Platform


def test_platform_get():
    """ Test platform getting. """

    platform = platforms.get("Windows")

    assert type(platform) == models.Platform


def test_platform_get_incorrect():
    """ Test incorrect getting of platforms. """

    assert_raises(exceptions.NonExistentPlatform, platforms.get, 200)


def test_plat_game_relation_game():
    """ Test platform-game relationship from a game viewpoint. """

    game = games.get("Flingler")
    platform = platforms.get("Windows")
    platform2 = platforms.get("Android")

    game.platforms.append(platform)
    game.platforms.append(platform2)

    assert platform in game.platforms
    assert platform2 in game.platforms


def test_plat_game_relation_plat():
    """ Test platform-game relationship from a platform viewpoint. """

    platform = platforms.get("Android")
    game = games.get("Flingler")

    assert game in platform.games


def test_add_rating_correct():
    """ Test rating adding correctly. """

    rating = ratings.add(4.0)
    rating = ratings.add(3.0)
    rating = ratings.add(2.0)

    assert type(rating) == models.Rating


def test_add_rating_incorrect():
    """ Test rating adding incorrectly. """

    assert_raises(exceptions.InvalidValue, ratings.add, 4)


def test_rating_get_correct():
    """ Test correct getting of ratings. """

    rating = ratings.get(1)
    assert type(rating) == models.Rating


def test_rating_get_incorrect():
    """ Test incorrect getting of ratings. """

    assert_raises(exceptions.NonExistentRating, ratings.get, 200)


def test_game_add_rating():
    """ Test adding ratings to a game. """

    game = games.get("Flingler")

    rating = ratings.get(1)
    rating2 = ratings.get(2)
    rating3 = rating.get(3)

    game.ratings.append(rating)
    game.ratings.append(rating2)
    game.ratings.append(rating3)

    assert rating in game.ratings
    assert rating3 in game.ratings


def test_calculate_rating_correct():
    """ Test if rating is calculated correctly. """

    game = games.get("Flingler")
    rating = ratings.calculate(game)

    assert 3.0 == rating


def test_calculate_rating_incorrect():
    """ Test if rating calculation fails when not passing a game object. """

    assert_raises(exceptions.InvalidParameter, ratings.calculate, "Flingler")


def test_add_event_correct():
    """ Test correct event adding. """

    import datetime as d

    starts = d.datetime(2014, 3, 17, 1)
    ends = d.datetime(2014, 3, 21, 1)

    event = events.add(starts, ends, "Spring Jam Week", "Some theme")
    assert type(event) == models.Event


def test_add_event_incorrect():
    """ Test incorrect event adding. """

    assert_raises(exceptions.InvalidValue, events.add, 3, 2, "Test Event")


def test_event_get():
    """ Test event getting """

    event = events.get(1)
    assert type(event) == models.Event


def test_game_event():
    """ Test event game adding """

    event = events.get(1)
    game = games.get(1)

    event.games.append(game)

    assert game in event.games


def test_participant_event():
    """ Test event participant adding """

    event = events.get(1)
    user = users.get(1)

    event.participants.append(user)

    assert user in event.participants


def test_participant_event_reverse():
    """ Test user events """

    event = events.get(1)
    user = users.get(1)

    assert event in user.participated


def test_delete_game():
    """ Test game deleting. """

    game = games.get("Flingler")
    game.delete()

    assert_raises(exceptions.NonExistentGame, games.get, "Flingler")


def test_delete_user():
    """ Test user deleting. """

    user = users.get("test_user")
    user.delete()

    assert_raises(exceptions.NonExistentUser, users.get, "test_user")


def test_delete_platform():
    """ Test platform deleting. """

    platform = platforms.get("Windows")
    platform.delete()

    assert_raises(exceptions.NonExistentPlatform, platforms.get, "Windows")


def test_delete_rating():
    """ Test rating deleting. """

    rating = ratings.get(1)
    rating.delete()

    assert_raises(exceptions.NonExistentRating, ratings.get, 1)


def test_delete_event():
    """ Test event deleting. """

    event = events.get(1)
    event.delete()

    assert_raises(exceptions.NonExistentEvent, events.get, 1)


