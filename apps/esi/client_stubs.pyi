# flake8: noqa=E501
# Auto Generated do not edit
from typing import Any

from esi.openapi_clients import ESIClientOperation
from esi.models import Token

class GetAlliancesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """List all active player alliances"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """List all active player alliances"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """List all active player alliances"""
        ...

class GetAlliancesAllianceIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Public information about an alliance"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Public information about an alliance"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Public information about an alliance"""
        ...

class GetAlliancesAllianceIdCorporationsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """List all current member corporations of an alliance"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """List all current member corporations of an alliance"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """List all current member corporations of an alliance"""
        ...

class GetAlliancesAllianceIdIconsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get the icon urls for a alliance  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the icon urls for a alliance  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the icon urls for a alliance  This route expires daily at 11:05"""
        ...

class GetCharactersCharacterIdAssetsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of the characters assets"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of the characters assets"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of the characters assets"""
        ...

class GetCorporationsCorporationIdAssetsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of the corporation assets"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of the corporation assets"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of the corporation assets"""
        ...

class PostCharactersCharacterIdAssetsLocationsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

class PostCharactersCharacterIdAssetsNamesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
        ...

class PostCorporationsCorporationIdAssetsLocationsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

class PostCorporationsCorporationIdAssetsNamesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
        ...

class GetCharactersCharacterIdCalendarOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
        ...

class GetCharactersCharacterIdCalendarEventIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get all the information for a specific event"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get all the information for a specific event"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get all the information for a specific event"""
        ...

class GetCharactersCharacterIdCalendarEventIdAttendeesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get all invited attendees for a given event"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get all invited attendees for a given event"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get all invited attendees for a given event"""
        ...

class PutCharactersCharacterIdCalendarEventIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Set your response status to an event"""
        ...

class GetCharactersCharacterIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Public information about a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Public information about a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Public information about a character"""
        ...

class GetCharactersCharacterIdAgentsResearchOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
        ...

class GetCharactersCharacterIdBlueprintsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of blueprints the character owns"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of blueprints the character owns"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of blueprints the character owns"""
        ...

class GetCharactersCharacterIdCorporationhistoryOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of all the corporations a character has been a member of"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of all the corporations a character has been a member of"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of all the corporations a character has been a member of"""
        ...

class GetCharactersCharacterIdFatigueOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return a character's jump activation and fatigue information"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a character's jump activation and fatigue information"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a character's jump activation and fatigue information"""
        ...

class GetCharactersCharacterIdMedalsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of medals the character has"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of medals the character has"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of medals the character has"""
        ...

class GetCharactersCharacterIdNotificationsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return character notifications"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return character notifications"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return character notifications"""
        ...

class GetCharactersCharacterIdNotificationsContactsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return notifications about having been added to someone's contact list"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return notifications about having been added to someone's contact list"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return notifications about having been added to someone's contact list"""
        ...

class GetCharactersCharacterIdPortraitOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get portrait urls for a character  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get portrait urls for a character  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get portrait urls for a character  This route expires daily at 11:05"""
        ...

class GetCharactersCharacterIdRolesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Returns a character's corporation roles"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a character's corporation roles"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a character's corporation roles"""
        ...

class GetCharactersCharacterIdStandingsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return character standings from agents, NPC corporations, and factions"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return character standings from agents, NPC corporations, and factions"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return character standings from agents, NPC corporations, and factions"""
        ...

class GetCharactersCharacterIdTitlesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a character's titles"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a character's titles"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a character's titles"""
        ...

class PostCharactersAffiliationOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Bulk lookup of character IDs to corporation, alliance and faction"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Bulk lookup of character IDs to corporation, alliance and faction"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Bulk lookup of character IDs to corporation, alliance and faction"""
        ...

class PostCharactersCharacterIdCspaOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> float:
        """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[float]:
        """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[float]]:
        """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
        ...

class GetCharactersCharacterIdClonesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """A list of the character's clones"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """A list of the character's clones"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """A list of the character's clones"""
        ...

class GetCharactersCharacterIdImplantsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return implants on the active clone of a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return implants on the active clone of a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Return implants on the active clone of a character"""
        ...

class DeleteCharactersCharacterIdContactsOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Bulk delete contacts"""
        ...

class GetAlliancesAllianceIdContactsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return contacts of an alliance"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return contacts of an alliance"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return contacts of an alliance"""
        ...

class GetAlliancesAllianceIdContactsLabelsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return custom labels for an alliance's contacts"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return custom labels for an alliance's contacts"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return custom labels for an alliance's contacts"""
        ...

class GetCharactersCharacterIdContactsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return contacts of a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return contacts of a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return contacts of a character"""
        ...

class GetCharactersCharacterIdContactsLabelsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return custom labels for a character's contacts"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return custom labels for a character's contacts"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return custom labels for a character's contacts"""
        ...

class GetCorporationsCorporationIdContactsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return contacts of a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return contacts of a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return contacts of a corporation"""
        ...

class GetCorporationsCorporationIdContactsLabelsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return custom labels for a corporation's contacts"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return custom labels for a corporation's contacts"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return custom labels for a corporation's contacts"""
        ...

class PostCharactersCharacterIdContactsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Bulk add contacts with same settings"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Bulk add contacts with same settings"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Bulk add contacts with same settings"""
        ...

class PutCharactersCharacterIdContactsOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Bulk edit contacts with same settings"""
        ...

class GetCharactersCharacterIdContractsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

class GetCharactersCharacterIdContractsContractIdBidsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists bids on a particular auction contract"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists bids on a particular auction contract"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists bids on a particular auction contract"""
        ...

class GetCharactersCharacterIdContractsContractIdItemsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists items of a particular contract"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists items of a particular contract"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists items of a particular contract"""
        ...

class GetContractsPublicBidsContractIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists bids on a public auction contract"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists bids on a public auction contract"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists bids on a public auction contract"""
        ...

class GetContractsPublicItemsContractIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists items of a public contract"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists items of a public contract"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists items of a public contract"""
        ...

class GetContractsPublicRegionIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a paginated list of all public contracts in the given region"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a paginated list of all public contracts in the given region"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a paginated list of all public contracts in the given region"""
        ...

class GetCorporationsCorporationIdContractsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

class GetCorporationsCorporationIdContractsContractIdBidsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists bids on a particular auction contract"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists bids on a particular auction contract"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists bids on a particular auction contract"""
        ...

class GetCorporationsCorporationIdContractsContractIdItemsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists items of a particular contract"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Lists items of a particular contract"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Lists items of a particular contract"""
        ...

class GetCorporationsCorporationIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Public information about a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Public information about a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Public information about a corporation"""
        ...

class GetCorporationsCorporationIdAlliancehistoryOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of all the alliances a corporation has been a member of"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of all the alliances a corporation has been a member of"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of all the alliances a corporation has been a member of"""
        ...

class GetCorporationsCorporationIdBlueprintsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a list of blueprints the corporation owns"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a list of blueprints the corporation owns"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a list of blueprints the corporation owns"""
        ...

class GetCorporationsCorporationIdContainersLogsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
        ...

class GetCorporationsCorporationIdDivisionsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
        ...

class GetCorporationsCorporationIdFacilitiesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a corporation's facilities"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a corporation's facilities"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a corporation's facilities"""
        ...

class GetCorporationsCorporationIdIconsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get the icon urls for a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the icon urls for a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the icon urls for a corporation"""
        ...

class GetCorporationsCorporationIdMedalsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a corporation's medals"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a corporation's medals"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a corporation's medals"""
        ...

