import logging
import logging.config
import os
import yaml


def set_up_logging(default_path='logging.yaml',
                   default_level=logging.INFO,
                   env_key='LOG_CFG',
                   **kwargs):
    """Set up logging configuration.

    Reads log config from a YAML file. See [1] for an example.

    [1]: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
    """
    path = default_path
    value = os.getenv(env_key, None)
    logger = logging.getLogger(__name__)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        logger.info('Logging configured from config file {}'.format(path))
    else:
        logging.basicConfig(level=default_level)
        logger.info('Default logging')
