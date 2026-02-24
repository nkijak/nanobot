"""
Entry point for running nanobot as a module: python -m nanobot
"""

import sys
from nanobot.cli.commands import app
from loguru import logger

if __name__ == "__main__":
    logger.add(sys.stderr)
    app()