class GetCorporationsCorporationIdMedalsIssuedOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns medals issued by a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns medals issued by a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns medals issued by a corporation"""
        ...

class GetCorporationsCorporationIdMembersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
        ...

class GetCorporationsCorporationIdMembersLimitOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> int:
        """Return a corporation's member limit, not including CEO himself"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return a corporation's member limit, not including CEO himself"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Return a corporation's member limit, not including CEO himself"""
        ...

class GetCorporationsCorporationIdMembersTitlesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a corporation's members' titles"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a corporation's members' titles"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a corporation's members' titles"""
        ...

class GetCorporationsCorporationIdMembertrackingOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns additional information about a corporation's members which helps tracking their activities"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns additional information about a corporation's members which helps tracking their activities"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns additional information about a corporation's members which helps tracking their activities"""
        ...

class GetCorporationsCorporationIdRolesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the roles of all members if the character has the personnel manager role or any grantable role."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the roles of all members if the character has the personnel manager role or any grantable role."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return the roles of all members if the character has the personnel manager role or any grantable role."""
        ...

class GetCorporationsCorporationIdRolesHistoryOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return how roles have changed for a coporation's members, up to a month"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return how roles have changed for a coporation's members, up to a month"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return how roles have changed for a coporation's members, up to a month"""
        ...

class GetCorporationsCorporationIdShareholdersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the current shareholders of a corporation."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the current shareholders of a corporation."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return the current shareholders of a corporation."""
        ...

class GetCorporationsCorporationIdStandingsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return corporation standings from agents, NPC corporations, and factions"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return corporation standings from agents, NPC corporations, and factions"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return corporation standings from agents, NPC corporations, and factions"""
        ...

class GetCorporationsCorporationIdStarbasesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns list of corporation starbases (POSes)"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns list of corporation starbases (POSes)"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns list of corporation starbases (POSes)"""
        ...

class GetCorporationsCorporationIdStarbasesStarbaseIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Returns various settings and fuels of a starbase (POS)"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns various settings and fuels of a starbase (POS)"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns various settings and fuels of a starbase (POS)"""
        ...

class GetCorporationsCorporationIdStructuresOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
        ...

class GetCorporationsCorporationIdTitlesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a corporation's titles"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a corporation's titles"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a corporation's titles"""
        ...

class GetCorporationsNpccorpsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of npc corporations  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of npc corporations  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of npc corporations  This route expires daily at 11:05"""
        ...

class GetCorporationsProjectsContributionOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Show your contribution to a corporation project."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Show your contribution to a corporation project."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Show your contribution to a corporation project."""
        ...

class GetCorporationsProjectsContributorsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Listing of all contributors to a corporation project."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Listing of all contributors to a corporation project."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Listing of all contributors to a corporation project."""
        ...

class GetCorporationsProjectsDetailOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get the details of a corporation project."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the details of a corporation project."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the details of a corporation project."""
        ...

class GetCorporationsProjectsListingOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Listing of all (active) corporation projects."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Listing of all (active) corporation projects."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Listing of all (active) corporation projects."""
        ...

class GetDogmaAttributesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of dogma attribute ids  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of dogma attribute ids  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of dogma attribute ids  This route expires daily at 11:05"""
        ...

class GetDogmaAttributesAttributeIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a dogma attribute  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a dogma attribute  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a dogma attribute  This route expires daily at 11:05"""
        ...

class GetDogmaDynamicItemsTypeIdItemIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
        ...

class GetDogmaEffectsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of dogma effect ids  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of dogma effect ids  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of dogma effect ids  This route expires daily at 11:05"""
        ...

class GetDogmaEffectsEffectIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a dogma effect  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a dogma effect  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a dogma effect  This route expires daily at 11:05"""
        ...

class GetCharactersCharacterIdFwStatsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
        ...

class GetCorporationsCorporationIdFwStatsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
        ...

class GetFwLeaderboardsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

class GetFwLeaderboardsCharactersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

class GetFwLeaderboardsCorporationsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

class GetFwStatsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
        ...

class GetFwSystemsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """An overview of the current ownership of faction warfare solar systems"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """An overview of the current ownership of faction warfare solar systems"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """An overview of the current ownership of faction warfare solar systems"""
        ...

class GetFwWarsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Data about which NPC factions are at war  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Data about which NPC factions are at war  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Data about which NPC factions are at war  This route expires daily at 11:05"""
        ...

class DeleteCharactersCharacterIdFittingsFittingIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Delete a fitting from a character"""
        ...

class GetCharactersCharacterIdFittingsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return fittings of a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return fittings of a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return fittings of a character"""
        ...

class PostCharactersCharacterIdFittingsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Save a new fitting for a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Save a new fitting for a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Save a new fitting for a character"""
        ...

class DeleteFleetsFleetIdMembersMemberIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Kick a fleet member"""
        ...

class DeleteFleetsFleetIdSquadsSquadIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Delete a fleet squad, only empty squads can be deleted"""
        ...

class DeleteFleetsFleetIdWingsWingIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty"""
        ...

class GetCharactersCharacterIdFleetOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return the fleet ID the character is in, if any."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the fleet ID the character is in, if any."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return the fleet ID the character is in, if any."""
        ...

class GetFleetsFleetIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return details about a fleet"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return details about a fleet"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return details about a fleet"""
        ...

class GetFleetsFleetIdMembersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return information about fleet members"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return information about fleet members"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return information about fleet members"""
        ...

class GetFleetsFleetIdWingsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return information about wings in a fleet"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return information about wings in a fleet"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return information about wings in a fleet"""
        ...

class PostFleetsFleetIdMembersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
        ...

class PostFleetsFleetIdWingsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Create a new wing in a fleet"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Create a new wing in a fleet"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Create a new wing in a fleet"""
        ...

class PostFleetsFleetIdWingsWingIdSquadsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Create a new squad in a fleet"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Create a new squad in a fleet"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Create a new squad in a fleet"""
        ...

class PutFleetsFleetIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Update settings about a fleet"""
        ...

class PutFleetsFleetIdMembersMemberIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Move a fleet member around"""
        ...

class PutFleetsFleetIdSquadsSquadIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Rename a fleet squad"""
        ...

class PutFleetsFleetIdWingsWingIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Rename a fleet wing"""
        ...

class GetIncursionsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of current incursions"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of current incursions"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of current incursions"""
        ...

class GetCharactersCharacterIdIndustryJobsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List industry jobs placed by a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List industry jobs placed by a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List industry jobs placed by a character"""
        ...

class GetCharactersCharacterIdMiningOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Paginated record of all mining done by a character for the past 30 days"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Paginated record of all mining done by a character for the past 30 days"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Paginated record of all mining done by a character for the past 30 days"""
        ...

class GetCorporationCorporationIdMiningExtractionsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
        ...

class GetCorporationCorporationIdMiningObserversOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Paginated list of all entities capable of observing and recording mining for a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Paginated list of all entities capable of observing and recording mining for a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Paginated list of all entities capable of observing and recording mining for a corporation"""
        ...

class GetCorporationCorporationIdMiningObserversObserverIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Paginated record of all mining seen by an observer"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Paginated record of all mining seen by an observer"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Paginated record of all mining seen by an observer"""
        ...

class GetCorporationsCorporationIdIndustryJobsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List industry jobs run by a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List industry jobs run by a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List industry jobs run by a corporation"""
        ...

class GetIndustryFacilitiesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of industry facilities"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of industry facilities"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of industry facilities"""
        ...

class GetIndustrySystemsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return cost indices for solar systems"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return cost indices for solar systems"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return cost indices for solar systems"""
        ...

class GetInsurancePricesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return available insurance levels for all ship types"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return available insurance levels for all ship types"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return available insurance levels for all ship types"""
        ...

class GetCharactersCharacterIdKillmailsRecentOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of a character's kills and losses going back 90 days"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of a character's kills and losses going back 90 days"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of a character's kills and losses going back 90 days"""
        ...

class GetCorporationsCorporationIdKillmailsRecentOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of a corporation's kills and losses going back 90 days"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of a corporation's kills and losses going back 90 days"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of a corporation's kills and losses going back 90 days"""
        ...

class GetKillmailsKillmailIdKillmailHashOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return a single killmail from its ID and hash"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a single killmail from its ID and hash"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a single killmail from its ID and hash"""
        ...

class GetCharactersCharacterIdLocationOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
        ...

class GetCharactersCharacterIdOnlineOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Checks if the character is currently online"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Checks if the character is currently online"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Checks if the character is currently online"""
        ...

class GetCharactersCharacterIdShipOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get the current ship type, name and id"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the current ship type, name and id"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the current ship type, name and id"""
        ...

class GetCharactersCharacterIdLoyaltyPointsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of loyalty points for all corporations the character has worked for"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of loyalty points for all corporations the character has worked for"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of loyalty points for all corporations the character has worked for"""
        ...

class GetLoyaltyStoresCorporationIdOffersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
        ...

class DeleteCharactersCharacterIdMailLabelsLabelIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Delete a mail label"""
        ...

class DeleteCharactersCharacterIdMailMailIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Delete a mail"""
        ...

class GetCharactersCharacterIdMailOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
        ...

class GetCharactersCharacterIdMailLabelsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return a list of the users mail labels, unread counts for each label and a total unread count."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of the users mail labels, unread counts for each label and a total unread count."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of the users mail labels, unread counts for each label and a total unread count."""
        ...

class GetCharactersCharacterIdMailListsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return all mailing lists that the character is subscribed to"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return all mailing lists that the character is subscribed to"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return all mailing lists that the character is subscribed to"""
        ...

class GetCharactersCharacterIdMailMailIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return the contents of an EVE mail"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return the contents of an EVE mail"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return the contents of an EVE mail"""
        ...

class PostCharactersCharacterIdMailOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> int:
        """Create and send a new mail"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Create and send a new mail"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Create and send a new mail"""
        ...

class PostCharactersCharacterIdMailLabelsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> int:
        """Create a mail label"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Create a mail label"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Create a mail label"""
        ...

class PutCharactersCharacterIdMailMailIdOperation(ESIClientOperation):
    """EsiOperation, use result()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> None:
        """Update metadata about a mail"""
        ...

class GetCharactersCharacterIdOrdersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List open market orders placed by a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List open market orders placed by a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List open market orders placed by a character"""
        ...

class GetCharactersCharacterIdOrdersHistoryOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List cancelled and expired market orders placed by a character up to 90 days in the past."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List cancelled and expired market orders placed by a character up to 90 days in the past."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List cancelled and expired market orders placed by a character up to 90 days in the past."""
        ...

class GetCorporationsCorporationIdOrdersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List open market orders placed on behalf of a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List open market orders placed on behalf of a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List open market orders placed on behalf of a corporation"""
        ...

class GetCorporationsCorporationIdOrdersHistoryOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
        ...

class GetMarketsGroupsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

class GetMarketsGroupsMarketGroupIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

class GetMarketsPricesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of prices"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of prices"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of prices"""
        ...

class GetMarketsRegionIdHistoryOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
        ...

class GetMarketsRegionIdOrdersOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of orders in a region"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of orders in a region"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of orders in a region"""
        ...

class GetMarketsRegionIdTypesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
        ...

class GetMarketsStructuresStructureIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return all orders in a structure"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return all orders in a structure"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return all orders in a structure"""
        ...

class GetMetaChangelogOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get the changelog of this API."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the changelog of this API."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the changelog of this API."""
        ...

class GetMetaCompatibilityDatesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get a list of compatibility dates."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of compatibility dates."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of compatibility dates."""
        ...

class GetCharactersCharacterIdPlanetsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a list of all planetary colonies owned by a character."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns a list of all planetary colonies owned by a character."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns a list of all planetary colonies owned by a character."""
        ...

class GetCharactersCharacterIdPlanetsPlanetIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
        ...

class GetCorporationsCorporationIdCustomsOfficesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List customs offices owned by a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List customs offices owned by a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List customs offices owned by a corporation"""
        ...

class GetUniverseSchematicsSchematicIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a planetary factory schematic"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a planetary factory schematic"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a planetary factory schematic"""
        ...

class GetRouteOriginDestinationOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get the systems between origin and destination"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get the systems between origin and destination"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get the systems between origin and destination"""
        ...

class GetCharactersCharacterIdSearchOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Search for entities that match a given sub-string."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Search for entities that match a given sub-string."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Search for entities that match a given sub-string."""
        ...

class GetCharactersCharacterIdAttributesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return attributes of a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return attributes of a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return attributes of a character"""
        ...

class GetCharactersCharacterIdSkillqueueOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List the configured skill queue for the given character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List the configured skill queue for the given character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List the configured skill queue for the given character"""
        ...

class GetCharactersCharacterIdSkillsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """List all trained skills for the given character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """List all trained skills for the given character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """List all trained skills for the given character"""
        ...

class GetSovereigntyCampaignsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Shows sovereignty data for campaigns."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Shows sovereignty data for campaigns."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Shows sovereignty data for campaigns."""
        ...

class GetSovereigntyMapOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Shows sovereignty information for solar systems"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Shows sovereignty information for solar systems"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Shows sovereignty information for solar systems"""
        ...

class GetSovereigntyStructuresOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Shows sovereignty data for structures."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Shows sovereignty data for structures."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Shows sovereignty data for structures."""
        ...

class GetStatusOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """EVE Server status"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """EVE Server status"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """EVE Server status"""
        ...

class GetUniverseAncestriesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get all character ancestries  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get all character ancestries  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get all character ancestries  This route expires daily at 11:05"""
        ...

class GetUniverseAsteroidBeltsAsteroidBeltIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on an asteroid belt  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on an asteroid belt  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on an asteroid belt  This route expires daily at 11:05"""
        ...

class GetUniverseBloodlinesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of bloodlines  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of bloodlines  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of bloodlines  This route expires daily at 11:05"""
        ...

class GetUniverseCategoriesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of item categories  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of item categories  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of item categories  This route expires daily at 11:05"""
        ...

class GetUniverseCategoriesCategoryIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information of an item category  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information of an item category  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information of an item category  This route expires daily at 11:05"""
        ...

class GetUniverseConstellationsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of constellations  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of constellations  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of constellations  This route expires daily at 11:05"""
        ...

class GetUniverseConstellationsConstellationIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a constellation  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a constellation  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a constellation  This route expires daily at 11:05"""
        ...

class GetUniverseFactionsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of factions  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of factions  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of factions  This route expires daily at 11:05"""
        ...

class GetUniverseGraphicsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of graphics  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of graphics  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of graphics  This route expires daily at 11:05"""
        ...

class GetUniverseGraphicsGraphicIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a graphic  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a graphic  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a graphic  This route expires daily at 11:05"""
        ...

class GetUniverseGroupsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

class GetUniverseGroupsGroupIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

class GetUniverseMoonsMoonIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a moon  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a moon  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a moon  This route expires daily at 11:05"""
        ...

class GetUniversePlanetsPlanetIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a planet  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a planet  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a planet  This route expires daily at 11:05"""
        ...

class GetUniverseRacesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of character races  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a list of character races  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a list of character races  This route expires daily at 11:05"""
        ...

class GetUniverseRegionsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of regions  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of regions  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of regions  This route expires daily at 11:05"""
        ...

class GetUniverseRegionsRegionIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a region  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a region  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a region  This route expires daily at 11:05"""
        ...

class GetUniverseStargatesStargateIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a stargate  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a stargate  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a stargate  This route expires daily at 11:05"""
        ...

class GetUniverseStarsStarIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a star  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a star  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a star  This route expires daily at 11:05"""
        ...

class GetUniverseStationsStationIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a station  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a station  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a station  This route expires daily at 11:05"""
        ...

class GetUniverseStructuresOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """List all public structures"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """List all public structures"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """List all public structures"""
        ...

class GetUniverseStructuresStructureIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
        ...

class GetUniverseSystemJumpsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
        ...

class GetUniverseSystemKillsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
        ...

class GetUniverseSystemsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of solar systems  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of solar systems  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of solar systems  This route expires daily at 11:05"""
        ...

class GetUniverseSystemsSystemIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a solar system.  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a solar system.  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a solar system.  This route expires daily at 11:05"""
        ...

class GetUniverseTypesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of type ids  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Get a list of type ids  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Get a list of type ids  This route expires daily at 11:05"""
        ...

class GetUniverseTypesTypeIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Get information on a type  This route expires daily at 11:05"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get information on a type  This route expires daily at 11:05"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get information on a type  This route expires daily at 11:05"""
        ...

class PostUniverseIdsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
        ...

class PostUniverseNamesOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
        ...

class PostUiAutopilotWaypointOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Set a solar system as autopilot waypoint"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Set a solar system as autopilot waypoint"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Set a solar system as autopilot waypoint"""
        ...

class PostUiOpenwindowContractOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Open the contract window inside the client"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Open the contract window inside the client"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Open the contract window inside the client"""
        ...

class PostUiOpenwindowInformationOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Open the information window for a character, corporation or alliance inside the client"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Open the information window for a character, corporation or alliance inside the client"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Open the information window for a character, corporation or alliance inside the client"""
        ...

class PostUiOpenwindowMarketdetailsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Open the market details window for a specific typeID inside the client"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Open the market details window for a specific typeID inside the client"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Open the market details window for a specific typeID inside the client"""
        ...

class PostUiOpenwindowNewmailOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any:
        """Open the New Mail window, according to settings from the request if applicable"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]:
        """Open the New Mail window, according to settings from the request if applicable"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[Any]]:
        """Open the New Mail window, according to settings from the request if applicable"""
        ...

class GetCharactersCharacterIdWalletOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> float:
        """Returns a character's wallet balance"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[float]:
        """Returns a character's wallet balance"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[float]]:
        """Returns a character's wallet balance"""
        ...

class GetCharactersCharacterIdWalletJournalOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Retrieve the given character's wallet journal going 30 days back"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Retrieve the given character's wallet journal going 30 days back"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Retrieve the given character's wallet journal going 30 days back"""
        ...

class GetCharactersCharacterIdWalletTransactionsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get wallet transactions of a character"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get wallet transactions of a character"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get wallet transactions of a character"""
        ...

class GetCorporationsCorporationIdWalletsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a corporation's wallets"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get a corporation's wallets"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get a corporation's wallets"""
        ...

class GetCorporationsCorporationIdWalletsDivisionJournalOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
        ...

class GetCorporationsCorporationIdWalletsDivisionTransactionsOperation(
    ESIClientOperation
):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get wallet transactions of a corporation"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Get wallet transactions of a corporation"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Get wallet transactions of a corporation"""
        ...

class GetWarsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return a list of wars"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]:
        """Return a list of wars"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[int]]:
        """Return a list of wars"""
        ...

class GetWarsWarIdOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]:
        """Return details about a war"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return details about a war"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return details about a war"""
        ...

