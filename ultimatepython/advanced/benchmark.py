import cProfile
import pstats
import time

# Module-level constants
_SLEEP_DURATION = .001


def finish_slower():
    """Finish slower."""
    for i in range(20):
        time.sleep(_SLEEP_DURATION)


def finish_faster():
    """Finish faster."""
    for i in range(10):
        time.sleep(_SLEEP_DURATION)


def main():
    # Create a profile instance
    profile = cProfile.Profile()

    profile.enable()

    for _ in range(2):
        finish_slower()
        finish_faster()

    profile.disable()

    # Sort statistics by cumulative time spent for each function call.
    # There are other ways to sort the stats by, but this is the most
    # common way of doing so. For more info, please consult Python docs:
    # https://docs.python.org/3/library/profile.html
    ps = pstats.Stats(profile).sort_stats('cumulative')

    # Notice how many times each function was called. In this case, the main
    # bottleneck for `finish_slower` and `finish_faster` is `time.sleep`
    # which occurred 60 times. By reading the code and the statistics, we
    # can infer that 40 occurrences came from `finish_slower` and 20 came
    # from `finish_faster`. It is clear why the latter function runs faster
    # in this case, but identifying insights like this are not simple in
    # large projects. Consider profiling in isolation when analyzing complex
    # classes and functions
    ps.print_stats()


if __name__ == "__main__":
    main()
