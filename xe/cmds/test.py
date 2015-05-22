from xe import settings
from xe.do import env_do


def main(tail):
    cmd = settings['TEST_RUNNER'].split()
    cmd.extend(tail)
    return env_do(cmd)
