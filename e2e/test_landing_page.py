import pytest
from playwright.sync_api import Page


@pytest.mark.playwright
def test_homepage_flow(page: Page, live_server):
    page.goto(live_server + '/')
    assert 'Welcome' in page.title()
