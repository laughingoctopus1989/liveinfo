#!/usr/bin/env python3
import platform
print("""
 _    _____ _   _ _____ _____ _   _______ _____
| |  |_   _| | | |  ___|_   _| \ | |  ___|  _  |
| |    | | | | | | |__   | | |  \| | |_  | | | |
| |    | | | | | |  __|  | | | . ` |  _| | | | |
| |____| |_\ \_/ / |___ _| |_| |\  | |   \ \_/ /
\_____|___/ \___/\____/ \___/\_| \_|_|    \___/

                                                
Operating System: %s\n
Processor: %s\n
Hostname: %s\n
""" % (platform.system(), platform.processor(), platform.node()))
