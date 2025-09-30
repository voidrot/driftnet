from django.shortcuts import render

from apps.market.view_helpers import build_market_tree


# Create your views here.
def market_index(request):
    market_groups = build_market_tree()
    return render(
        request,
        'market-index.html',
        {'market_groups': market_groups},
    )
