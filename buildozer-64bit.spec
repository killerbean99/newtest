[app]
# Application information
title = Mobile App 001
package.name = mobileapp001
package.domain = org.wiseplat
source.dir = .

# Application version
version = 0.3

# Application requirements
requirements = python3,kivy==2.3.0

# Supported orientation
orientation = portrait

# OSX Specific
osx.python_version = 3
osx.kivy_version = 2.0.0

# Android specific
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
# Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
