from django.db import migrations

VIEW_SQL = """
CREATE OR REPLACE VIEW market_group_with_types AS
SELECT
    mg.id AS market_group_id,
    mg.name_id->>'en' AS market_group_name,
    mg.parent_group_id,
    t.id AS type_id,
    t.name->>'en' AS type_name
FROM sde_marketgroup mg
LEFT JOIN sde_type t ON t.market_group_id = mg.id;
"""

DROP_VIEW_SQL = """
DROP VIEW IF EXISTS market_group_with_types;
"""


class Migration(migrations.Migration):
    dependencies = [
        # Update this to the latest migration in market app if needed
    ]

    operations = [
        migrations.RunSQL(VIEW_SQL, DROP_VIEW_SQL),
    ]
