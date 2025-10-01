from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.market.view_helpers import build_market_tree


# Create your views here.
def market_index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'market-index.html',
    )


@require_GET
def item_details(request: HttpRequest, item_id: int) -> HttpResponse:
    # Placeholder implementation for item details
    # In a real application, you would fetch item details from the database
    item = {
        'id': item_id,
        'name': f'Item {item_id}',
        'description': f'Description for item {item_id}',
        'price': f'${item_id * 10}.00',
    }
    return render(
        request,
        'partials/market-item-details.html',
        context=item,
    )


@require_GET
def market_sidebar(request: HttpRequest) -> HttpResponse:
    market_groups = build_market_tree()
    return render(
        request,
        'partials/market-sidebar.html',
        {'market_groups': market_groups},
    )
