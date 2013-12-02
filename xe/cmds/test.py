from xe import settings
from xe.do import env_do


def main(tail):
    return env_do('%s %s' % (settings['TEST_RUNNER'], ' '.join(tail)))
