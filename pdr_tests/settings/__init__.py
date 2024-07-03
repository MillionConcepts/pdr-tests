"""settings for pdr-tests - public interface
See settings.base for the list of settings.
They can be overridden by creating settings.user.
"""

from pdr_tests.settings._patcher import load_settings
load_settings()
