#!/usr/bin/env python3
"""Print the one-sentence apology the agent owes you.

The sentence itself is stored in entry_text; this file pulls it
out of that module by attribute name and prints it on its own.
"""

import entry_text

_apology = getattr(entry_text, "LINE")

print(_apology)
