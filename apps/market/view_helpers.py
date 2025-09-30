from typing import Any

from apps.market.models.market_group_with_types import MarketGroupWithTypes


# @cached_as(MarketGroup, timeout=3600, lock=True)
def build_market_tree() -> list[dict[str, Any]]:
    # Fetch all rows from the view
    rows = list(
        MarketGroupWithTypes.objects.all().values(
            'market_group_id',
            'market_group_name',
            'parent_group_id',
            'type_id',
            'type_name',
        )
    )

    # Build group map
    group_map = {}
    for row in rows:
        mgid = row['market_group_id']
        if mgid not in group_map:
            group_map[mgid] = {
                'id': mgid,
                'name': row['market_group_name'],
                'parent_group_id': row['parent_group_id'],
                'children': [],
                'market_items': [],
            }
        # Attach type if present
        if row['type_id']:
            group_map[mgid]['market_items'].append(
                {'id': row['type_id'], 'item_name': row['type_name']}
            )

    # Attach children in a single pass, no recursion
    for group in group_map.values():
        parent_id = group['parent_group_id']
        if parent_id and parent_id in group_map and parent_id != group['id']:
            group_map[parent_id]['children'].append(group)

    # Collect root groups
    return [group for group in group_map.values() if group['parent_group_id'] is None]


def flatten_tree(groups, level=0):
    flat = []
    for group in groups:
        flat.append(
            {
                'id': group['id'],
                'name': group['name'],
                'level': level,
                'market_items': group.get('market_items', []),
                'margin_left': (level + 1) * 20,
            }
        )
        flat.extend(flatten_tree(group['children'], level + 1))
    return flat
