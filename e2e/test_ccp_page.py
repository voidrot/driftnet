import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect


@pytest.mark.playwright
def test_ccp_page_content(page: Page, live_server):
    page.goto(live_server + '/ccp')
    expect(
        page.get_by_role('heading', name='CCP / EVE Online Resources', exact=True)
    ).to_be_visible()
    expect(page.get_by_text('Last updated:')).to_be_visible()
    expect(
        page.get_by_text(
            'EVE Online, the EVE logo, and related marks are owned by CCP Games.'
        )
    ).to_be_visible()
    expect(
        page.get_by_text(
            'driftnet is an independent community project and is not affiliated with, endorsed by, or sponsored by CCP Games.'
        )
    ).to_be_visible()
    expect(
        page.get_by_text(
            "Official Trademarks: you are permitted to use CCP's official trademarks only when they remain unchanged — do not stretch, deform, recolor, or otherwise modify the marks or logos in any way."
        )
    ).to_be_visible()
    expect(page.get_by_text('Required disclaimer:')).to_be_visible()
    expect(
        page.get_by_text(
            'This material is used with limited permission of CCP Games. No official affiliation or endorsement by CCP Games is stated or implied.'
        )
    ).to_be_visible()
    expect(
        page.get_by_text(
            'any EVE-related artwork, screenshots, characters, logos, or other recognizable features shown on this site are the property of CCP Games and are used here for informational and community purposes only (non-commercial).'
        )
    ).to_be_visible()
    expect(
        page.get_by_text(
            'If you represent CCP and have concerns about material on this site, or if you believe any content infringes your rights, please contact us at'
        )
    ).to_be_visible()
    expect(page.get_by_role('link', name='support@driftnet.example')).to_be_visible()
    expect(page.get_by_role('link', name='CCP Legal')).to_be_visible()