class GetWarsWarIdKillmailsOperation(ESIClientOperation):
    """EsiOperation, use result(), results() or results_localized()"""
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of kills related to a war"""
        ...

    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]:
        """Return a list of kills related to a war"""
        ...

    def results_localized(
        self, languages: list[str] | str | None = None, **extra
    ) -> dict[str, list[dict[str, Any]]]:
        """Return a list of kills related to a war"""
        ...

class ESIClientStub:
    class _Alliance:
        def GetAlliances(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesOperation:
            """List all active player alliances"""
            ...

        def GetAlliancesAllianceId(
            self,
            alliance_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdOperation:
            """Public information about an alliance"""
            ...

        def GetAlliancesAllianceIdCorporations(
            self,
            alliance_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdCorporationsOperation:
            """List all current member corporations of an alliance"""
            ...

        def GetAlliancesAllianceIdIcons(
            self,
            alliance_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdIconsOperation:
            """Get the icon urls for a alliance  This route expires daily at 11:05"""
            ...

    Alliance: _Alliance = _Alliance()

    class _Assets:
        def GetCharactersCharacterIdAssets(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdAssetsOperation:
            """Return a list of the characters assets"""
            ...

        def GetCorporationsCorporationIdAssets(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdAssetsOperation:
            """Return a list of the corporation assets"""
            ...

        def PostCharactersCharacterIdAssetsLocations(
            self,
            body: list[int],
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdAssetsLocationsOperation:
            """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
            ...

        def PostCharactersCharacterIdAssetsNames(
            self,
            body: list[int],
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdAssetsNamesOperation:
            """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
            ...

        def PostCorporationsCorporationIdAssetsLocations(
            self,
            body: list[int],
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCorporationsCorporationIdAssetsLocationsOperation:
            """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
            ...

        def PostCorporationsCorporationIdAssetsNames(
            self,
            body: list[int],
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCorporationsCorporationIdAssetsNamesOperation:
            """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
            ...

    Assets: _Assets = _Assets()

    class _Calendar:
        def GetCharactersCharacterIdCalendar(
            self,
            character_id: int,
            token: Token,
            from_event: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdCalendarOperation:
            """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
            ...

        def GetCharactersCharacterIdCalendarEventId(
            self,
            character_id: int,
            event_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdCalendarEventIdOperation:
            """Get all the information for a specific event"""
            ...

        def GetCharactersCharacterIdCalendarEventIdAttendees(
            self,
            character_id: int,
            event_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdCalendarEventIdAttendeesOperation:
            """Get all invited attendees for a given event"""
            ...

        def PutCharactersCharacterIdCalendarEventId(
            self,
            body: dict[str, Any],
            character_id: int,
            event_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutCharactersCharacterIdCalendarEventIdOperation:
            """Set your response status to an event"""
            ...

    Calendar: _Calendar = _Calendar()

    class _Character:
        def GetCharactersCharacterId(
            self,
            character_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdOperation:
            """Public information about a character"""
            ...

        def GetCharactersCharacterIdAgentsResearch(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdAgentsResearchOperation:
            """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
            ...

        def GetCharactersCharacterIdBlueprints(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdBlueprintsOperation:
            """Return a list of blueprints the character owns"""
            ...

        def GetCharactersCharacterIdCorporationhistory(
            self,
            character_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdCorporationhistoryOperation:
            """Get a list of all the corporations a character has been a member of"""
            ...

        def GetCharactersCharacterIdFatigue(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFatigueOperation:
            """Return a character's jump activation and fatigue information"""
            ...

        def GetCharactersCharacterIdMedals(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMedalsOperation:
            """Return a list of medals the character has"""
            ...

        def GetCharactersCharacterIdNotifications(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdNotificationsOperation:
            """Return character notifications"""
            ...

        def GetCharactersCharacterIdNotificationsContacts(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdNotificationsContactsOperation:
            """Return notifications about having been added to someone's contact list"""
            ...

        def GetCharactersCharacterIdPortrait(
            self,
            character_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdPortraitOperation:
            """Get portrait urls for a character  This route expires daily at 11:05"""
            ...

        def GetCharactersCharacterIdRoles(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdRolesOperation:
            """Returns a character's corporation roles"""
            ...

        def GetCharactersCharacterIdStandings(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdStandingsOperation:
            """Return character standings from agents, NPC corporations, and factions"""
            ...

        def GetCharactersCharacterIdTitles(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdTitlesOperation:
            """Returns a character's titles"""
            ...

        def PostCharactersAffiliation(
            self,
            body: list[int],
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersAffiliationOperation:
            """Bulk lookup of character IDs to corporation, alliance and faction"""
            ...

        def PostCharactersCharacterIdCspa(
            self,
            body: list[int],
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdCspaOperation:
            """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
            ...

    Character: _Character = _Character()

    class _Clones:
        def GetCharactersCharacterIdClones(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdClonesOperation:
            """A list of the character's clones"""
            ...

        def GetCharactersCharacterIdImplants(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdImplantsOperation:
            """Return implants on the active clone of a character"""
            ...

    Clones: _Clones = _Clones()

    class _Contacts:
        def DeleteCharactersCharacterIdContacts(
            self,
            character_id: int,
            contact_ids: list[Any],
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteCharactersCharacterIdContactsOperation:
            """Bulk delete contacts"""
            ...

        def GetAlliancesAllianceIdContacts(
            self,
            alliance_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdContactsOperation:
            """Return contacts of an alliance"""
            ...

        def GetAlliancesAllianceIdContactsLabels(
            self,
            alliance_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdContactsLabelsOperation:
            """Return custom labels for an alliance's contacts"""
            ...

        def GetCharactersCharacterIdContacts(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdContactsOperation:
            """Return contacts of a character"""
            ...

        def GetCharactersCharacterIdContactsLabels(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdContactsLabelsOperation:
            """Return custom labels for a character's contacts"""
            ...

        def GetCorporationsCorporationIdContacts(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContactsOperation:
            """Return contacts of a corporation"""
            ...

        def GetCorporationsCorporationIdContactsLabels(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContactsLabelsOperation:
            """Return custom labels for a corporation's contacts"""
            ...

        def PostCharactersCharacterIdContacts(
            self,
            body: list[int],
            character_id: int,
            standing: float,
            token: Token,
            label_ids: list[Any] | None = ...,
            watched: bool | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdContactsOperation:
            """Bulk add contacts with same settings"""
            ...

        def PutCharactersCharacterIdContacts(
            self,
            body: list[int],
            character_id: int,
            standing: float,
            token: Token,
            label_ids: list[Any] | None = ...,
            watched: bool | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutCharactersCharacterIdContactsOperation:
            """Bulk edit contacts with same settings"""
            ...

    Contacts: _Contacts = _Contacts()

    class _Contracts:
        def GetCharactersCharacterIdContracts(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdContractsOperation:
            """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
            ...

        def GetCharactersCharacterIdContractsContractIdBids(
            self,
            character_id: int,
            contract_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdContractsContractIdBidsOperation:
            """Lists bids on a particular auction contract"""
            ...

        def GetCharactersCharacterIdContractsContractIdItems(
            self,
            character_id: int,
            contract_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdContractsContractIdItemsOperation:
            """Lists items of a particular contract"""
            ...

        def GetContractsPublicBidsContractId(
            self,
            contract_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetContractsPublicBidsContractIdOperation:
            """Lists bids on a public auction contract"""
            ...

        def GetContractsPublicItemsContractId(
            self,
            contract_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetContractsPublicItemsContractIdOperation:
            """Lists items of a public contract"""
            ...

        def GetContractsPublicRegionId(
            self,
            region_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetContractsPublicRegionIdOperation:
            """Returns a paginated list of all public contracts in the given region"""
            ...

        def GetCorporationsCorporationIdContracts(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContractsOperation:
            """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
            ...

        def GetCorporationsCorporationIdContractsContractIdBids(
            self,
            contract_id: int,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContractsContractIdBidsOperation:
            """Lists bids on a particular auction contract"""
            ...

        def GetCorporationsCorporationIdContractsContractIdItems(
            self,
            contract_id: int,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContractsContractIdItemsOperation:
            """Lists items of a particular contract"""
            ...

    Contracts: _Contracts = _Contracts()

    class _Corporation:
        def GetCorporationsCorporationId(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdOperation:
            """Public information about a corporation"""
            ...

        def GetCorporationsCorporationIdAlliancehistory(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdAlliancehistoryOperation:
            """Get a list of all the alliances a corporation has been a member of"""
            ...

        def GetCorporationsCorporationIdBlueprints(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdBlueprintsOperation:
            """Returns a list of blueprints the corporation owns"""
            ...

        def GetCorporationsCorporationIdContainersLogs(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContainersLogsOperation:
            """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
            ...

        def GetCorporationsCorporationIdDivisions(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdDivisionsOperation:
            """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
            ...

        def GetCorporationsCorporationIdFacilities(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdFacilitiesOperation:
            """Return a corporation's facilities"""
            ...

        def GetCorporationsCorporationIdIcons(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdIconsOperation:
            """Get the icon urls for a corporation"""
            ...

        def GetCorporationsCorporationIdMedals(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMedalsOperation:
            """Returns a corporation's medals"""
            ...

        def GetCorporationsCorporationIdMedalsIssued(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMedalsIssuedOperation:
            """Returns medals issued by a corporation"""
            ...

        def GetCorporationsCorporationIdMembers(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembersOperation:
            """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
            ...

        def GetCorporationsCorporationIdMembersLimit(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembersLimitOperation:
            """Return a corporation's member limit, not including CEO himself"""
            ...

        def GetCorporationsCorporationIdMembersTitles(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembersTitlesOperation:
            """Returns a corporation's members' titles"""
            ...

        def GetCorporationsCorporationIdMembertracking(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembertrackingOperation:
            """Returns additional information about a corporation's members which helps tracking their activities"""
            ...

        def GetCorporationsCorporationIdRoles(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdRolesOperation:
            """Return the roles of all members if the character has the personnel manager role or any grantable role."""
            ...

        def GetCorporationsCorporationIdRolesHistory(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdRolesHistoryOperation:
            """Return how roles have changed for a coporation's members, up to a month"""
            ...

        def GetCorporationsCorporationIdShareholders(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdShareholdersOperation:
            """Return the current shareholders of a corporation."""
            ...

        def GetCorporationsCorporationIdStandings(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdStandingsOperation:
            """Return corporation standings from agents, NPC corporations, and factions"""
            ...

        def GetCorporationsCorporationIdStarbases(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdStarbasesOperation:
            """Returns list of corporation starbases (POSes)"""
            ...

        def GetCorporationsCorporationIdStarbasesStarbaseId(
            self,
            corporation_id: int,
            starbase_id: int,
            system_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdStarbasesStarbaseIdOperation:
            """Returns various settings and fuels of a starbase (POS)"""
            ...

        def GetCorporationsCorporationIdStructures(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdStructuresOperation:
            """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
            ...

        def GetCorporationsCorporationIdTitles(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdTitlesOperation:
            """Returns a corporation's titles"""
            ...

        def GetCorporationsNpccorps(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsNpccorpsOperation:
            """Get a list of npc corporations  This route expires daily at 11:05"""
            ...

    Corporation: _Corporation = _Corporation()

    class _Corporation_Projects:
        def GetCorporationsProjectsContribution(
            self,
            corporation_id: int,
            project_id: str,
            character_id: int,
            token: Token,
            If_Modified_Since: str | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsProjectsContributionOperation:
            """Show your contribution to a corporation project."""
            ...

        def GetCorporationsProjectsContributors(
            self,
            corporation_id: int,
            project_id: str,
            token: Token,
            after: str | None = ...,
            before: str | None = ...,
            limit: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsProjectsContributorsOperation:
            """Listing of all contributors to a corporation project."""
            ...

        def GetCorporationsProjectsDetail(
            self,
            corporation_id: int,
            project_id: str,
            token: Token,
            If_Modified_Since: str | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsProjectsDetailOperation:
            """Get the details of a corporation project."""
            ...

        def GetCorporationsProjectsListing(
            self,
            corporation_id: int,
            token: Token,
            after: str | None = ...,
            before: str | None = ...,
            limit: int | None = ...,
            state: str | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsProjectsListingOperation:
            """Listing of all (active) corporation projects."""
            ...

    Corporation_Projects: _Corporation_Projects = _Corporation_Projects()

    class _Dogma:
        def GetDogmaAttributes(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaAttributesOperation:
            """Get a list of dogma attribute ids  This route expires daily at 11:05"""
            ...

        def GetDogmaAttributesAttributeId(
            self,
            attribute_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaAttributesAttributeIdOperation:
            """Get information on a dogma attribute  This route expires daily at 11:05"""
            ...

        def GetDogmaDynamicItemsTypeIdItemId(
            self,
            item_id: int,
            type_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaDynamicItemsTypeIdItemIdOperation:
            """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
            ...

        def GetDogmaEffects(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaEffectsOperation:
            """Get a list of dogma effect ids  This route expires daily at 11:05"""
            ...

        def GetDogmaEffectsEffectId(
            self,
            effect_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaEffectsEffectIdOperation:
            """Get information on a dogma effect  This route expires daily at 11:05"""
            ...

    Dogma: _Dogma = _Dogma()

    class _Faction_Warfare:
        def GetCharactersCharacterIdFwStats(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFwStatsOperation:
            """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
            ...

        def GetCorporationsCorporationIdFwStats(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdFwStatsOperation:
            """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
            ...

        def GetFwLeaderboards(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwLeaderboardsOperation:
            """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
            ...

        def GetFwLeaderboardsCharacters(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwLeaderboardsCharactersOperation:
            """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
            ...

        def GetFwLeaderboardsCorporations(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwLeaderboardsCorporationsOperation:
            """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
            ...

        def GetFwStats(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwStatsOperation:
            """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
            ...

        def GetFwSystems(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwSystemsOperation:
            """An overview of the current ownership of faction warfare solar systems"""
            ...

        def GetFwWars(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwWarsOperation:
            """Data about which NPC factions are at war  This route expires daily at 11:05"""
            ...

    Faction_Warfare: _Faction_Warfare = _Faction_Warfare()

    class _Fittings:
        def DeleteCharactersCharacterIdFittingsFittingId(
            self,
            character_id: int,
            fitting_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteCharactersCharacterIdFittingsFittingIdOperation:
            """Delete a fitting from a character"""
            ...

        def GetCharactersCharacterIdFittings(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFittingsOperation:
            """Return fittings of a character"""
            ...

        def PostCharactersCharacterIdFittings(
            self,
            body: dict[str, Any],
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdFittingsOperation:
            """Save a new fitting for a character"""
            ...

    Fittings: _Fittings = _Fittings()

    class _Fleets:
        def DeleteFleetsFleetIdMembersMemberId(
            self,
            fleet_id: int,
            member_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteFleetsFleetIdMembersMemberIdOperation:
            """Kick a fleet member"""
            ...

        def DeleteFleetsFleetIdSquadsSquadId(
            self,
            fleet_id: int,
            squad_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteFleetsFleetIdSquadsSquadIdOperation:
            """Delete a fleet squad, only empty squads can be deleted"""
            ...

        def DeleteFleetsFleetIdWingsWingId(
            self,
            fleet_id: int,
            wing_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteFleetsFleetIdWingsWingIdOperation:
            """Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty"""
            ...

        def GetCharactersCharacterIdFleet(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFleetOperation:
            """Return the fleet ID the character is in, if any."""
            ...

        def GetFleetsFleetId(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFleetsFleetIdOperation:
            """Return details about a fleet"""
            ...

        def GetFleetsFleetIdMembers(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFleetsFleetIdMembersOperation:
            """Return information about fleet members"""
            ...

        def GetFleetsFleetIdWings(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFleetsFleetIdWingsOperation:
            """Return information about wings in a fleet"""
            ...

        def PostFleetsFleetIdMembers(
            self,
            body: dict[str, Any],
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostFleetsFleetIdMembersOperation:
            """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
            ...

        def PostFleetsFleetIdWings(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostFleetsFleetIdWingsOperation:
            """Create a new wing in a fleet"""
            ...

        def PostFleetsFleetIdWingsWingIdSquads(
            self,
            fleet_id: int,
            wing_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostFleetsFleetIdWingsWingIdSquadsOperation:
            """Create a new squad in a fleet"""
            ...

        def PutFleetsFleetId(
            self,
            body: dict[str, Any],
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdOperation:
            """Update settings about a fleet"""
            ...

        def PutFleetsFleetIdMembersMemberId(
            self,
            body: dict[str, Any],
            fleet_id: int,
            member_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdMembersMemberIdOperation:
            """Move a fleet member around"""
            ...

        def PutFleetsFleetIdSquadsSquadId(
            self,
            body: dict[str, Any],
            fleet_id: int,
            squad_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdSquadsSquadIdOperation:
            """Rename a fleet squad"""
            ...

        def PutFleetsFleetIdWingsWingId(
            self,
            body: dict[str, Any],
            fleet_id: int,
            wing_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdWingsWingIdOperation:
            """Rename a fleet wing"""
            ...

    Fleets: _Fleets = _Fleets()

    class _Incursions:
        def GetIncursions(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetIncursionsOperation:
            """Return a list of current incursions"""
            ...

    Incursions: _Incursions = _Incursions()

    class _Industry:
        def GetCharactersCharacterIdIndustryJobs(
            self,
            character_id: int,
            token: Token,
            include_completed: bool | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdIndustryJobsOperation:
            """List industry jobs placed by a character"""
            ...

        def GetCharactersCharacterIdMining(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMiningOperation:
            """Paginated record of all mining done by a character for the past 30 days"""
            ...

        def GetCorporationCorporationIdMiningExtractions(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationCorporationIdMiningExtractionsOperation:
            """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
            ...

        def GetCorporationCorporationIdMiningObservers(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationCorporationIdMiningObserversOperation:
            """Paginated list of all entities capable of observing and recording mining for a corporation"""
            ...

        def GetCorporationCorporationIdMiningObserversObserverId(
            self,
            corporation_id: int,
            observer_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationCorporationIdMiningObserversObserverIdOperation:
            """Paginated record of all mining seen by an observer"""
            ...

        def GetCorporationsCorporationIdIndustryJobs(
            self,
            corporation_id: int,
            token: Token,
            include_completed: bool | None = ...,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdIndustryJobsOperation:
            """List industry jobs run by a corporation"""
            ...

        def GetIndustryFacilities(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetIndustryFacilitiesOperation:
            """Return a list of industry facilities"""
            ...

        def GetIndustrySystems(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetIndustrySystemsOperation:
            """Return cost indices for solar systems"""
            ...

    Industry: _Industry = _Industry()

    class _Insurance:
        def GetInsurancePrices(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetInsurancePricesOperation:
            """Return available insurance levels for all ship types"""
            ...

    Insurance: _Insurance = _Insurance()

    class _Killmails:
        def GetCharactersCharacterIdKillmailsRecent(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdKillmailsRecentOperation:
            """Return a list of a character's kills and losses going back 90 days"""
            ...

        def GetCorporationsCorporationIdKillmailsRecent(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdKillmailsRecentOperation:
            """Get a list of a corporation's kills and losses going back 90 days"""
            ...

        def GetKillmailsKillmailIdKillmailHash(
            self,
            killmail_hash: str,
            killmail_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetKillmailsKillmailIdKillmailHashOperation:
            """Return a single killmail from its ID and hash"""
            ...

    Killmails: _Killmails = _Killmails()

    class _Location:
        def GetCharactersCharacterIdLocation(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdLocationOperation:
            """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
            ...

        def GetCharactersCharacterIdOnline(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdOnlineOperation:
            """Checks if the character is currently online"""
            ...

        def GetCharactersCharacterIdShip(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdShipOperation:
            """Get the current ship type, name and id"""
            ...

    Location: _Location = _Location()

    class _Loyalty:
        def GetCharactersCharacterIdLoyaltyPoints(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdLoyaltyPointsOperation:
            """Return a list of loyalty points for all corporations the character has worked for"""
            ...

        def GetLoyaltyStoresCorporationIdOffers(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetLoyaltyStoresCorporationIdOffersOperation:
            """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
            ...

    Loyalty: _Loyalty = _Loyalty()

    class _Mail:
        def DeleteCharactersCharacterIdMailLabelsLabelId(
            self,
            character_id: int,
            label_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteCharactersCharacterIdMailLabelsLabelIdOperation:
            """Delete a mail label"""
            ...

        def DeleteCharactersCharacterIdMailMailId(
            self,
            character_id: int,
            mail_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> DeleteCharactersCharacterIdMailMailIdOperation:
            """Delete a mail"""
            ...

        def GetCharactersCharacterIdMail(
            self,
            character_id: int,
            token: Token,
            labels: list[Any] | None = ...,
            last_mail_id: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMailOperation:
            """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
            ...

        def GetCharactersCharacterIdMailLabels(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMailLabelsOperation:
            """Return a list of the users mail labels, unread counts for each label and a total unread count."""
            ...

        def GetCharactersCharacterIdMailLists(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMailListsOperation:
            """Return all mailing lists that the character is subscribed to"""
            ...

        def GetCharactersCharacterIdMailMailId(
            self,
            character_id: int,
            mail_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMailMailIdOperation:
            """Return the contents of an EVE mail"""
            ...

        def PostCharactersCharacterIdMail(
            self,
            body: dict[str, Any],
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdMailOperation:
            """Create and send a new mail"""
            ...

        def PostCharactersCharacterIdMailLabels(
            self,
            body: dict[str, Any],
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdMailLabelsOperation:
            """Create a mail label"""
            ...

        def PutCharactersCharacterIdMailMailId(
            self,
            body: dict[str, Any],
            character_id: int,
            mail_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutCharactersCharacterIdMailMailIdOperation:
            """Update metadata about a mail"""
            ...

    Mail: _Mail = _Mail()

    class _Market:
        def GetCharactersCharacterIdOrders(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdOrdersOperation:
            """List open market orders placed by a character"""
            ...

        def GetCharactersCharacterIdOrdersHistory(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdOrdersHistoryOperation:
            """List cancelled and expired market orders placed by a character up to 90 days in the past."""
            ...

        def GetCorporationsCorporationIdOrders(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdOrdersOperation:
            """List open market orders placed on behalf of a corporation"""
            ...

        def GetCorporationsCorporationIdOrdersHistory(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdOrdersHistoryOperation:
            """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
            ...

        def GetMarketsGroups(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsGroupsOperation:
            """Get a list of item groups  This route expires daily at 11:05"""
            ...

        def GetMarketsGroupsMarketGroupId(
            self,
            market_group_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsGroupsMarketGroupIdOperation:
            """Get information on an item group  This route expires daily at 11:05"""
            ...

        def GetMarketsPrices(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsPricesOperation:
            """Return a list of prices"""
            ...

        def GetMarketsRegionIdHistory(
            self,
            region_id: int,
            type_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsRegionIdHistoryOperation:
            """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
            ...

        def GetMarketsRegionIdOrders(
            self,
            order_type: str,
            region_id: int,
            page: int | None = ...,
            type_id: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsRegionIdOrdersOperation:
            """Return a list of orders in a region"""
            ...

        def GetMarketsRegionIdTypes(
            self,
            region_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsRegionIdTypesOperation:
            """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
            ...

        def GetMarketsStructuresStructureId(
            self,
            structure_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsStructuresStructureIdOperation:
            """Return all orders in a structure"""
            ...

    Market: _Market = _Market()

    class _Meta:
        def GetMetaChangelog(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMetaChangelogOperation:
            """Get the changelog of this API."""
            ...

        def GetMetaCompatibilityDates(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMetaCompatibilityDatesOperation:
            """Get a list of compatibility dates."""
            ...

    Meta: _Meta = _Meta()

    class _Planetary_Interaction:
        def GetCharactersCharacterIdPlanets(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdPlanetsOperation:
            """Returns a list of all planetary colonies owned by a character."""
            ...

        def GetCharactersCharacterIdPlanetsPlanetId(
            self,
            character_id: int,
            planet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdPlanetsPlanetIdOperation:
            """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
            ...

        def GetCorporationsCorporationIdCustomsOffices(
            self,
            corporation_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdCustomsOfficesOperation:
            """List customs offices owned by a corporation"""
            ...

        def GetUniverseSchematicsSchematicId(
            self,
            schematic_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSchematicsSchematicIdOperation:
            """Get information on a planetary factory schematic"""
            ...

    Planetary_Interaction: _Planetary_Interaction = _Planetary_Interaction()

    class _Routes:
        def GetRouteOriginDestination(
            self,
            destination: int,
            origin: int,
            avoid: list[Any] | None = ...,
            connections: list[Any] | None = ...,
            flag: str | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetRouteOriginDestinationOperation:
            """Get the systems between origin and destination"""
            ...

    Routes: _Routes = _Routes()

    class _Search:
        def GetCharactersCharacterIdSearch(
            self,
            categories: list[Any],
            character_id: int,
            search: str,
            token: Token,
            strict: bool | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdSearchOperation:
            """Search for entities that match a given sub-string."""
            ...

    Search: _Search = _Search()

    class _Skills:
        def GetCharactersCharacterIdAttributes(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdAttributesOperation:
            """Return attributes of a character"""
            ...

        def GetCharactersCharacterIdSkillqueue(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdSkillqueueOperation:
            """List the configured skill queue for the given character"""
            ...

        def GetCharactersCharacterIdSkills(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdSkillsOperation:
            """List all trained skills for the given character"""
            ...

    Skills: _Skills = _Skills()

    class _Sovereignty:
        def GetSovereigntyCampaigns(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetSovereigntyCampaignsOperation:
            """Shows sovereignty data for campaigns."""
            ...

        def GetSovereigntyMap(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetSovereigntyMapOperation:
            """Shows sovereignty information for solar systems"""
            ...

        def GetSovereigntyStructures(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetSovereigntyStructuresOperation:
            """Shows sovereignty data for structures."""
            ...

    Sovereignty: _Sovereignty = _Sovereignty()

    class _Status:
        def GetStatus(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetStatusOperation:
            """EVE Server status"""
            ...

    Status: _Status = _Status()

    class _Universe:
        def GetUniverseAncestries(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseAncestriesOperation:
            """Get all character ancestries  This route expires daily at 11:05"""
            ...

        def GetUniverseAsteroidBeltsAsteroidBeltId(
            self,
            asteroid_belt_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseAsteroidBeltsAsteroidBeltIdOperation:
            """Get information on an asteroid belt  This route expires daily at 11:05"""
            ...

        def GetUniverseBloodlines(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseBloodlinesOperation:
            """Get a list of bloodlines  This route expires daily at 11:05"""
            ...

        def GetUniverseCategories(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseCategoriesOperation:
            """Get a list of item categories  This route expires daily at 11:05"""
            ...

        def GetUniverseCategoriesCategoryId(
            self,
            category_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseCategoriesCategoryIdOperation:
            """Get information of an item category  This route expires daily at 11:05"""
            ...

        def GetUniverseConstellations(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseConstellationsOperation:
            """Get a list of constellations  This route expires daily at 11:05"""
            ...

        def GetUniverseConstellationsConstellationId(
            self,
            constellation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseConstellationsConstellationIdOperation:
            """Get information on a constellation  This route expires daily at 11:05"""
            ...

        def GetUniverseFactions(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseFactionsOperation:
            """Get a list of factions  This route expires daily at 11:05"""
            ...

        def GetUniverseGraphics(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGraphicsOperation:
            """Get a list of graphics  This route expires daily at 11:05"""
            ...

        def GetUniverseGraphicsGraphicId(
            self,
            graphic_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGraphicsGraphicIdOperation:
            """Get information on a graphic  This route expires daily at 11:05"""
            ...

        def GetUniverseGroups(
            self,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGroupsOperation:
            """Get a list of item groups  This route expires daily at 11:05"""
            ...

        def GetUniverseGroupsGroupId(
            self,
            group_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGroupsGroupIdOperation:
            """Get information on an item group  This route expires daily at 11:05"""
            ...

        def GetUniverseMoonsMoonId(
            self,
            moon_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseMoonsMoonIdOperation:
            """Get information on a moon  This route expires daily at 11:05"""
            ...

        def GetUniversePlanetsPlanetId(
            self,
            planet_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniversePlanetsPlanetIdOperation:
            """Get information on a planet  This route expires daily at 11:05"""
            ...

        def GetUniverseRaces(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseRacesOperation:
            """Get a list of character races  This route expires daily at 11:05"""
            ...

        def GetUniverseRegions(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseRegionsOperation:
            """Get a list of regions  This route expires daily at 11:05"""
            ...

        def GetUniverseRegionsRegionId(
            self,
            region_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseRegionsRegionIdOperation:
            """Get information on a region  This route expires daily at 11:05"""
            ...

        def GetUniverseStargatesStargateId(
            self,
            stargate_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStargatesStargateIdOperation:
            """Get information on a stargate  This route expires daily at 11:05"""
            ...

        def GetUniverseStarsStarId(
            self,
            star_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStarsStarIdOperation:
            """Get information on a star  This route expires daily at 11:05"""
            ...

        def GetUniverseStationsStationId(
            self,
            station_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStationsStationIdOperation:
            """Get information on a station  This route expires daily at 11:05"""
            ...

        def GetUniverseStructures(
            self,
            filter: str | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStructuresOperation:
            """List all public structures"""
            ...

        def GetUniverseStructuresStructureId(
            self,
            structure_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStructuresStructureIdOperation:
            """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
            ...

        def GetUniverseSystemJumps(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemJumpsOperation:
            """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
            ...

        def GetUniverseSystemKills(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemKillsOperation:
            """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
            ...

        def GetUniverseSystems(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemsOperation:
            """Get a list of solar systems  This route expires daily at 11:05"""
            ...

        def GetUniverseSystemsSystemId(
            self,
            system_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemsSystemIdOperation:
            """Get information on a solar system.  This route expires daily at 11:05"""
            ...

        def GetUniverseTypes(
            self,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseTypesOperation:
            """Get a list of type ids  This route expires daily at 11:05"""
            ...

        def GetUniverseTypesTypeId(
            self,
            type_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseTypesTypeIdOperation:
            """Get information on a type  This route expires daily at 11:05"""
            ...

        def PostUniverseIds(
            self,
            body: list[str],
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUniverseIdsOperation:
            """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
            ...

        def PostUniverseNames(
            self,
            body: list[int],
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUniverseNamesOperation:
            """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
            ...

    Universe: _Universe = _Universe()

    class _User_Interface:
        def PostUiAutopilotWaypoint(
            self,
            add_to_beginning: bool,
            clear_other_waypoints: bool,
            destination_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiAutopilotWaypointOperation:
            """Set a solar system as autopilot waypoint"""
            ...

        def PostUiOpenwindowContract(
            self,
            contract_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowContractOperation:
            """Open the contract window inside the client"""
            ...

        def PostUiOpenwindowInformation(
            self,
            target_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowInformationOperation:
            """Open the information window for a character, corporation or alliance inside the client"""
            ...

        def PostUiOpenwindowMarketdetails(
            self,
            type_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowMarketdetailsOperation:
            """Open the market details window for a specific typeID inside the client"""
            ...

        def PostUiOpenwindowNewmail(
            self,
            body: dict[str, Any],
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowNewmailOperation:
            """Open the New Mail window, according to settings from the request if applicable"""
            ...

    User_Interface: _User_Interface = _User_Interface()

    class _Wallet:
        def GetCharactersCharacterIdWallet(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdWalletOperation:
            """Returns a character's wallet balance"""
            ...

        def GetCharactersCharacterIdWalletJournal(
            self,
            character_id: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdWalletJournalOperation:
            """Retrieve the given character's wallet journal going 30 days back"""
            ...

        def GetCharactersCharacterIdWalletTransactions(
            self,
            character_id: int,
            token: Token,
            from_id: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdWalletTransactionsOperation:
            """Get wallet transactions of a character"""
            ...

        def GetCorporationsCorporationIdWallets(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdWalletsOperation:
            """Get a corporation's wallets"""
            ...

        def GetCorporationsCorporationIdWalletsDivisionJournal(
            self,
            corporation_id: int,
            division: int,
            token: Token,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdWalletsDivisionJournalOperation:
            """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
            ...

        def GetCorporationsCorporationIdWalletsDivisionTransactions(
            self,
            corporation_id: int,
            division: int,
            token: Token,
            from_id: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdWalletsDivisionTransactionsOperation:
            """Get wallet transactions of a corporation"""
            ...

    Wallet: _Wallet = _Wallet()

    class _Wars:
        def GetWars(
            self,
            max_war_id: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetWarsOperation:
            """Return a list of wars"""
            ...

        def GetWarsWarId(
            self,
            war_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetWarsWarIdOperation:
            """Return details about a war"""
            ...

        def GetWarsWarIdKillmails(
            self,
            war_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetWarsWarIdKillmailsOperation:
            """Return a list of kills related to a war"""
            ...

    Wars: _Wars = _Wars()
