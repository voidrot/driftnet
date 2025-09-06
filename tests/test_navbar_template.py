from pathlib import Path

from django.template import Context, Template


def render_template_for_user(username=None):
    path = Path('apps/templates/base.html')
    with path.open() as fh:
        tpl = Template(fh.read())

    user_like = type(
        'U',
        (),
        {
            'is_authenticated': bool(username),
            'username': username,
        },
    )
    ctx = Context({'user': user_like})
    return tpl.render(ctx)


def test_navbar_shows_dropdown_for_authenticated_user():
    out = render_template_for_user('alice')
    assert 'Open user menu' in out
    assert 'Profile' in out
    assert 'Logout' in out


def test_navbar_shows_login_links_for_anonymous_user():
    out = render_template_for_user(None)
    assert 'Login' in out
    assert 'Sign Up' in out
