from xe import settings
from xe.do import env_do


def main(tail):
    cmd = [settings['TEST_RUNNER']]
    cmd.extend(tail)
    print(cmd)
    return env_do(cmd)
