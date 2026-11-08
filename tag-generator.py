
#!/usr/bin/env python3

"""
Generate Jekyll tag pages from post YAML front matter.
Requires: pip install pyyaml
"""

from pathlib import Path
from collections import defaultdict
import yaml

POST_DIR = Path("_posts")
TAG_DIR = Path("tag")

tags_to_posts = defaultdict(list)

# Read post front matter
for post in sorted(POST_DIR.glob("*.md")):
    content = post.read_text(encoding="utf-8-sig")
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        continue

    try:
        end = next(
            i for i in range(1, len(lines))
            if lines[i].strip() == "---"
        )
    except StopIteration:
        print(f"WARNING: Unclosed front matter: {post}")
        continue

    metadata = yaml.safe_load(
        "\n".join(lines[1:end])
    ) or {}

    raw_tags = metadata.get("tags", [])

    if isinstance(raw_tags, str):
        tags = raw_tags.split()
    elif isinstance(raw_tags, list):
        tags = [str(t) for t in raw_tags]
    else:
        raise ValueError(f"Invalid tags in {post}")

    for tag in tags:
        tag = tag.strip()
        if tag:
            tags_to_posts[tag].append(post.name)

# Display discovered tags
print("\nTags discovered:\n")

for tag, posts in sorted(tags_to_posts.items()):
    print(f"{tag} ({len(posts)} posts)")
    for post in posts:
        print(f"    {post}")

# Validate filenames before modifying anything
for tag in tags_to_posts:
    if tag in (".", "..") or "/" in tag or "\\" in tag:
        raise ValueError(f"Unsafe tag filename: {tag!r}")

# Remove old generated pages
TAG_DIR.mkdir(exist_ok=True)

for old_file in TAG_DIR.glob("*.md"):
    old_file.unlink()

# Generate new tag pages
for tag in sorted(tags_to_posts):
    output = TAG_DIR / f"{tag}.md"

    front_matter = {
        "layout": "tagpage",
        "title": f"Tag: {tag}",
        "tag": tag,
        "robots": "noindex"
    }

    output.write_text(
        "---\n"
        + yaml.safe_dump(
            front_matter,
            sort_keys=False,
            allow_unicode=True
        )
        + "---\n",
        encoding="utf-8"
    )

print(f"\nGenerated {len(tags_to_posts)} tag pages.")
