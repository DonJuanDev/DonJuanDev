"""
Single source of truth for everything personal in this profile README.

Every generator (portrait, info card, heatmap) imports from here, so changing
your bio/stack/handle is a one-file edit -- no hunting through SVG builders.

Regenerate after editing:
    python scripts/fetch_contributions.py
    python scripts/render_heatmap_svg.py
    python scripts/make_info_card.py
    python scripts/prep_photo.py source-photo.jpg && python scripts/make_ascii_svg.py
"""

# ---- identity -------------------------------------------------------------
GITHUB_USER = "DonJuanDev"
FULL_NAME = "Juan Pereira"
TAGLINE = "Software Developer · Backend · .NET"

# shell prompt shown in each terminal-style SVG titlebar ("<PROMPT_USER>@github")
PROMPT_USER = "juan"

# First year with contributions. GitHub's public endpoint only serves a rolling
# 12-month window, so fetch_contributions.py walks year-by-year from here to get
# real all-time totals and true streaks (a 1-year window caps streaks at ~366).
ACCOUNT_START_YEAR = 2024

# ---- info card rows -------------------------------------------------------
# ("host",)          -> "<PROMPT_USER>@github" + rule
# ("kv", key, value) -> orange key + light value
# ("sec", title)     -> blue section header
# ("bul", text)      -> green bullet
# ("gap",)           -> vertical space
ROWS = [
    ("host",),
    ("kv", "Now", "Software Developer · Backend"),
    ("kv", "Building", "AmericanCut — systems & ops"),
    ("kv", "Also", "Full-stack web products"),
    ("kv", "Edu", "Computer Programming"),
    ("kv", "Exp", "4+ years shipping software"),
    ("gap",),
    ("sec", "Stack"),
    ("kv", "Lang", "C#, TypeScript, JavaScript"),
    ("kv", "Backend", ".NET, Docker, AWS, MongoDB"),
    ("kv", "Tools", "Git, ClaudeCode, Datadog, VS"),
    ("kv", "Also", "PHP, HTML/CSS, Node"),
    ("gap",),
    ("sec", "Highlights"),
    ("bul", "CDM Central"),
    ("bul", "Xcord"),
]
