import subprocess

import pytest

pytest.importorskip("rich")
pytest.importorskip("sp_repo_review")


def test_cmd_help():
    subprocess.run(["repo-review", "--help"], check=True)


def test_cmd_basic():
    subprocess.run(["repo-review", "."], check=True)


def test_cmd_html():
    subprocess.run(
        ["repo-review", ".", "--format", "html", "--stderr", "html"], check=True
    )


def test_cmd_json():
    subprocess.run(
        ["repo-review", ".", "--format", "json", "--stderr", "json"], check=True
    )


def test_cmd_svg():
    subprocess.run(
        ["repo-review", ".", "--format", "svg", "--stderr", "svg"], check=True
    )
