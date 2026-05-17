"""Shared dataclasses for the regenerate pipeline.

Kept in a separate module so the per-section content files
(`_content_math.py`, `_content_overview.py`, `_content_history.py`) can
import from it without forming a circular import with `regenerate.py`.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Paper:
    title: str
    authors: str
    year: str
    url: str
    summary: str
    venue: str = ""


@dataclass
class Extra:
    label: str
    url: str


@dataclass
class Chapter:
    id: int
    slug: str
    part: str
    title: str
    summary_html: str
    papers: list[Paper] = field(default_factory=list)
    extras: list[Extra] = field(default_factory=list)
