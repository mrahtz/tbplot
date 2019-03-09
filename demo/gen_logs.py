import time

import easy_tf_log

for i in range(3):
    logger = easy_tf_log.Logger()
    logger.set_log_dir(f'run-seed{i}')
    logger.logkv('foo', 0)
    time.sleep(1.0)
    logger.logkv('foo', 1 + i / 3)


