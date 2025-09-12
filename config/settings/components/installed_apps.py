DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.forms',
]

PROJECT_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.sde.apps.SdeConfig',
    'apps.esi_utils.apps.EsiUtilsConfig',
    'apps.dashboard.apps.DashboardConfig',
    'apps.alliance.apps.AllianceConfig',
    'apps.asset.apps.AssetConfig',
    'apps.character.apps.CharacterConfig',
    'apps.clones.apps.ClonesConfig',
    'apps.contacts.apps.ContactsConfig',
    'apps.contracts.apps.ContractsConfig',
    'apps.corporation.apps.CorporationConfig',
    'apps.faction_warfare.apps.FactionWarfareConfig',
    'apps.fittings.apps.FittingsConfig',
    'apps.fleets.apps.FleetsConfig',
    'apps.incursions.apps.IncursionsConfig',
    'apps.industry.apps.IndustryConfig',
    'apps.insurance.apps.InsuranceConfig',
    'apps.killmails.apps.KillmailsConfig',
    'apps.location.apps.LocationConfig',
    'apps.loyalty.apps.LoyaltyConfig',
    'apps.mail.apps.MailConfig',
    'apps.market.apps.MarketConfig',
    'apps.planetary_interaction.apps.PlanetaryInteractionConfig',
    'apps.skills.apps.SkillsConfig',
    'apps.sovereignty.apps.SovereigntyConfig',
    'apps.wallet.apps.WalletConfig',
    'apps.wars.apps.WarsConfig',
]

THIRD_PARTY_APPS = [
    'django_tailwind_cli',
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.socialaccount',
    'django_celery_results',
    'django_celery_beat',
    'esi',
]

INSTALLED_APPS = [*DJANGO_APPS, *THIRD_PARTY_APPS, *PROJECT_APPS]
