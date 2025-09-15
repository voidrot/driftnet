# flake8: noqa=E501
# Auto Generated do not edit
from typing import Any

from esi.models import Token
from esi.openapi_clients import ESIClientOperation

class GetAlliancesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetAlliancesAllianceIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetAlliancesAllianceIdCorporationsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetAlliancesAllianceIdIconsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdAssetsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdAssetsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersCharacterIdAssetsLocationsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersCharacterIdAssetsNamesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCorporationsCorporationIdAssetsLocationsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCorporationsCorporationIdAssetsNamesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdCalendarOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdCalendarEventIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdCalendarEventIdAttendeesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PutCharactersCharacterIdCalendarEventIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdAgentsResearchOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdBlueprintsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdCorporationhistoryOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdFatigueOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdMedalsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdNotificationsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdNotificationsContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdPortraitOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdRolesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdStandingsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdTitlesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersAffiliationOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersCharacterIdCspaOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdClonesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdImplantsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class DeleteCharactersCharacterIdContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetAlliancesAllianceIdContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetAlliancesAllianceIdContactsLabelsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdContactsLabelsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdContactsLabelsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersCharacterIdContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PutCharactersCharacterIdContactsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdContractsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdContractsContractIdBidsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdContractsContractIdItemsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetContractsPublicBidsContractIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetContractsPublicItemsContractIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetContractsPublicRegionIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdContractsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdContractsContractIdBidsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdContractsContractIdItemsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdAlliancehistoryOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdBlueprintsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdContainersLogsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdDivisionsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdFacilitiesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdIconsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdMedalsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdMedalsIssuedOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdMembersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetCorporationsCorporationIdMembersLimitOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> int: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetCorporationsCorporationIdMembersTitlesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdMembertrackingOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdRolesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdRolesHistoryOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdShareholdersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdStandingsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdStarbasesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdStarbasesStarbaseIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdStructuresOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdTitlesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsNpccorpsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetCorporationsProjectsContributionOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsProjectsContributorsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsProjectsDetailOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsProjectsListingOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetDogmaAttributesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetDogmaAttributesAttributeIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetDogmaDynamicItemsTypeIdItemIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetDogmaEffectsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetDogmaEffectsEffectIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdFwStatsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdFwStatsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFwLeaderboardsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFwLeaderboardsCharactersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFwLeaderboardsCorporationsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFwStatsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFwSystemsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFwWarsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class DeleteCharactersCharacterIdFittingsFittingIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdFittingsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersCharacterIdFittingsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class DeleteFleetsFleetIdMembersMemberIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class DeleteFleetsFleetIdSquadsSquadIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class DeleteFleetsFleetIdWingsWingIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdFleetOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFleetsFleetIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFleetsFleetIdMembersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetFleetsFleetIdWingsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostFleetsFleetIdMembersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostFleetsFleetIdWingsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostFleetsFleetIdWingsWingIdSquadsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PutFleetsFleetIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PutFleetsFleetIdMembersMemberIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PutFleetsFleetIdSquadsSquadIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PutFleetsFleetIdWingsWingIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetIncursionsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdIndustryJobsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdMiningOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationCorporationIdMiningExtractionsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationCorporationIdMiningObserversOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationCorporationIdMiningObserversObserverIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdIndustryJobsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetIndustryFacilitiesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetIndustrySystemsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetInsurancePricesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdKillmailsRecentOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdKillmailsRecentOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetKillmailsKillmailIdKillmailHashOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdLocationOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdOnlineOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdShipOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdLoyaltyPointsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetLoyaltyStoresCorporationIdOffersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class DeleteCharactersCharacterIdMailLabelsLabelIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class DeleteCharactersCharacterIdMailMailIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdMailOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdMailLabelsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdMailListsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdMailMailIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostCharactersCharacterIdMailOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostCharactersCharacterIdMailLabelsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PutCharactersCharacterIdMailMailIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdOrdersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdOrdersHistoryOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdOrdersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdOrdersHistoryOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMarketsGroupsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetMarketsGroupsMarketGroupIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMarketsPricesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMarketsRegionIdHistoryOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMarketsRegionIdOrdersOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMarketsRegionIdTypesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetMarketsStructuresStructureIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMetaChangelogOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetMetaCompatibilityDatesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdPlanetsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdPlanetsPlanetIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdCustomsOfficesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseSchematicsSchematicIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetRouteOriginDestinationOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetCharactersCharacterIdSearchOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdAttributesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdSkillqueueOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdSkillsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetSovereigntyCampaignsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetSovereigntyMapOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetSovereigntyStructuresOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetStatusOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseAncestriesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseAsteroidBeltsAsteroidBeltIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseBloodlinesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseCategoriesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseCategoriesCategoryIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseConstellationsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseConstellationsConstellationIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseFactionsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseGraphicsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseGraphicsGraphicIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseGroupsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseGroupsGroupIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseMoonsMoonIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniversePlanetsPlanetIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseRacesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseRegionsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseRegionsRegionIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseStargatesStargateIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseStarsStarIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseStationsStationIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseStructuresOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseStructuresStructureIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseSystemJumpsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseSystemKillsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseSystemsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseSystemsSystemIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetUniverseTypesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetUniverseTypesTypeIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostUniverseIdsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostUniverseNamesOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class PostUiAutopilotWaypointOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostUiOpenwindowContractOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostUiOpenwindowInformationOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostUiOpenwindowMarketdetailsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class PostUiOpenwindowNewmailOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> Any: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[Any]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[Any]: ...

class GetCharactersCharacterIdWalletOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> float: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[float]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[float]: ...

class GetCharactersCharacterIdWalletJournalOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCharactersCharacterIdWalletTransactionsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdWalletsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdWalletsDivisionJournalOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetCorporationsCorporationIdWalletsDivisionTransactionsOperation(
    ESIClientOperation
):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetWarsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[int]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[int]: ...

class GetWarsWarIdOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> dict[str, Any]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class GetWarsWarIdKillmailsOperation(ESIClientOperation):
    def result(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results(
        self,
        etag: str | None = None,
        return_response: bool = False,
        use_cache: bool = True,
        **extra,
    ) -> list[dict[str, Any]]: ...
    def results_localized(
        self, languages: str | list[str] = 'en', **kwargs
    ) -> list[dict[str, Any]]: ...

class ESIClientStub:
    class _Alliance:
        def GetAlliances(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesOperation: ...
        def GetAlliancesAllianceId(
            self,
            alliance_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdOperation: ...
        def GetAlliancesAllianceIdCorporations(
            self,
            alliance_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdCorporationsOperation: ...
        def GetAlliancesAllianceIdIcons(
            self,
            alliance_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdIconsOperation: ...

    Alliance: _Alliance = ...

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
        ) -> GetCharactersCharacterIdAssetsOperation: ...
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
        ) -> GetCorporationsCorporationIdAssetsOperation: ...
        def PostCharactersCharacterIdAssetsLocations(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdAssetsLocationsOperation: ...
        def PostCharactersCharacterIdAssetsNames(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdAssetsNamesOperation: ...
        def PostCorporationsCorporationIdAssetsLocations(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCorporationsCorporationIdAssetsLocationsOperation: ...
        def PostCorporationsCorporationIdAssetsNames(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCorporationsCorporationIdAssetsNamesOperation: ...

    Assets: _Assets = ...

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
        ) -> GetCharactersCharacterIdCalendarOperation: ...
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
        ) -> GetCharactersCharacterIdCalendarEventIdOperation: ...
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
        ) -> GetCharactersCharacterIdCalendarEventIdAttendeesOperation: ...
        def PutCharactersCharacterIdCalendarEventId(
            self,
            character_id: int,
            event_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutCharactersCharacterIdCalendarEventIdOperation: ...

    Calendar: _Calendar = ...

    class _Character:
        def GetCharactersCharacterId(
            self,
            character_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdOperation: ...
        def GetCharactersCharacterIdAgentsResearch(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdAgentsResearchOperation: ...
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
        ) -> GetCharactersCharacterIdBlueprintsOperation: ...
        def GetCharactersCharacterIdCorporationhistory(
            self,
            character_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdCorporationhistoryOperation: ...
        def GetCharactersCharacterIdFatigue(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFatigueOperation: ...
        def GetCharactersCharacterIdMedals(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMedalsOperation: ...
        def GetCharactersCharacterIdNotifications(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdNotificationsOperation: ...
        def GetCharactersCharacterIdNotificationsContacts(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdNotificationsContactsOperation: ...
        def GetCharactersCharacterIdPortrait(
            self,
            character_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdPortraitOperation: ...
        def GetCharactersCharacterIdRoles(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdRolesOperation: ...
        def GetCharactersCharacterIdStandings(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdStandingsOperation: ...
        def GetCharactersCharacterIdTitles(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdTitlesOperation: ...
        def PostCharactersAffiliation(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersAffiliationOperation: ...
        def PostCharactersCharacterIdCspa(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdCspaOperation: ...

    Character: _Character = ...

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
        ) -> GetCharactersCharacterIdClonesOperation: ...
        def GetCharactersCharacterIdImplants(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdImplantsOperation: ...

    Clones: _Clones = ...

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
        ) -> DeleteCharactersCharacterIdContactsOperation: ...
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
        ) -> GetAlliancesAllianceIdContactsOperation: ...
        def GetAlliancesAllianceIdContactsLabels(
            self,
            alliance_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetAlliancesAllianceIdContactsLabelsOperation: ...
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
        ) -> GetCharactersCharacterIdContactsOperation: ...
        def GetCharactersCharacterIdContactsLabels(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdContactsLabelsOperation: ...
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
        ) -> GetCorporationsCorporationIdContactsOperation: ...
        def GetCorporationsCorporationIdContactsLabels(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdContactsLabelsOperation: ...
        def PostCharactersCharacterIdContacts(
            self,
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
        ) -> PostCharactersCharacterIdContactsOperation: ...
        def PutCharactersCharacterIdContacts(
            self,
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
        ) -> PutCharactersCharacterIdContactsOperation: ...

    Contacts: _Contacts = ...

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
        ) -> GetCharactersCharacterIdContractsOperation: ...
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
        ) -> GetCharactersCharacterIdContractsContractIdBidsOperation: ...
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
        ) -> GetCharactersCharacterIdContractsContractIdItemsOperation: ...
        def GetContractsPublicBidsContractId(
            self,
            contract_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetContractsPublicBidsContractIdOperation: ...
        def GetContractsPublicItemsContractId(
            self,
            contract_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetContractsPublicItemsContractIdOperation: ...
        def GetContractsPublicRegionId(
            self,
            region_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetContractsPublicRegionIdOperation: ...
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
        ) -> GetCorporationsCorporationIdContractsOperation: ...
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
        ) -> GetCorporationsCorporationIdContractsContractIdBidsOperation: ...
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
        ) -> GetCorporationsCorporationIdContractsContractIdItemsOperation: ...

    Contracts: _Contracts = ...

    class _Corporation:
        def GetCorporationsCorporationId(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdOperation: ...
        def GetCorporationsCorporationIdAlliancehistory(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdAlliancehistoryOperation: ...
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
        ) -> GetCorporationsCorporationIdBlueprintsOperation: ...
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
        ) -> GetCorporationsCorporationIdContainersLogsOperation: ...
        def GetCorporationsCorporationIdDivisions(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdDivisionsOperation: ...
        def GetCorporationsCorporationIdFacilities(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdFacilitiesOperation: ...
        def GetCorporationsCorporationIdIcons(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdIconsOperation: ...
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
        ) -> GetCorporationsCorporationIdMedalsOperation: ...
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
        ) -> GetCorporationsCorporationIdMedalsIssuedOperation: ...
        def GetCorporationsCorporationIdMembers(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembersOperation: ...
        def GetCorporationsCorporationIdMembersLimit(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembersLimitOperation: ...
        def GetCorporationsCorporationIdMembersTitles(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembersTitlesOperation: ...
        def GetCorporationsCorporationIdMembertracking(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdMembertrackingOperation: ...
        def GetCorporationsCorporationIdRoles(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdRolesOperation: ...
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
        ) -> GetCorporationsCorporationIdRolesHistoryOperation: ...
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
        ) -> GetCorporationsCorporationIdShareholdersOperation: ...
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
        ) -> GetCorporationsCorporationIdStandingsOperation: ...
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
        ) -> GetCorporationsCorporationIdStarbasesOperation: ...
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
        ) -> GetCorporationsCorporationIdStarbasesStarbaseIdOperation: ...
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
        ) -> GetCorporationsCorporationIdStructuresOperation: ...
        def GetCorporationsCorporationIdTitles(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdTitlesOperation: ...
        def GetCorporationsNpccorps(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsNpccorpsOperation: ...

    Corporation: _Corporation = ...

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
        ) -> GetCorporationsProjectsContributionOperation: ...
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
        ) -> GetCorporationsProjectsContributorsOperation: ...
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
        ) -> GetCorporationsProjectsDetailOperation: ...
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
        ) -> GetCorporationsProjectsListingOperation: ...

    Corporation_Projects: _Corporation_Projects = ...

    class _Dogma:
        def GetDogmaAttributes(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaAttributesOperation: ...
        def GetDogmaAttributesAttributeId(
            self,
            attribute_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaAttributesAttributeIdOperation: ...
        def GetDogmaDynamicItemsTypeIdItemId(
            self,
            item_id: int,
            type_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaDynamicItemsTypeIdItemIdOperation: ...
        def GetDogmaEffects(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaEffectsOperation: ...
        def GetDogmaEffectsEffectId(
            self,
            effect_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetDogmaEffectsEffectIdOperation: ...

    Dogma: _Dogma = ...

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
        ) -> GetCharactersCharacterIdFwStatsOperation: ...
        def GetCorporationsCorporationIdFwStats(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdFwStatsOperation: ...
        def GetFwLeaderboards(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwLeaderboardsOperation: ...
        def GetFwLeaderboardsCharacters(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwLeaderboardsCharactersOperation: ...
        def GetFwLeaderboardsCorporations(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwLeaderboardsCorporationsOperation: ...
        def GetFwStats(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwStatsOperation: ...
        def GetFwSystems(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwSystemsOperation: ...
        def GetFwWars(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFwWarsOperation: ...

    Faction_Warfare: _Faction_Warfare = ...

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
        ) -> DeleteCharactersCharacterIdFittingsFittingIdOperation: ...
        def GetCharactersCharacterIdFittings(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFittingsOperation: ...
        def PostCharactersCharacterIdFittings(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdFittingsOperation: ...

    Fittings: _Fittings = ...

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
        ) -> DeleteFleetsFleetIdMembersMemberIdOperation: ...
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
        ) -> DeleteFleetsFleetIdSquadsSquadIdOperation: ...
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
        ) -> DeleteFleetsFleetIdWingsWingIdOperation: ...
        def GetCharactersCharacterIdFleet(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdFleetOperation: ...
        def GetFleetsFleetId(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFleetsFleetIdOperation: ...
        def GetFleetsFleetIdMembers(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFleetsFleetIdMembersOperation: ...
        def GetFleetsFleetIdWings(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetFleetsFleetIdWingsOperation: ...
        def PostFleetsFleetIdMembers(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostFleetsFleetIdMembersOperation: ...
        def PostFleetsFleetIdWings(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostFleetsFleetIdWingsOperation: ...
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
        ) -> PostFleetsFleetIdWingsWingIdSquadsOperation: ...
        def PutFleetsFleetId(
            self,
            fleet_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdOperation: ...
        def PutFleetsFleetIdMembersMemberId(
            self,
            fleet_id: int,
            member_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdMembersMemberIdOperation: ...
        def PutFleetsFleetIdSquadsSquadId(
            self,
            fleet_id: int,
            squad_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdSquadsSquadIdOperation: ...
        def PutFleetsFleetIdWingsWingId(
            self,
            fleet_id: int,
            wing_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutFleetsFleetIdWingsWingIdOperation: ...

    Fleets: _Fleets = ...

    class _Incursions:
        def GetIncursions(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetIncursionsOperation: ...

    Incursions: _Incursions = ...

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
        ) -> GetCharactersCharacterIdIndustryJobsOperation: ...
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
        ) -> GetCharactersCharacterIdMiningOperation: ...
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
        ) -> GetCorporationCorporationIdMiningExtractionsOperation: ...
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
        ) -> GetCorporationCorporationIdMiningObserversOperation: ...
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
        ) -> GetCorporationCorporationIdMiningObserversObserverIdOperation: ...
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
        ) -> GetCorporationsCorporationIdIndustryJobsOperation: ...
        def GetIndustryFacilities(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetIndustryFacilitiesOperation: ...
        def GetIndustrySystems(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetIndustrySystemsOperation: ...

    Industry: _Industry = ...

    class _Insurance:
        def GetInsurancePrices(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetInsurancePricesOperation: ...

    Insurance: _Insurance = ...

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
        ) -> GetCharactersCharacterIdKillmailsRecentOperation: ...
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
        ) -> GetCorporationsCorporationIdKillmailsRecentOperation: ...
        def GetKillmailsKillmailIdKillmailHash(
            self,
            killmail_hash: str,
            killmail_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetKillmailsKillmailIdKillmailHashOperation: ...

    Killmails: _Killmails = ...

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
        ) -> GetCharactersCharacterIdLocationOperation: ...
        def GetCharactersCharacterIdOnline(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdOnlineOperation: ...
        def GetCharactersCharacterIdShip(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdShipOperation: ...

    Location: _Location = ...

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
        ) -> GetCharactersCharacterIdLoyaltyPointsOperation: ...
        def GetLoyaltyStoresCorporationIdOffers(
            self,
            corporation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetLoyaltyStoresCorporationIdOffersOperation: ...

    Loyalty: _Loyalty = ...

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
        ) -> DeleteCharactersCharacterIdMailLabelsLabelIdOperation: ...
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
        ) -> DeleteCharactersCharacterIdMailMailIdOperation: ...
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
        ) -> GetCharactersCharacterIdMailOperation: ...
        def GetCharactersCharacterIdMailLabels(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMailLabelsOperation: ...
        def GetCharactersCharacterIdMailLists(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdMailListsOperation: ...
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
        ) -> GetCharactersCharacterIdMailMailIdOperation: ...
        def PostCharactersCharacterIdMail(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdMailOperation: ...
        def PostCharactersCharacterIdMailLabels(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostCharactersCharacterIdMailLabelsOperation: ...
        def PutCharactersCharacterIdMailMailId(
            self,
            character_id: int,
            mail_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PutCharactersCharacterIdMailMailIdOperation: ...

    Mail: _Mail = ...

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
        ) -> GetCharactersCharacterIdOrdersOperation: ...
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
        ) -> GetCharactersCharacterIdOrdersHistoryOperation: ...
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
        ) -> GetCorporationsCorporationIdOrdersOperation: ...
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
        ) -> GetCorporationsCorporationIdOrdersHistoryOperation: ...
        def GetMarketsGroups(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsGroupsOperation: ...
        def GetMarketsGroupsMarketGroupId(
            self,
            market_group_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsGroupsMarketGroupIdOperation: ...
        def GetMarketsPrices(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsPricesOperation: ...
        def GetMarketsRegionIdHistory(
            self,
            region_id: int,
            type_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsRegionIdHistoryOperation: ...
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
        ) -> GetMarketsRegionIdOrdersOperation: ...
        def GetMarketsRegionIdTypes(
            self,
            region_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMarketsRegionIdTypesOperation: ...
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
        ) -> GetMarketsStructuresStructureIdOperation: ...

    Market: _Market = ...

    class _Meta:
        def GetMetaChangelog(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMetaChangelogOperation: ...
        def GetMetaCompatibilityDates(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetMetaCompatibilityDatesOperation: ...

    Meta: _Meta = ...

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
        ) -> GetCharactersCharacterIdPlanetsOperation: ...
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
        ) -> GetCharactersCharacterIdPlanetsPlanetIdOperation: ...
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
        ) -> GetCorporationsCorporationIdCustomsOfficesOperation: ...
        def GetUniverseSchematicsSchematicId(
            self,
            schematic_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSchematicsSchematicIdOperation: ...

    Planetary_Interaction: _Planetary_Interaction = ...

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
        ) -> GetRouteOriginDestinationOperation: ...

    Routes: _Routes = ...

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
        ) -> GetCharactersCharacterIdSearchOperation: ...

    Search: _Search = ...

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
        ) -> GetCharactersCharacterIdAttributesOperation: ...
        def GetCharactersCharacterIdSkillqueue(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdSkillqueueOperation: ...
        def GetCharactersCharacterIdSkills(
            self,
            character_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCharactersCharacterIdSkillsOperation: ...

    Skills: _Skills = ...

    class _Sovereignty:
        def GetSovereigntyCampaigns(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetSovereigntyCampaignsOperation: ...
        def GetSovereigntyMap(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetSovereigntyMapOperation: ...
        def GetSovereigntyStructures(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetSovereigntyStructuresOperation: ...

    Sovereignty: _Sovereignty = ...

    class _Status:
        def GetStatus(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetStatusOperation: ...

    Status: _Status = ...

    class _Universe:
        def GetUniverseAncestries(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseAncestriesOperation: ...
        def GetUniverseAsteroidBeltsAsteroidBeltId(
            self,
            asteroid_belt_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseAsteroidBeltsAsteroidBeltIdOperation: ...
        def GetUniverseBloodlines(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseBloodlinesOperation: ...
        def GetUniverseCategories(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseCategoriesOperation: ...
        def GetUniverseCategoriesCategoryId(
            self,
            category_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseCategoriesCategoryIdOperation: ...
        def GetUniverseConstellations(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseConstellationsOperation: ...
        def GetUniverseConstellationsConstellationId(
            self,
            constellation_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseConstellationsConstellationIdOperation: ...
        def GetUniverseFactions(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseFactionsOperation: ...
        def GetUniverseGraphics(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGraphicsOperation: ...
        def GetUniverseGraphicsGraphicId(
            self,
            graphic_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGraphicsGraphicIdOperation: ...
        def GetUniverseGroups(
            self,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGroupsOperation: ...
        def GetUniverseGroupsGroupId(
            self,
            group_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseGroupsGroupIdOperation: ...
        def GetUniverseMoonsMoonId(
            self,
            moon_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseMoonsMoonIdOperation: ...
        def GetUniversePlanetsPlanetId(
            self,
            planet_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniversePlanetsPlanetIdOperation: ...
        def GetUniverseRaces(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseRacesOperation: ...
        def GetUniverseRegions(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseRegionsOperation: ...
        def GetUniverseRegionsRegionId(
            self,
            region_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseRegionsRegionIdOperation: ...
        def GetUniverseStargatesStargateId(
            self,
            stargate_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStargatesStargateIdOperation: ...
        def GetUniverseStarsStarId(
            self,
            star_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStarsStarIdOperation: ...
        def GetUniverseStationsStationId(
            self,
            station_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStationsStationIdOperation: ...
        def GetUniverseStructures(
            self,
            filter: str | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStructuresOperation: ...
        def GetUniverseStructuresStructureId(
            self,
            structure_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseStructuresStructureIdOperation: ...
        def GetUniverseSystemJumps(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemJumpsOperation: ...
        def GetUniverseSystemKills(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemKillsOperation: ...
        def GetUniverseSystems(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemsOperation: ...
        def GetUniverseSystemsSystemId(
            self,
            system_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseSystemsSystemIdOperation: ...
        def GetUniverseTypes(
            self,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseTypesOperation: ...
        def GetUniverseTypesTypeId(
            self,
            type_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetUniverseTypesTypeIdOperation: ...
        def PostUniverseIds(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUniverseIdsOperation: ...
        def PostUniverseNames(
            self,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUniverseNamesOperation: ...

    Universe: _Universe = ...

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
        ) -> PostUiAutopilotWaypointOperation: ...
        def PostUiOpenwindowContract(
            self,
            contract_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowContractOperation: ...
        def PostUiOpenwindowInformation(
            self,
            target_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowInformationOperation: ...
        def PostUiOpenwindowMarketdetails(
            self,
            type_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowMarketdetailsOperation: ...
        def PostUiOpenwindowNewmail(
            self,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> PostUiOpenwindowNewmailOperation: ...

    User_Interface: _User_Interface = ...

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
        ) -> GetCharactersCharacterIdWalletOperation: ...
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
        ) -> GetCharactersCharacterIdWalletJournalOperation: ...
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
        ) -> GetCharactersCharacterIdWalletTransactionsOperation: ...
        def GetCorporationsCorporationIdWallets(
            self,
            corporation_id: int,
            token: Token,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetCorporationsCorporationIdWalletsOperation: ...
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
        ) -> GetCorporationsCorporationIdWalletsDivisionJournalOperation: ...
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
        ) -> GetCorporationsCorporationIdWalletsDivisionTransactionsOperation: ...

    Wallet: _Wallet = ...

    class _Wars:
        def GetWars(
            self,
            max_war_id: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetWarsOperation: ...
        def GetWarsWarId(
            self,
            war_id: int,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetWarsWarIdOperation: ...
        def GetWarsWarIdKillmails(
            self,
            war_id: int,
            page: int | None = ...,
            Accept_Language: str | None = ...,
            If_None_Match: str | None = ...,
            X_Compatibility_Date: str | None = ...,
            X_Tenant: str | None = ...,
            **kwargs: Any,
        ) -> GetWarsWarIdKillmailsOperation: ...

    Wars: _Wars = ...
