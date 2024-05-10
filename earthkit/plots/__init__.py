# Copyright 2024, European Centre for Medium Range Weather Forecasts.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import os

from matplotlib import font_manager, rcParams
import matplotlib.pyplot as plt

from earthkit.plots import styles
from earthkit.plots.components.figures import Figure
from earthkit.plots.components.maps import Map
from earthkit.plots.components.subplots import Subplot
from earthkit.plots.definitions import FONTS_DIR, SCHEMA_DIR
from earthkit.plots.schemas import schema

try:
    # NOTE: the `version.py` file must not be present in the git repository
    #   as it is generated by setuptools at install time
    from .version import __version__
except ImportError:  # pragma: no cover
    # Local copy or not installed with setuptools
    __version__ = "999"


__all__ = [
    "Figure",
    "Subplot",
    "Map",
    "schema",
    "styles",
]


def _quickplot(function):
    def wrapper(*args, **kwargs):
        figure = Figure()
        subplot = figure.add_subplot(0, 0)
        getattr(subplot, function.__name__)(*args, **kwargs)
        return subplot

    return wrapper


@_quickplot
def line(*args, **kwargs):
    """Quick plot"""


@_quickplot
def bar(*args, **kwargs):
    """Quick plot"""


@_quickplot
def scatter(*args, **kwargs):
    """Quick plot"""


@_quickplot
def block(*args, **kwargs):
    """Quick plot"""


@_quickplot
def contour(*args, **kwargs):
    """Quick plot"""


@_quickplot
def contourf(*args, **kwargs):
    """Quick plot"""


def register_fonts():
    fontpaths = glob.glob(os.path.join(FONTS_DIR, "*"))
    for fontpath in fontpaths:
        font_files = glob.glob(os.path.join(fontpath, "*.ttf"))
        for font_file in font_files:
            font_manager.fontManager.addfont(font_file)


register_fonts()
# rcParams["font.family"] = schema.font
# rcParams["text.color"] = "#333"
# rcParams["axes.linewidth"] = 0.75
# rcParams["axes.edgecolor"] = "#aaa"
