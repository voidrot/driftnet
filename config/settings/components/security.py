# from csp.constants import NONE
# from csp.constants import SELF

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = 'DENY'

# === Django CSP Configuration ===
# CONTENT_SECURITY_POLICY = {
#     'EXCLUDE_URL_PREFIXES': ['/admin/'],
#     'DIRECTIVES': {
#         'default-src': [SELF, 'cdn.example.net'],
#         'frame-ancestors': [SELF],
#         'form-action': [SELF],
#         'report-uri': '/csp-report/',
#     },
# }

# CONTENT_SECURITY_POLICY_REPORT_ONLY = {
#     'EXCLUDE_URL_PREFIXES': ['/admin/'],
#     'DIRECTIVES': {
#         'default-src': [NONE],
#         'connect-src': [SELF],
#         'img-src': [SELF, 'https://images.evetech.net', 'data:'],
#         'form-action': [SELF],
#         'frame-ancestors': [SELF],
#         'script-src': [SELF, 'https://cdn.jsdelivr.net'],
#         'style-src': [SELF, 'sha256-faU7yAF8NxuMTNEwVmBz+VcYeIoBQ2EMHW3WaVxCvnk='],
#         # 'upgrade-insecure-requests': True,
#         # 'report-uri': '/csp-report/',
#     },
# }
