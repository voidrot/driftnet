# flake8: noqa=E501
# Auto Generated do not edit
from typing import Any, List, Optional
from pydantic import BaseModel
from apps.esi.client import ESIClientOperation
from apps.esi.models import Token


class AlliancesAllianceIdGet(BaseModel):
    creator_corporation_id: int
    creator_id: int
    date_founded: str
    executor_corporation_id: int = None
    faction_id: int = None
    name: str
    ticker: str

class AlliancesAllianceIdIconsGet(BaseModel):
    px128x128: str = None
    px64x64: str = None

class InlineModel(BaseModel):
    killmail_hash: str
    killmail_id: int

class CharactersCharacterIdCalendarEventIdGet(BaseModel):
    date: str
    duration: int
    event_id: int
    importance: int
    owner_id: int
    owner_name: str
    owner_type: str
    response: str
    text: str
    title: str

class CharactersCharacterIdGet(BaseModel):
    alliance_id: int = None
    birthday: str
    bloodline_id: int
    corporation_id: int
    description: str = None
    faction_id: int = None
    gender: str
    name: str
    race_id: int
    security_status: float = None
    title: str = None

class CharactersCharacterIdFatigueGet(BaseModel):
    jump_fatigue_expire_date: str = None
    last_jump_date: str = None
    last_update_date: str = None

class CharactersCharacterIdPortraitGet(BaseModel):
    px128x128: str = None
    px256x256: str = None
    px512x512: str = None
    px64x64: str = None

class CharactersCharacterIdRolesGet(BaseModel):
    roles: List[str] = None
    roles_at_base: List[str] = None
    roles_at_hq: List[str] = None
    roles_at_other: List[str] = None

class CharactersCharacterIdClonesGet(BaseModel):
    home_location: InlineModel = None
    jump_clones: List[InlineModel]
    last_clone_jump_date: str = None
    last_station_change_date: str = None

class CorporationsCorporationIdGet(BaseModel):
    alliance_id: int = None
    ceo_id: int
    creator_id: int
    date_founded: str = None
    description: str = None
    faction_id: int = None
    home_station_id: int = None
    member_count: int
    name: str
    shares: int = None
    tax_rate: float
    ticker: str
    url: str = None
    war_eligible: bool = None

class CorporationsCorporationIdDivisionsGet(BaseModel):
    hangar: List[InlineModel] = None
    wallet: List[InlineModel] = None

class CorporationsCorporationIdIconsGet(BaseModel):
    px128x128: str = None
    px256x256: str = None
    px64x64: str = None

class CorporationsCorporationIdStarbasesStarbaseIdGet(BaseModel):
    allow_alliance_members: bool
    allow_corporation_members: bool
    anchor: str
    attack_if_at_war: bool
    attack_if_other_security_status_dropping: bool
    attack_security_status_threshold: float = None
    attack_standing_threshold: float = None
    fuel_bay_take: str
    fuel_bay_view: str
    fuels: List[InlineModel] = None
    offline: str
    online: str
    unanchor: str
    use_alliance_standings: bool

class CorporationsProjectsContribution(BaseModel):
    contributed: int
    last_modified: str = None

class CorporationsProjectsContributors(BaseModel):
    contributors: List[CorporationsProjectsContributorsContributor]
    cursor: Cursor = None

class CorporationsProjectsDetail(BaseModel):
    configuration: Any
    contribution: CorporationsProjectsDetailContribution = None
    creator: CorporationsProjectsDetailCreator
    details: CorporationsProjectsDetailDetails
    id: str
    last_modified: str
    name: str
    progress: CorporationsProjectsDetailProgress
    reward: CorporationsProjectsDetailReward = None
    state: str

class CorporationsProjectsListing(BaseModel):
    cursor: Cursor = None
    projects: List[CorporationsProjectsDetailProject]

class DogmaAttributesAttributeIdGet(BaseModel):
    attribute_id: int
    default_value: float = None
    description: str = None
    display_name: str = None
    high_is_good: bool = None
    icon_id: int = None
    name: str = None
    published: bool = None
    stackable: bool = None
    unit_id: int = None

class DogmaDynamicItemsTypeIdItemIdGet(BaseModel):
    created_by: int
    dogma_attributes: List[InlineModel]
    dogma_effects: List[InlineModel]
    mutator_type_id: int
    source_type_id: int

class DogmaEffectsEffectIdGet(BaseModel):
    description: str = None
    disallow_auto_repeat: bool = None
    discharge_attribute_id: int = None
    display_name: str = None
    duration_attribute_id: int = None
    effect_category: int = None
    effect_id: int
    electronic_chance: bool = None
    falloff_attribute_id: int = None
    icon_id: int = None
    is_assistance: bool = None
    is_offensive: bool = None
    is_warp_safe: bool = None
    modifiers: List[InlineModel] = None
    name: str = None
    post_expression: int = None
    pre_expression: int = None
    published: bool = None
    range_attribute_id: int = None
    range_chance: bool = None
    tracking_speed_attribute_id: int = None

class CharactersCharacterIdFwStatsGet(BaseModel):
    current_rank: int = None
    enlisted_on: str = None
    faction_id: int = None
    highest_rank: int = None
    kills: InlineModel
    victory_points: InlineModel

class CorporationsCorporationIdFwStatsGet(BaseModel):
    enlisted_on: str = None
    faction_id: int = None
    kills: InlineModel
    pilots: int = None
    victory_points: InlineModel

class FwLeaderboardsGet(BaseModel):
    kills: InlineModel
    victory_points: InlineModel

class FwLeaderboardsCharactersGet(BaseModel):
    kills: InlineModel
    victory_points: InlineModel

class FwLeaderboardsCorporationsGet(BaseModel):
    kills: InlineModel
    victory_points: InlineModel

class CharactersCharacterIdFittingsPost(BaseModel):
    fitting_id: int

class CharactersCharacterIdFleetGet(BaseModel):
    fleet_boss_id: int
    fleet_id: int
    role: str
    squad_id: int
    wing_id: int

class FleetsFleetIdGet(BaseModel):
    is_free_move: bool
    is_registered: bool
    is_voice_enabled: bool
    motd: str

class FleetsFleetIdWingsPost(BaseModel):
    wing_id: int

class FleetsFleetIdWingsWingIdSquadsPost(BaseModel):
    squad_id: int

class KillmailsKillmailIdKillmailHashGet(BaseModel):
    attackers: List[InlineModel]
    killmail_id: int
    killmail_time: str
    moon_id: int = None
    solar_system_id: int
    victim: InlineModel
    war_id: int = None

class CharactersCharacterIdLocationGet(BaseModel):
    solar_system_id: int
    station_id: int = None
    structure_id: int = None

class CharactersCharacterIdOnlineGet(BaseModel):
    last_login: str = None
    last_logout: str = None
    logins: int = None
    online: bool

class CharactersCharacterIdShipGet(BaseModel):
    ship_item_id: int
    ship_name: str
    ship_type_id: int

class CharactersCharacterIdMailLabelsGet(BaseModel):
    labels: List[InlineModel] = None
    total_unread_count: int = None

class CharactersCharacterIdMailMailIdGet(BaseModel):
    body: str = None
    from: int = None
    labels: List[int] = None
    read: bool = None
    recipients: List[InlineModel] = None
    subject: str = None
    timestamp: str = None

class MarketsGroupsMarketGroupIdGet(BaseModel):
    description: str
    market_group_id: int
    name: str
    parent_group_id: int = None
    types: List[int]

class MetaChangelog(BaseModel):
    changelog: InlineModel

class MetaCompatibilityDates(BaseModel):
    compatibility_dates: List[str]

class CharactersCharacterIdPlanetsPlanetIdGet(BaseModel):
    links: List[InlineModel]
    pins: List[InlineModel]
    routes: List[InlineModel]

class UniverseSchematicsSchematicIdGet(BaseModel):
    cycle_time: int
    schematic_name: str

class CharactersCharacterIdSearchGet(BaseModel):
    agent: List[int] = None
    alliance: List[int] = None
    character: List[int] = None
    constellation: List[int] = None
    corporation: List[int] = None
    faction: List[int] = None
    inventory_type: List[int] = None
    region: List[int] = None
    solar_system: List[int] = None
    station: List[int] = None
    structure: List[int] = None

class CharactersCharacterIdAttributesGet(BaseModel):
    accrued_remap_cooldown_date: str = None
    bonus_remaps: int = None
    charisma: int
    intelligence: int
    last_remap_date: str = None
    memory: int
    perception: int
    willpower: int

class CharactersCharacterIdSkillsGet(BaseModel):
    skills: List[InlineModel]
    total_sp: int
    unallocated_sp: int = None

class StatusGet(BaseModel):
    players: int
    server_version: str
    start_time: str
    vip: bool = None

class UniverseAsteroidBeltsAsteroidBeltIdGet(BaseModel):
    name: str
    position: InlineModel
    system_id: int

class UniverseCategoriesCategoryIdGet(BaseModel):
    category_id: int
    groups: List[int]
    name: str
    published: bool

class UniverseConstellationsConstellationIdGet(BaseModel):
    constellation_id: int
    name: str
    position: InlineModel
    region_id: int
    systems: List[int]

class UniverseGraphicsGraphicIdGet(BaseModel):
    collision_file: str = None
    graphic_file: str = None
    graphic_id: int
    icon_folder: str = None
    sof_dna: str = None
    sof_fation_name: str = None
    sof_hull_name: str = None
    sof_race_name: str = None

class UniverseGroupsGroupIdGet(BaseModel):
    category_id: int
    group_id: int
    name: str
    published: bool
    types: List[int]

class UniverseMoonsMoonIdGet(BaseModel):
    moon_id: int
    name: str
    position: InlineModel
    system_id: int

class UniversePlanetsPlanetIdGet(BaseModel):
    name: str
    planet_id: int
    position: InlineModel
    system_id: int
    type_id: int

class UniverseRegionsRegionIdGet(BaseModel):
    constellations: List[int]
    description: str = None
    name: str
    region_id: int

class UniverseStargatesStargateIdGet(BaseModel):
    destination: InlineModel
    name: str
    position: InlineModel
    stargate_id: int
    system_id: int
    type_id: int

class UniverseStarsStarIdGet(BaseModel):
    age: int
    luminosity: float
    name: str
    radius: int
    solar_system_id: int
    spectral_class: str
    temperature: int
    type_id: int

class UniverseStationsStationIdGet(BaseModel):
    max_dockable_ship_volume: float
    name: str
    office_rental_cost: float
    owner: int = None
    position: InlineModel
    race_id: int = None
    reprocessing_efficiency: float
    reprocessing_stations_take: float
    services: List[str]
    station_id: int
    system_id: int
    type_id: int

class UniverseStructuresStructureIdGet(BaseModel):
    name: str
    owner_id: int
    position: InlineModel = None
    solar_system_id: int
    type_id: int = None

class UniverseSystemsSystemIdGet(BaseModel):
    constellation_id: int
    name: str
    planets: List[InlineModel] = None
    position: InlineModel
    security_class: str = None
    security_status: float
    star_id: int = None
    stargates: List[int] = None
    stations: List[int] = None
    system_id: int

class UniverseTypesTypeIdGet(BaseModel):
    capacity: float = None
    description: str
    dogma_attributes: List[InlineModel] = None
    dogma_effects: List[InlineModel] = None
    graphic_id: int = None
    group_id: int
    icon_id: int = None
    market_group_id: int = None
    mass: float = None
    name: str
    packaged_volume: float = None
    portion_size: int = None
    published: bool
    radius: float = None
    type_id: int
    volume: float = None

class WarsWarIdGet(BaseModel):
    aggressor: InlineModel
    allies: List[InlineModel] = None
    declared: str
    defender: InlineModel
    finished: str = None
    id: int
    mutual: bool
    open_for_allies: bool
    retracted: str = None
    started: str = None

class GetAlliancesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """List all active player alliances"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """List all active player alliances"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """List all active player alliances"""
        ...


class GetAlliancesAllianceIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> AlliancesAllianceIdGet:
        """Public information about an alliance"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[AlliancesAllianceIdGet]:
        """Public information about an alliance"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[AlliancesAllianceIdGet]]:
        """Public information about an alliance"""
        ...


class GetAlliancesAllianceIdCorporationsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """List all current member corporations of an alliance"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """List all current member corporations of an alliance"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """List all current member corporations of an alliance"""
        ...


class GetAlliancesAllianceIdIconsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> AlliancesAllianceIdIconsGet:
        """Get the icon urls for a alliance  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[AlliancesAllianceIdIconsGet]:
        """Get the icon urls for a alliance  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[AlliancesAllianceIdIconsGet]]:
        """Get the icon urls for a alliance  This route expires daily at 11:05"""
        ...


class GetCharactersCharacterIdAssetsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of the characters assets"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of the characters assets"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of the characters assets"""
        ...


class GetCorporationsCorporationIdAssetsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of the corporation assets"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of the corporation assets"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of the corporation assets"""
        ...


class PostCharactersCharacterIdAssetsLocationsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...


class PostCharactersCharacterIdAssetsNamesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
        ...


class PostCorporationsCorporationIdAssetsLocationsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
        ...


class PostCorporationsCorporationIdAssetsNamesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
        ...


class GetCharactersCharacterIdCalendarOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
        ...


class GetCharactersCharacterIdCalendarEventIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdCalendarEventIdGet:
        """Get all the information for a specific event"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdCalendarEventIdGet]:
        """Get all the information for a specific event"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdCalendarEventIdGet]]:
        """Get all the information for a specific event"""
        ...


class GetCharactersCharacterIdCalendarEventIdAttendeesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get all invited attendees for a given event"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get all invited attendees for a given event"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get all invited attendees for a given event"""
        ...


class PutCharactersCharacterIdCalendarEventIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Set your response status to an event"""
        ...

class GetCharactersCharacterIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdGet:
        """Public information about a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdGet]:
        """Public information about a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdGet]]:
        """Public information about a character"""
        ...


class GetCharactersCharacterIdAgentsResearchOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
        ...


class GetCharactersCharacterIdBlueprintsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of blueprints the character owns"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of blueprints the character owns"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of blueprints the character owns"""
        ...


class GetCharactersCharacterIdCorporationhistoryOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of all the corporations a character has been a member of"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of all the corporations a character has been a member of"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of all the corporations a character has been a member of"""
        ...


class GetCharactersCharacterIdFatigueOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdFatigueGet:
        """Return a character's jump activation and fatigue information"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdFatigueGet]:
        """Return a character's jump activation and fatigue information"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdFatigueGet]]:
        """Return a character's jump activation and fatigue information"""
        ...


class GetCharactersCharacterIdMedalsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of medals the character has"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of medals the character has"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of medals the character has"""
        ...


class GetCharactersCharacterIdNotificationsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return character notifications"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return character notifications"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return character notifications"""
        ...


class GetCharactersCharacterIdNotificationsContactsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return notifications about having been added to someone's contact list"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return notifications about having been added to someone's contact list"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return notifications about having been added to someone's contact list"""
        ...


class GetCharactersCharacterIdPortraitOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdPortraitGet:
        """Get portrait urls for a character  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdPortraitGet]:
        """Get portrait urls for a character  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdPortraitGet]]:
        """Get portrait urls for a character  This route expires daily at 11:05"""
        ...


class GetCharactersCharacterIdRolesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdRolesGet:
        """Returns a character's corporation roles"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdRolesGet]:
        """Returns a character's corporation roles"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdRolesGet]]:
        """Returns a character's corporation roles"""
        ...


class GetCharactersCharacterIdStandingsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return character standings from agents, NPC corporations, and factions"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return character standings from agents, NPC corporations, and factions"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return character standings from agents, NPC corporations, and factions"""
        ...


class GetCharactersCharacterIdTitlesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a character's titles"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a character's titles"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a character's titles"""
        ...


class PostCharactersAffiliationOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Bulk lookup of character IDs to corporation, alliance and faction"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Bulk lookup of character IDs to corporation, alliance and faction"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Bulk lookup of character IDs to corporation, alliance and faction"""
        ...


class PostCharactersCharacterIdCspaOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> float:
        """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[float]:
        """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[float]]:
        """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
        ...


class GetCharactersCharacterIdClonesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdClonesGet:
        """A list of the character's clones"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdClonesGet]:
        """A list of the character's clones"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdClonesGet]]:
        """A list of the character's clones"""
        ...


class GetCharactersCharacterIdImplantsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return implants on the active clone of a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return implants on the active clone of a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Return implants on the active clone of a character"""
        ...


class DeleteCharactersCharacterIdContactsOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Bulk delete contacts"""
        ...

class GetAlliancesAllianceIdContactsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return contacts of an alliance"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return contacts of an alliance"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return contacts of an alliance"""
        ...


class GetAlliancesAllianceIdContactsLabelsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return custom labels for an alliance's contacts"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return custom labels for an alliance's contacts"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return custom labels for an alliance's contacts"""
        ...


class GetCharactersCharacterIdContactsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return contacts of a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return contacts of a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return contacts of a character"""
        ...


class GetCharactersCharacterIdContactsLabelsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return custom labels for a character's contacts"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return custom labels for a character's contacts"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return custom labels for a character's contacts"""
        ...


class GetCorporationsCorporationIdContactsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return contacts of a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return contacts of a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return contacts of a corporation"""
        ...


class GetCorporationsCorporationIdContactsLabelsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return custom labels for a corporation's contacts"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return custom labels for a corporation's contacts"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return custom labels for a corporation's contacts"""
        ...


class PostCharactersCharacterIdContactsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Bulk add contacts with same settings"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Bulk add contacts with same settings"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Bulk add contacts with same settings"""
        ...


class PutCharactersCharacterIdContactsOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Bulk edit contacts with same settings"""
        ...

class GetCharactersCharacterIdContractsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...


class GetCharactersCharacterIdContractsContractIdBidsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists bids on a particular auction contract"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists bids on a particular auction contract"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Lists bids on a particular auction contract"""
        ...


class GetCharactersCharacterIdContractsContractIdItemsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists items of a particular contract"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists items of a particular contract"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Lists items of a particular contract"""
        ...


class GetContractsPublicBidsContractIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists bids on a public auction contract"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists bids on a public auction contract"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Lists bids on a public auction contract"""
        ...


class GetContractsPublicItemsContractIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists items of a public contract"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists items of a public contract"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Lists items of a public contract"""
        ...


class GetContractsPublicRegionIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a paginated list of all public contracts in the given region"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a paginated list of all public contracts in the given region"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a paginated list of all public contracts in the given region"""
        ...


class GetCorporationsCorporationIdContractsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
        ...


class GetCorporationsCorporationIdContractsContractIdBidsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists bids on a particular auction contract"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists bids on a particular auction contract"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Lists bids on a particular auction contract"""
        ...


class GetCorporationsCorporationIdContractsContractIdItemsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists items of a particular contract"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Lists items of a particular contract"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Lists items of a particular contract"""
        ...


class GetCorporationsCorporationIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsCorporationIdGet:
        """Public information about a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsCorporationIdGet]:
        """Public information about a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsCorporationIdGet]]:
        """Public information about a corporation"""
        ...


class GetCorporationsCorporationIdAlliancehistoryOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of all the alliances a corporation has been a member of"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of all the alliances a corporation has been a member of"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of all the alliances a corporation has been a member of"""
        ...


class GetCorporationsCorporationIdBlueprintsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a list of blueprints the corporation owns"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a list of blueprints the corporation owns"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a list of blueprints the corporation owns"""
        ...


class GetCorporationsCorporationIdContainersLogsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
        ...


class GetCorporationsCorporationIdDivisionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsCorporationIdDivisionsGet:
        """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsCorporationIdDivisionsGet]:
        """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsCorporationIdDivisionsGet]]:
        """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
        ...


class GetCorporationsCorporationIdFacilitiesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a corporation's facilities"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a corporation's facilities"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a corporation's facilities"""
        ...


class GetCorporationsCorporationIdIconsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsCorporationIdIconsGet:
        """Get the icon urls for a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsCorporationIdIconsGet]:
        """Get the icon urls for a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsCorporationIdIconsGet]]:
        """Get the icon urls for a corporation"""
        ...


class GetCorporationsCorporationIdMedalsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a corporation's medals"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a corporation's medals"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a corporation's medals"""
        ...


class GetCorporationsCorporationIdMedalsIssuedOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns medals issued by a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns medals issued by a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns medals issued by a corporation"""
        ...


class GetCorporationsCorporationIdMembersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
        ...


class GetCorporationsCorporationIdMembersLimitOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> int:
        """Return a corporation's member limit, not including CEO himself"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return a corporation's member limit, not including CEO himself"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Return a corporation's member limit, not including CEO himself"""
        ...


class GetCorporationsCorporationIdMembersTitlesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a corporation's members' titles"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a corporation's members' titles"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a corporation's members' titles"""
        ...


class GetCorporationsCorporationIdMembertrackingOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns additional information about a corporation's members which helps tracking their activities"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns additional information about a corporation's members which helps tracking their activities"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns additional information about a corporation's members which helps tracking their activities"""
        ...


class GetCorporationsCorporationIdRolesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return the roles of all members if the character has the personnel manager role or any grantable role."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return the roles of all members if the character has the personnel manager role or any grantable role."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return the roles of all members if the character has the personnel manager role or any grantable role."""
        ...


class GetCorporationsCorporationIdRolesHistoryOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return how roles have changed for a coporation's members, up to a month"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return how roles have changed for a coporation's members, up to a month"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return how roles have changed for a coporation's members, up to a month"""
        ...


class GetCorporationsCorporationIdShareholdersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return the current shareholders of a corporation."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return the current shareholders of a corporation."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return the current shareholders of a corporation."""
        ...


class GetCorporationsCorporationIdStandingsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return corporation standings from agents, NPC corporations, and factions"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return corporation standings from agents, NPC corporations, and factions"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return corporation standings from agents, NPC corporations, and factions"""
        ...


class GetCorporationsCorporationIdStarbasesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns list of corporation starbases (POSes)"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns list of corporation starbases (POSes)"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns list of corporation starbases (POSes)"""
        ...


class GetCorporationsCorporationIdStarbasesStarbaseIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsCorporationIdStarbasesStarbaseIdGet:
        """Returns various settings and fuels of a starbase (POS)"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsCorporationIdStarbasesStarbaseIdGet]:
        """Returns various settings and fuels of a starbase (POS)"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsCorporationIdStarbasesStarbaseIdGet]]:
        """Returns various settings and fuels of a starbase (POS)"""
        ...


class GetCorporationsCorporationIdStructuresOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
        ...


class GetCorporationsCorporationIdTitlesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a corporation's titles"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a corporation's titles"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a corporation's titles"""
        ...


class GetCorporationsNpccorpsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of npc corporations  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of npc corporations  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of npc corporations  This route expires daily at 11:05"""
        ...


class GetCorporationsProjectsContributionOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsProjectsContribution:
        """Show your contribution to a corporation project."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsProjectsContribution]:
        """Show your contribution to a corporation project."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsProjectsContribution]]:
        """Show your contribution to a corporation project."""
        ...


class GetCorporationsProjectsContributorsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsProjectsContributors:
        """Listing of all contributors to a corporation project."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsProjectsContributors]:
        """Listing of all contributors to a corporation project."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsProjectsContributors]]:
        """Listing of all contributors to a corporation project."""
        ...


class GetCorporationsProjectsDetailOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsProjectsDetail:
        """Get the details of a corporation project."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsProjectsDetail]:
        """Get the details of a corporation project."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsProjectsDetail]]:
        """Get the details of a corporation project."""
        ...


class GetCorporationsProjectsListingOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsProjectsListing:
        """Listing of all (active) corporation projects."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsProjectsListing]:
        """Listing of all (active) corporation projects."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsProjectsListing]]:
        """Listing of all (active) corporation projects."""
        ...


class GetDogmaAttributesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of dogma attribute ids  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of dogma attribute ids  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of dogma attribute ids  This route expires daily at 11:05"""
        ...


class GetDogmaAttributesAttributeIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> DogmaAttributesAttributeIdGet:
        """Get information on a dogma attribute  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[DogmaAttributesAttributeIdGet]:
        """Get information on a dogma attribute  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[DogmaAttributesAttributeIdGet]]:
        """Get information on a dogma attribute  This route expires daily at 11:05"""
        ...


class GetDogmaDynamicItemsTypeIdItemIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> DogmaDynamicItemsTypeIdItemIdGet:
        """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[DogmaDynamicItemsTypeIdItemIdGet]:
        """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[DogmaDynamicItemsTypeIdItemIdGet]]:
        """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
        ...


class GetDogmaEffectsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of dogma effect ids  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of dogma effect ids  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of dogma effect ids  This route expires daily at 11:05"""
        ...


class GetDogmaEffectsEffectIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> DogmaEffectsEffectIdGet:
        """Get information on a dogma effect  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[DogmaEffectsEffectIdGet]:
        """Get information on a dogma effect  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[DogmaEffectsEffectIdGet]]:
        """Get information on a dogma effect  This route expires daily at 11:05"""
        ...


class GetCharactersCharacterIdFwStatsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdFwStatsGet:
        """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdFwStatsGet]:
        """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdFwStatsGet]]:
        """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
        ...


class GetCorporationsCorporationIdFwStatsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CorporationsCorporationIdFwStatsGet:
        """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CorporationsCorporationIdFwStatsGet]:
        """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CorporationsCorporationIdFwStatsGet]]:
        """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
        ...


class GetFwLeaderboardsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> FwLeaderboardsGet:
        """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[FwLeaderboardsGet]:
        """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[FwLeaderboardsGet]]:
        """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...


class GetFwLeaderboardsCharactersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> FwLeaderboardsCharactersGet:
        """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[FwLeaderboardsCharactersGet]:
        """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[FwLeaderboardsCharactersGet]]:
        """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...


class GetFwLeaderboardsCorporationsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> FwLeaderboardsCorporationsGet:
        """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[FwLeaderboardsCorporationsGet]:
        """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[FwLeaderboardsCorporationsGet]]:
        """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
        ...


class GetFwStatsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
        ...


class GetFwSystemsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """An overview of the current ownership of faction warfare solar systems"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """An overview of the current ownership of faction warfare solar systems"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """An overview of the current ownership of faction warfare solar systems"""
        ...


class GetFwWarsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Data about which NPC factions are at war  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Data about which NPC factions are at war  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Data about which NPC factions are at war  This route expires daily at 11:05"""
        ...


class DeleteCharactersCharacterIdFittingsFittingIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Delete a fitting from a character"""
        ...

class GetCharactersCharacterIdFittingsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return fittings of a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return fittings of a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return fittings of a character"""
        ...


class PostCharactersCharacterIdFittingsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdFittingsPost:
        """Save a new fitting for a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdFittingsPost]:
        """Save a new fitting for a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdFittingsPost]]:
        """Save a new fitting for a character"""
        ...


class DeleteFleetsFleetIdMembersMemberIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Kick a fleet member"""
        ...

class DeleteFleetsFleetIdSquadsSquadIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Delete a fleet squad, only empty squads can be deleted"""
        ...

class DeleteFleetsFleetIdWingsWingIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty"""
        ...

class GetCharactersCharacterIdFleetOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdFleetGet:
        """Return the fleet ID the character is in, if any."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdFleetGet]:
        """Return the fleet ID the character is in, if any."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdFleetGet]]:
        """Return the fleet ID the character is in, if any."""
        ...


class GetFleetsFleetIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> FleetsFleetIdGet:
        """Return details about a fleet"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[FleetsFleetIdGet]:
        """Return details about a fleet"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[FleetsFleetIdGet]]:
        """Return details about a fleet"""
        ...


class GetFleetsFleetIdMembersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return information about fleet members"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return information about fleet members"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return information about fleet members"""
        ...


class GetFleetsFleetIdWingsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return information about wings in a fleet"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return information about wings in a fleet"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return information about wings in a fleet"""
        ...


class PostFleetsFleetIdMembersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
        ...


class PostFleetsFleetIdWingsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> FleetsFleetIdWingsPost:
        """Create a new wing in a fleet"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[FleetsFleetIdWingsPost]:
        """Create a new wing in a fleet"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[FleetsFleetIdWingsPost]]:
        """Create a new wing in a fleet"""
        ...


class PostFleetsFleetIdWingsWingIdSquadsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> FleetsFleetIdWingsWingIdSquadsPost:
        """Create a new squad in a fleet"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[FleetsFleetIdWingsWingIdSquadsPost]:
        """Create a new squad in a fleet"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[FleetsFleetIdWingsWingIdSquadsPost]]:
        """Create a new squad in a fleet"""
        ...


class PutFleetsFleetIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Update settings about a fleet"""
        ...

class PutFleetsFleetIdMembersMemberIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Move a fleet member around"""
        ...

class PutFleetsFleetIdSquadsSquadIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Rename a fleet squad"""
        ...

class PutFleetsFleetIdWingsWingIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Rename a fleet wing"""
        ...

class GetIncursionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of current incursions"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of current incursions"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of current incursions"""
        ...


class GetCharactersCharacterIdIndustryJobsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List industry jobs placed by a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List industry jobs placed by a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List industry jobs placed by a character"""
        ...


class GetCharactersCharacterIdMiningOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Paginated record of all mining done by a character for the past 30 days"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Paginated record of all mining done by a character for the past 30 days"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Paginated record of all mining done by a character for the past 30 days"""
        ...


class GetCorporationCorporationIdMiningExtractionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
        ...


class GetCorporationCorporationIdMiningObserversOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Paginated list of all entities capable of observing and recording mining for a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Paginated list of all entities capable of observing and recording mining for a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Paginated list of all entities capable of observing and recording mining for a corporation"""
        ...


class GetCorporationCorporationIdMiningObserversObserverIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Paginated record of all mining seen by an observer"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Paginated record of all mining seen by an observer"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Paginated record of all mining seen by an observer"""
        ...


class GetCorporationsCorporationIdIndustryJobsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List industry jobs run by a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List industry jobs run by a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List industry jobs run by a corporation"""
        ...


class GetIndustryFacilitiesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of industry facilities"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of industry facilities"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of industry facilities"""
        ...


class GetIndustrySystemsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return cost indices for solar systems"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return cost indices for solar systems"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return cost indices for solar systems"""
        ...


class GetInsurancePricesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return available insurance levels for all ship types"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return available insurance levels for all ship types"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return available insurance levels for all ship types"""
        ...


class GetCharactersCharacterIdKillmailsRecentOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of a character's kills and losses going back 90 days"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of a character's kills and losses going back 90 days"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of a character's kills and losses going back 90 days"""
        ...


class GetCorporationsCorporationIdKillmailsRecentOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of a corporation's kills and losses going back 90 days"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of a corporation's kills and losses going back 90 days"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of a corporation's kills and losses going back 90 days"""
        ...


class GetKillmailsKillmailIdKillmailHashOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> KillmailsKillmailIdKillmailHashGet:
        """Return a single killmail from its ID and hash"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[KillmailsKillmailIdKillmailHashGet]:
        """Return a single killmail from its ID and hash"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[KillmailsKillmailIdKillmailHashGet]]:
        """Return a single killmail from its ID and hash"""
        ...


class GetCharactersCharacterIdLocationOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdLocationGet:
        """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdLocationGet]:
        """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdLocationGet]]:
        """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
        ...


class GetCharactersCharacterIdOnlineOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdOnlineGet:
        """Checks if the character is currently online"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdOnlineGet]:
        """Checks if the character is currently online"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdOnlineGet]]:
        """Checks if the character is currently online"""
        ...


class GetCharactersCharacterIdShipOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdShipGet:
        """Get the current ship type, name and id"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdShipGet]:
        """Get the current ship type, name and id"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdShipGet]]:
        """Get the current ship type, name and id"""
        ...


class GetCharactersCharacterIdLoyaltyPointsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of loyalty points for all corporations the character has worked for"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of loyalty points for all corporations the character has worked for"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of loyalty points for all corporations the character has worked for"""
        ...


class GetLoyaltyStoresCorporationIdOffersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
        ...


class DeleteCharactersCharacterIdMailLabelsLabelIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Delete a mail label"""
        ...

class DeleteCharactersCharacterIdMailMailIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Delete a mail"""
        ...

class GetCharactersCharacterIdMailOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
        ...


class GetCharactersCharacterIdMailLabelsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdMailLabelsGet:
        """Return a list of the users mail labels, unread counts for each label and a total unread count."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdMailLabelsGet]:
        """Return a list of the users mail labels, unread counts for each label and a total unread count."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdMailLabelsGet]]:
        """Return a list of the users mail labels, unread counts for each label and a total unread count."""
        ...


class GetCharactersCharacterIdMailListsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return all mailing lists that the character is subscribed to"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return all mailing lists that the character is subscribed to"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return all mailing lists that the character is subscribed to"""
        ...


class GetCharactersCharacterIdMailMailIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdMailMailIdGet:
        """Return the contents of an EVE mail"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdMailMailIdGet]:
        """Return the contents of an EVE mail"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdMailMailIdGet]]:
        """Return the contents of an EVE mail"""
        ...


class PostCharactersCharacterIdMailOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> int:
        """Create and send a new mail"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Create and send a new mail"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Create and send a new mail"""
        ...


class PostCharactersCharacterIdMailLabelsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> int:
        """Create a mail label"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Create a mail label"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Create a mail label"""
        ...


class PutCharactersCharacterIdMailMailIdOperation(EsiOperation):
    """ESIClientOperation, use result()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> None:
        """Update metadata about a mail"""
        ...

class GetCharactersCharacterIdOrdersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List open market orders placed by a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List open market orders placed by a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List open market orders placed by a character"""
        ...


class GetCharactersCharacterIdOrdersHistoryOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List cancelled and expired market orders placed by a character up to 90 days in the past."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List cancelled and expired market orders placed by a character up to 90 days in the past."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List cancelled and expired market orders placed by a character up to 90 days in the past."""
        ...


class GetCorporationsCorporationIdOrdersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List open market orders placed on behalf of a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List open market orders placed on behalf of a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List open market orders placed on behalf of a corporation"""
        ...


class GetCorporationsCorporationIdOrdersHistoryOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
        ...


class GetMarketsGroupsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...


class GetMarketsGroupsMarketGroupIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> MarketsGroupsMarketGroupIdGet:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[MarketsGroupsMarketGroupIdGet]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[MarketsGroupsMarketGroupIdGet]]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...


class GetMarketsPricesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of prices"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of prices"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of prices"""
        ...


class GetMarketsRegionIdHistoryOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
        ...


class GetMarketsRegionIdOrdersOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of orders in a region"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of orders in a region"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of orders in a region"""
        ...


class GetMarketsRegionIdTypesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
        ...


class GetMarketsStructuresStructureIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return all orders in a structure"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return all orders in a structure"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return all orders in a structure"""
        ...


class GetMetaChangelogOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> MetaChangelog:
        """Get the changelog of this API."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[MetaChangelog]:
        """Get the changelog of this API."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[MetaChangelog]]:
        """Get the changelog of this API."""
        ...


class GetMetaCompatibilityDatesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> MetaCompatibilityDates:
        """Get a list of compatibility dates."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[MetaCompatibilityDates]:
        """Get a list of compatibility dates."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[MetaCompatibilityDates]]:
        """Get a list of compatibility dates."""
        ...


class GetCharactersCharacterIdPlanetsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a list of all planetary colonies owned by a character."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Returns a list of all planetary colonies owned by a character."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Returns a list of all planetary colonies owned by a character."""
        ...


class GetCharactersCharacterIdPlanetsPlanetIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdPlanetsPlanetIdGet:
        """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdPlanetsPlanetIdGet]:
        """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdPlanetsPlanetIdGet]]:
        """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
        ...


class GetCorporationsCorporationIdCustomsOfficesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List customs offices owned by a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List customs offices owned by a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List customs offices owned by a corporation"""
        ...


class GetUniverseSchematicsSchematicIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseSchematicsSchematicIdGet:
        """Get information on a planetary factory schematic"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseSchematicsSchematicIdGet]:
        """Get information on a planetary factory schematic"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseSchematicsSchematicIdGet]]:
        """Get information on a planetary factory schematic"""
        ...


class GetRouteOriginDestinationOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get the systems between origin and destination"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get the systems between origin and destination"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get the systems between origin and destination"""
        ...


class GetCharactersCharacterIdSearchOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdSearchGet:
        """Search for entities that match a given sub-string."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdSearchGet]:
        """Search for entities that match a given sub-string."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdSearchGet]]:
        """Search for entities that match a given sub-string."""
        ...


class GetCharactersCharacterIdAttributesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdAttributesGet:
        """Return attributes of a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdAttributesGet]:
        """Return attributes of a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdAttributesGet]]:
        """Return attributes of a character"""
        ...


class GetCharactersCharacterIdSkillqueueOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List the configured skill queue for the given character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """List the configured skill queue for the given character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """List the configured skill queue for the given character"""
        ...


class GetCharactersCharacterIdSkillsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> CharactersCharacterIdSkillsGet:
        """List all trained skills for the given character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[CharactersCharacterIdSkillsGet]:
        """List all trained skills for the given character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[CharactersCharacterIdSkillsGet]]:
        """List all trained skills for the given character"""
        ...


class GetSovereigntyCampaignsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Shows sovereignty data for campaigns."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Shows sovereignty data for campaigns."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Shows sovereignty data for campaigns."""
        ...


class GetSovereigntyMapOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Shows sovereignty information for solar systems"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Shows sovereignty information for solar systems"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Shows sovereignty information for solar systems"""
        ...


class GetSovereigntyStructuresOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Shows sovereignty data for structures."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Shows sovereignty data for structures."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Shows sovereignty data for structures."""
        ...


class GetStatusOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> StatusGet:
        """EVE Server status"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[StatusGet]:
        """EVE Server status"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[StatusGet]]:
        """EVE Server status"""
        ...


class GetUniverseAncestriesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get all character ancestries  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get all character ancestries  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get all character ancestries  This route expires daily at 11:05"""
        ...


class GetUniverseAsteroidBeltsAsteroidBeltIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseAsteroidBeltsAsteroidBeltIdGet:
        """Get information on an asteroid belt  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseAsteroidBeltsAsteroidBeltIdGet]:
        """Get information on an asteroid belt  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseAsteroidBeltsAsteroidBeltIdGet]]:
        """Get information on an asteroid belt  This route expires daily at 11:05"""
        ...


class GetUniverseBloodlinesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of bloodlines  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of bloodlines  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of bloodlines  This route expires daily at 11:05"""
        ...


class GetUniverseCategoriesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of item categories  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of item categories  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of item categories  This route expires daily at 11:05"""
        ...


class GetUniverseCategoriesCategoryIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseCategoriesCategoryIdGet:
        """Get information of an item category  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseCategoriesCategoryIdGet]:
        """Get information of an item category  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseCategoriesCategoryIdGet]]:
        """Get information of an item category  This route expires daily at 11:05"""
        ...


class GetUniverseConstellationsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of constellations  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of constellations  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of constellations  This route expires daily at 11:05"""
        ...


class GetUniverseConstellationsConstellationIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseConstellationsConstellationIdGet:
        """Get information on a constellation  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseConstellationsConstellationIdGet]:
        """Get information on a constellation  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseConstellationsConstellationIdGet]]:
        """Get information on a constellation  This route expires daily at 11:05"""
        ...


class GetUniverseFactionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of factions  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of factions  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of factions  This route expires daily at 11:05"""
        ...


class GetUniverseGraphicsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of graphics  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of graphics  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of graphics  This route expires daily at 11:05"""
        ...


class GetUniverseGraphicsGraphicIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseGraphicsGraphicIdGet:
        """Get information on a graphic  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseGraphicsGraphicIdGet]:
        """Get information on a graphic  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseGraphicsGraphicIdGet]]:
        """Get information on a graphic  This route expires daily at 11:05"""
        ...


class GetUniverseGroupsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of item groups  This route expires daily at 11:05"""
        ...


class GetUniverseGroupsGroupIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseGroupsGroupIdGet:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseGroupsGroupIdGet]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseGroupsGroupIdGet]]:
        """Get information on an item group  This route expires daily at 11:05"""
        ...


class GetUniverseMoonsMoonIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseMoonsMoonIdGet:
        """Get information on a moon  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseMoonsMoonIdGet]:
        """Get information on a moon  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseMoonsMoonIdGet]]:
        """Get information on a moon  This route expires daily at 11:05"""
        ...


class GetUniversePlanetsPlanetIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniversePlanetsPlanetIdGet:
        """Get information on a planet  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniversePlanetsPlanetIdGet]:
        """Get information on a planet  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniversePlanetsPlanetIdGet]]:
        """Get information on a planet  This route expires daily at 11:05"""
        ...


class GetUniverseRacesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of character races  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a list of character races  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a list of character races  This route expires daily at 11:05"""
        ...


class GetUniverseRegionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of regions  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of regions  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of regions  This route expires daily at 11:05"""
        ...


class GetUniverseRegionsRegionIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseRegionsRegionIdGet:
        """Get information on a region  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseRegionsRegionIdGet]:
        """Get information on a region  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseRegionsRegionIdGet]]:
        """Get information on a region  This route expires daily at 11:05"""
        ...


class GetUniverseStargatesStargateIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseStargatesStargateIdGet:
        """Get information on a stargate  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseStargatesStargateIdGet]:
        """Get information on a stargate  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseStargatesStargateIdGet]]:
        """Get information on a stargate  This route expires daily at 11:05"""
        ...


class GetUniverseStarsStarIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseStarsStarIdGet:
        """Get information on a star  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseStarsStarIdGet]:
        """Get information on a star  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseStarsStarIdGet]]:
        """Get information on a star  This route expires daily at 11:05"""
        ...


class GetUniverseStationsStationIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseStationsStationIdGet:
        """Get information on a station  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseStationsStationIdGet]:
        """Get information on a station  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseStationsStationIdGet]]:
        """Get information on a station  This route expires daily at 11:05"""
        ...


class GetUniverseStructuresOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """List all public structures"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """List all public structures"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """List all public structures"""
        ...


class GetUniverseStructuresStructureIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseStructuresStructureIdGet:
        """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseStructuresStructureIdGet]:
        """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseStructuresStructureIdGet]]:
        """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
        ...


class GetUniverseSystemJumpsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
        ...


class GetUniverseSystemKillsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
        ...


class GetUniverseSystemsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of solar systems  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of solar systems  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of solar systems  This route expires daily at 11:05"""
        ...


class GetUniverseSystemsSystemIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseSystemsSystemIdGet:
        """Get information on a solar system.  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseSystemsSystemIdGet]:
        """Get information on a solar system.  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseSystemsSystemIdGet]]:
        """Get information on a solar system.  This route expires daily at 11:05"""
        ...


class GetUniverseTypesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of type ids  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Get a list of type ids  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Get a list of type ids  This route expires daily at 11:05"""
        ...


class GetUniverseTypesTypeIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> UniverseTypesTypeIdGet:
        """Get information on a type  This route expires daily at 11:05"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[UniverseTypesTypeIdGet]:
        """Get information on a type  This route expires daily at 11:05"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[UniverseTypesTypeIdGet]]:
        """Get information on a type  This route expires daily at 11:05"""
        ...


class PostUniverseIdsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
        ...


class PostUniverseNamesOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
        ...


class PostUiAutopilotWaypointOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Set a solar system as autopilot waypoint"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Set a solar system as autopilot waypoint"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Set a solar system as autopilot waypoint"""
        ...


class PostUiOpenwindowContractOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Open the contract window inside the client"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Open the contract window inside the client"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Open the contract window inside the client"""
        ...


class PostUiOpenwindowInformationOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Open the information window for a character, corporation or alliance inside the client"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Open the information window for a character, corporation or alliance inside the client"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Open the information window for a character, corporation or alliance inside the client"""
        ...


class PostUiOpenwindowMarketdetailsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Open the market details window for a specific typeID inside the client"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Open the market details window for a specific typeID inside the client"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Open the market details window for a specific typeID inside the client"""
        ...


class PostUiOpenwindowNewmailOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> Any:
        """Open the New Mail window, according to settings from the request if applicable"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[Any]:
        """Open the New Mail window, according to settings from the request if applicable"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[Any]]:
        """Open the New Mail window, according to settings from the request if applicable"""
        ...


class GetCharactersCharacterIdWalletOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> float:
        """Returns a character's wallet balance"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[float]:
        """Returns a character's wallet balance"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[float]]:
        """Returns a character's wallet balance"""
        ...


class GetCharactersCharacterIdWalletJournalOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Retrieve the given character's wallet journal going 30 days back"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Retrieve the given character's wallet journal going 30 days back"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Retrieve the given character's wallet journal going 30 days back"""
        ...


class GetCharactersCharacterIdWalletTransactionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get wallet transactions of a character"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get wallet transactions of a character"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get wallet transactions of a character"""
        ...


class GetCorporationsCorporationIdWalletsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a corporation's wallets"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get a corporation's wallets"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get a corporation's wallets"""
        ...


class GetCorporationsCorporationIdWalletsDivisionJournalOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
        ...


class GetCorporationsCorporationIdWalletsDivisionTransactionsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get wallet transactions of a corporation"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Get wallet transactions of a corporation"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Get wallet transactions of a corporation"""
        ...


class GetWarsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return a list of wars"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[int]:
        """Return a list of wars"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[int]]:
        """Return a list of wars"""
        ...


class GetWarsWarIdOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> WarsWarIdGet:
        """Return details about a war"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[WarsWarIdGet]:
        """Return details about a war"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[WarsWarIdGet]]:
        """Return details about a war"""
        ...


class GetWarsWarIdKillmailsOperation(EsiOperation):
    """ESIClientOperation, use result(), results() or results_localized()"""
    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of kills related to a war"""
        ...

    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> List[InlineModel]:
        """Return a list of kills related to a war"""
        ...

    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, List[InlineModel]]:
        """Return a list of kills related to a war"""
        ...


class ESIClientStub:
    class _Alliance:
        def GetAlliances(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetAlliancesOperation:
            """List all active player alliances"""
            ...

        def GetAlliancesAllianceId(self, alliance_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetAlliancesAllianceIdOperation:
            """Public information about an alliance"""
            ...

        def GetAlliancesAllianceIdCorporations(self, alliance_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetAlliancesAllianceIdCorporationsOperation:
            """List all current member corporations of an alliance"""
            ...

        def GetAlliancesAllianceIdIcons(self, alliance_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetAlliancesAllianceIdIconsOperation:
            """Get the icon urls for a alliance  This route expires daily at 11:05"""
            ...


    Alliance: _Alliance = _Alliance()

    class _Assets:
        def GetCharactersCharacterIdAssets(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdAssetsOperation:
            """Return a list of the characters assets"""
            ...

        def GetCorporationsCorporationIdAssets(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdAssetsOperation:
            """Return a list of the corporation assets"""
            ...

        def PostCharactersCharacterIdAssetsLocations(self, body: List[int], character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdAssetsLocationsOperation:
            """Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
            ...

        def PostCharactersCharacterIdAssetsNames(self, body: List[int], character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdAssetsNamesOperation:
            """Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships."""
            ...

        def PostCorporationsCorporationIdAssetsLocations(self, body: List[int], corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCorporationsCorporationIdAssetsLocationsOperation:
            """Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)"""
            ...

        def PostCorporationsCorporationIdAssetsNames(self, body: List[int], corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCorporationsCorporationIdAssetsNamesOperation:
            """Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships"""
            ...


    Assets: _Assets = _Assets()

    class _Calendar:
        def GetCharactersCharacterIdCalendar(self, character_id: int, token: Token, from_event: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdCalendarOperation:
            """Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event"""
            ...

        def GetCharactersCharacterIdCalendarEventId(self, character_id: int, event_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdCalendarEventIdOperation:
            """Get all the information for a specific event"""
            ...

        def GetCharactersCharacterIdCalendarEventIdAttendees(self, character_id: int, event_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdCalendarEventIdAttendeesOperation:
            """Get all invited attendees for a given event"""
            ...

        def PutCharactersCharacterIdCalendarEventId(self, body: InlineModel, character_id: int, event_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutCharactersCharacterIdCalendarEventIdOperation:
            """Set your response status to an event"""
            ...


    Calendar: _Calendar = _Calendar()

    class _Character:
        def GetCharactersCharacterId(self, character_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdOperation:
            """Public information about a character"""
            ...

        def GetCharactersCharacterIdAgentsResearch(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdAgentsResearchOperation:
            """Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)"""
            ...

        def GetCharactersCharacterIdBlueprints(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdBlueprintsOperation:
            """Return a list of blueprints the character owns"""
            ...

        def GetCharactersCharacterIdCorporationhistory(self, character_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdCorporationhistoryOperation:
            """Get a list of all the corporations a character has been a member of"""
            ...

        def GetCharactersCharacterIdFatigue(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdFatigueOperation:
            """Return a character's jump activation and fatigue information"""
            ...

        def GetCharactersCharacterIdMedals(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdMedalsOperation:
            """Return a list of medals the character has"""
            ...

        def GetCharactersCharacterIdNotifications(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdNotificationsOperation:
            """Return character notifications"""
            ...

        def GetCharactersCharacterIdNotificationsContacts(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdNotificationsContactsOperation:
            """Return notifications about having been added to someone's contact list"""
            ...

        def GetCharactersCharacterIdPortrait(self, character_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdPortraitOperation:
            """Get portrait urls for a character  This route expires daily at 11:05"""
            ...

        def GetCharactersCharacterIdRoles(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdRolesOperation:
            """Returns a character's corporation roles"""
            ...

        def GetCharactersCharacterIdStandings(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdStandingsOperation:
            """Return character standings from agents, NPC corporations, and factions"""
            ...

        def GetCharactersCharacterIdTitles(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdTitlesOperation:
            """Returns a character's titles"""
            ...

        def PostCharactersAffiliation(self, body: List[int], Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersAffiliationOperation:
            """Bulk lookup of character IDs to corporation, alliance and faction"""
            ...

        def PostCharactersCharacterIdCspa(self, body: List[int], character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdCspaOperation:
            """Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost"""
            ...


    Character: _Character = _Character()

    class _Clones:
        def GetCharactersCharacterIdClones(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdClonesOperation:
            """A list of the character's clones"""
            ...

        def GetCharactersCharacterIdImplants(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdImplantsOperation:
            """Return implants on the active clone of a character"""
            ...


    Clones: _Clones = _Clones()

    class _Contacts:
        def DeleteCharactersCharacterIdContacts(self, character_id: int, contact_ids: list[Any], token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteCharactersCharacterIdContactsOperation:
            """Bulk delete contacts"""
            ...

        def GetAlliancesAllianceIdContacts(self, alliance_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetAlliancesAllianceIdContactsOperation:
            """Return contacts of an alliance"""
            ...

        def GetAlliancesAllianceIdContactsLabels(self, alliance_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetAlliancesAllianceIdContactsLabelsOperation:
            """Return custom labels for an alliance's contacts"""
            ...

        def GetCharactersCharacterIdContacts(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdContactsOperation:
            """Return contacts of a character"""
            ...

        def GetCharactersCharacterIdContactsLabels(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdContactsLabelsOperation:
            """Return custom labels for a character's contacts"""
            ...

        def GetCorporationsCorporationIdContacts(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdContactsOperation:
            """Return contacts of a corporation"""
            ...

        def GetCorporationsCorporationIdContactsLabels(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdContactsLabelsOperation:
            """Return custom labels for a corporation's contacts"""
            ...

        def PostCharactersCharacterIdContacts(self, body: List[int], character_id: int, standing: float, token: Token, label_ids: Optional[list[Any]] = ..., watched: Optional[bool] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdContactsOperation:
            """Bulk add contacts with same settings"""
            ...

        def PutCharactersCharacterIdContacts(self, body: List[int], character_id: int, standing: float, token: Token, label_ids: Optional[list[Any]] = ..., watched: Optional[bool] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutCharactersCharacterIdContactsOperation:
            """Bulk edit contacts with same settings"""
            ...


    Contacts: _Contacts = _Contacts()

    class _Contracts:
        def GetCharactersCharacterIdContracts(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdContractsOperation:
            """Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
            ...

        def GetCharactersCharacterIdContractsContractIdBids(self, character_id: int, contract_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdContractsContractIdBidsOperation:
            """Lists bids on a particular auction contract"""
            ...

        def GetCharactersCharacterIdContractsContractIdItems(self, character_id: int, contract_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdContractsContractIdItemsOperation:
            """Lists items of a particular contract"""
            ...

        def GetContractsPublicBidsContractId(self, contract_id: int, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetContractsPublicBidsContractIdOperation:
            """Lists bids on a public auction contract"""
            ...

        def GetContractsPublicItemsContractId(self, contract_id: int, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetContractsPublicItemsContractIdOperation:
            """Lists items of a public contract"""
            ...

        def GetContractsPublicRegionId(self, region_id: int, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetContractsPublicRegionIdOperation:
            """Returns a paginated list of all public contracts in the given region"""
            ...

        def GetCorporationsCorporationIdContracts(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdContractsOperation:
            """Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress"."""
            ...

        def GetCorporationsCorporationIdContractsContractIdBids(self, contract_id: int, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdContractsContractIdBidsOperation:
            """Lists bids on a particular auction contract"""
            ...

        def GetCorporationsCorporationIdContractsContractIdItems(self, contract_id: int, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdContractsContractIdItemsOperation:
            """Lists items of a particular contract"""
            ...


    Contracts: _Contracts = _Contracts()

    class _Corporation:
        def GetCorporationsCorporationId(self, corporation_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdOperation:
            """Public information about a corporation"""
            ...

        def GetCorporationsCorporationIdAlliancehistory(self, corporation_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdAlliancehistoryOperation:
            """Get a list of all the alliances a corporation has been a member of"""
            ...

        def GetCorporationsCorporationIdBlueprints(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdBlueprintsOperation:
            """Returns a list of blueprints the corporation owns"""
            ...

        def GetCorporationsCorporationIdContainersLogs(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdContainersLogsOperation:
            """Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation"""
            ...

        def GetCorporationsCorporationIdDivisions(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdDivisionsOperation:
            """Return corporation hangar and wallet division names, only show if a division is not using the default name"""
            ...

        def GetCorporationsCorporationIdFacilities(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdFacilitiesOperation:
            """Return a corporation's facilities"""
            ...

        def GetCorporationsCorporationIdIcons(self, corporation_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdIconsOperation:
            """Get the icon urls for a corporation"""
            ...

        def GetCorporationsCorporationIdMedals(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdMedalsOperation:
            """Returns a corporation's medals"""
            ...

        def GetCorporationsCorporationIdMedalsIssued(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdMedalsIssuedOperation:
            """Returns medals issued by a corporation"""
            ...

        def GetCorporationsCorporationIdMembers(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdMembersOperation:
            """Return the current member list of a corporation, the token's character need to be a member of the corporation."""
            ...

        def GetCorporationsCorporationIdMembersLimit(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdMembersLimitOperation:
            """Return a corporation's member limit, not including CEO himself"""
            ...

        def GetCorporationsCorporationIdMembersTitles(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdMembersTitlesOperation:
            """Returns a corporation's members' titles"""
            ...

        def GetCorporationsCorporationIdMembertracking(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdMembertrackingOperation:
            """Returns additional information about a corporation's members which helps tracking their activities"""
            ...

        def GetCorporationsCorporationIdRoles(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdRolesOperation:
            """Return the roles of all members if the character has the personnel manager role or any grantable role."""
            ...

        def GetCorporationsCorporationIdRolesHistory(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdRolesHistoryOperation:
            """Return how roles have changed for a coporation's members, up to a month"""
            ...

        def GetCorporationsCorporationIdShareholders(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdShareholdersOperation:
            """Return the current shareholders of a corporation."""
            ...

        def GetCorporationsCorporationIdStandings(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdStandingsOperation:
            """Return corporation standings from agents, NPC corporations, and factions"""
            ...

        def GetCorporationsCorporationIdStarbases(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdStarbasesOperation:
            """Returns list of corporation starbases (POSes)"""
            ...

        def GetCorporationsCorporationIdStarbasesStarbaseId(self, corporation_id: int, starbase_id: int, system_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdStarbasesStarbaseIdOperation:
            """Returns various settings and fuels of a starbase (POS)"""
            ...

        def GetCorporationsCorporationIdStructures(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdStructuresOperation:
            """Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th"""
            ...

        def GetCorporationsCorporationIdTitles(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdTitlesOperation:
            """Returns a corporation's titles"""
            ...

        def GetCorporationsNpccorps(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsNpccorpsOperation:
            """Get a list of npc corporations  This route expires daily at 11:05"""
            ...


    Corporation: _Corporation = _Corporation()

    class _Corporation_Projects:
        def GetCorporationsProjectsContribution(self, corporation_id: int, project_id: str, character_id: int, token: Token, If_Modified_Since: Optional[str] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsProjectsContributionOperation:
            """Show your contribution to a corporation project."""
            ...

        def GetCorporationsProjectsContributors(self, corporation_id: int, project_id: str, token: Token, after: Optional[str] = ..., before: Optional[str] = ..., limit: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsProjectsContributorsOperation:
            """Listing of all contributors to a corporation project."""
            ...

        def GetCorporationsProjectsDetail(self, corporation_id: int, project_id: str, token: Token, If_Modified_Since: Optional[str] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsProjectsDetailOperation:
            """Get the details of a corporation project."""
            ...

        def GetCorporationsProjectsListing(self, corporation_id: int, token: Token, after: Optional[str] = ..., before: Optional[str] = ..., limit: Optional[int] = ..., state: Optional[str] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsProjectsListingOperation:
            """Listing of all (active) corporation projects."""
            ...


    Corporation_Projects: _Corporation_Projects = _Corporation_Projects()

    class _Dogma:
        def GetDogmaAttributes(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetDogmaAttributesOperation:
            """Get a list of dogma attribute ids  This route expires daily at 11:05"""
            ...

        def GetDogmaAttributesAttributeId(self, attribute_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetDogmaAttributesAttributeIdOperation:
            """Get information on a dogma attribute  This route expires daily at 11:05"""
            ...

        def GetDogmaDynamicItemsTypeIdItemId(self, item_id: int, type_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetDogmaDynamicItemsTypeIdItemIdOperation:
            """Returns info about a dynamic item resulting from mutation with a mutaplasmid.  This route expires daily at 11:05"""
            ...

        def GetDogmaEffects(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetDogmaEffectsOperation:
            """Get a list of dogma effect ids  This route expires daily at 11:05"""
            ...

        def GetDogmaEffectsEffectId(self, effect_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetDogmaEffectsEffectIdOperation:
            """Get information on a dogma effect  This route expires daily at 11:05"""
            ...


    Dogma: _Dogma = _Dogma()

    class _Faction_Warfare:
        def GetCharactersCharacterIdFwStats(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdFwStatsOperation:
            """Statistical overview of a character involved in faction warfare  This route expires daily at 11:05"""
            ...

        def GetCorporationsCorporationIdFwStats(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdFwStatsOperation:
            """Statistics about a corporation involved in faction warfare  This route expires daily at 11:05"""
            ...

        def GetFwLeaderboards(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFwLeaderboardsOperation:
            """Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
            ...

        def GetFwLeaderboardsCharacters(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFwLeaderboardsCharactersOperation:
            """Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
            ...

        def GetFwLeaderboardsCorporations(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFwLeaderboardsCorporationsOperation:
            """Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  This route expires daily at 11:05"""
            ...

        def GetFwStats(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFwStatsOperation:
            """Statistical overviews of factions involved in faction warfare  This route expires daily at 11:05"""
            ...

        def GetFwSystems(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFwSystemsOperation:
            """An overview of the current ownership of faction warfare solar systems"""
            ...

        def GetFwWars(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFwWarsOperation:
            """Data about which NPC factions are at war  This route expires daily at 11:05"""
            ...


    Faction_Warfare: _Faction_Warfare = _Faction_Warfare()

    class _Fittings:
        def DeleteCharactersCharacterIdFittingsFittingId(self, character_id: int, fitting_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteCharactersCharacterIdFittingsFittingIdOperation:
            """Delete a fitting from a character"""
            ...

        def GetCharactersCharacterIdFittings(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdFittingsOperation:
            """Return fittings of a character"""
            ...

        def PostCharactersCharacterIdFittings(self, body: InlineModel, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdFittingsOperation:
            """Save a new fitting for a character"""
            ...


    Fittings: _Fittings = _Fittings()

    class _Fleets:
        def DeleteFleetsFleetIdMembersMemberId(self, fleet_id: int, member_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteFleetsFleetIdMembersMemberIdOperation:
            """Kick a fleet member"""
            ...

        def DeleteFleetsFleetIdSquadsSquadId(self, fleet_id: int, squad_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteFleetsFleetIdSquadsSquadIdOperation:
            """Delete a fleet squad, only empty squads can be deleted"""
            ...

        def DeleteFleetsFleetIdWingsWingId(self, fleet_id: int, wing_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteFleetsFleetIdWingsWingIdOperation:
            """Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty"""
            ...

        def GetCharactersCharacterIdFleet(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdFleetOperation:
            """Return the fleet ID the character is in, if any."""
            ...

        def GetFleetsFleetId(self, fleet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFleetsFleetIdOperation:
            """Return details about a fleet"""
            ...

        def GetFleetsFleetIdMembers(self, fleet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFleetsFleetIdMembersOperation:
            """Return information about fleet members"""
            ...

        def GetFleetsFleetIdWings(self, fleet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetFleetsFleetIdWingsOperation:
            """Return information about wings in a fleet"""
            ...

        def PostFleetsFleetIdMembers(self, body: InlineModel, fleet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostFleetsFleetIdMembersOperation:
            """Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI"""
            ...

        def PostFleetsFleetIdWings(self, fleet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostFleetsFleetIdWingsOperation:
            """Create a new wing in a fleet"""
            ...

        def PostFleetsFleetIdWingsWingIdSquads(self, fleet_id: int, wing_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostFleetsFleetIdWingsWingIdSquadsOperation:
            """Create a new squad in a fleet"""
            ...

        def PutFleetsFleetId(self, body: InlineModel, fleet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutFleetsFleetIdOperation:
            """Update settings about a fleet"""
            ...

        def PutFleetsFleetIdMembersMemberId(self, body: InlineModel, fleet_id: int, member_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutFleetsFleetIdMembersMemberIdOperation:
            """Move a fleet member around"""
            ...

        def PutFleetsFleetIdSquadsSquadId(self, body: InlineModel, fleet_id: int, squad_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutFleetsFleetIdSquadsSquadIdOperation:
            """Rename a fleet squad"""
            ...

        def PutFleetsFleetIdWingsWingId(self, body: InlineModel, fleet_id: int, wing_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutFleetsFleetIdWingsWingIdOperation:
            """Rename a fleet wing"""
            ...


    Fleets: _Fleets = _Fleets()

    class _Incursions:
        def GetIncursions(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetIncursionsOperation:
            """Return a list of current incursions"""
            ...


    Incursions: _Incursions = _Incursions()

    class _Industry:
        def GetCharactersCharacterIdIndustryJobs(self, character_id: int, token: Token, include_completed: Optional[bool] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdIndustryJobsOperation:
            """List industry jobs placed by a character"""
            ...

        def GetCharactersCharacterIdMining(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdMiningOperation:
            """Paginated record of all mining done by a character for the past 30 days"""
            ...

        def GetCorporationCorporationIdMiningExtractions(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationCorporationIdMiningExtractionsOperation:
            """Extraction timers for all moon chunks being extracted by refineries belonging to a corporation."""
            ...

        def GetCorporationCorporationIdMiningObservers(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationCorporationIdMiningObserversOperation:
            """Paginated list of all entities capable of observing and recording mining for a corporation"""
            ...

        def GetCorporationCorporationIdMiningObserversObserverId(self, corporation_id: int, observer_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationCorporationIdMiningObserversObserverIdOperation:
            """Paginated record of all mining seen by an observer"""
            ...

        def GetCorporationsCorporationIdIndustryJobs(self, corporation_id: int, token: Token, include_completed: Optional[bool] = ..., page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdIndustryJobsOperation:
            """List industry jobs run by a corporation"""
            ...

        def GetIndustryFacilities(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetIndustryFacilitiesOperation:
            """Return a list of industry facilities"""
            ...

        def GetIndustrySystems(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetIndustrySystemsOperation:
            """Return cost indices for solar systems"""
            ...


    Industry: _Industry = _Industry()

    class _Insurance:
        def GetInsurancePrices(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetInsurancePricesOperation:
            """Return available insurance levels for all ship types"""
            ...


    Insurance: _Insurance = _Insurance()

    class _Killmails:
        def GetCharactersCharacterIdKillmailsRecent(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdKillmailsRecentOperation:
            """Return a list of a character's kills and losses going back 90 days"""
            ...

        def GetCorporationsCorporationIdKillmailsRecent(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdKillmailsRecentOperation:
            """Get a list of a corporation's kills and losses going back 90 days"""
            ...

        def GetKillmailsKillmailIdKillmailHash(self, killmail_hash: str, killmail_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetKillmailsKillmailIdKillmailHashOperation:
            """Return a single killmail from its ID and hash"""
            ...


    Killmails: _Killmails = _Killmails()

    class _Location:
        def GetCharactersCharacterIdLocation(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdLocationOperation:
            """Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable"""
            ...

        def GetCharactersCharacterIdOnline(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdOnlineOperation:
            """Checks if the character is currently online"""
            ...

        def GetCharactersCharacterIdShip(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdShipOperation:
            """Get the current ship type, name and id"""
            ...


    Location: _Location = _Location()

    class _Loyalty:
        def GetCharactersCharacterIdLoyaltyPoints(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdLoyaltyPointsOperation:
            """Return a list of loyalty points for all corporations the character has worked for"""
            ...

        def GetLoyaltyStoresCorporationIdOffers(self, corporation_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetLoyaltyStoresCorporationIdOffersOperation:
            """Return a list of offers from a specific corporation's loyalty store  This route expires daily at 11:05"""
            ...


    Loyalty: _Loyalty = _Loyalty()

    class _Mail:
        def DeleteCharactersCharacterIdMailLabelsLabelId(self, character_id: int, label_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteCharactersCharacterIdMailLabelsLabelIdOperation:
            """Delete a mail label"""
            ...

        def DeleteCharactersCharacterIdMailMailId(self, character_id: int, mail_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> DeleteCharactersCharacterIdMailMailIdOperation:
            """Delete a mail"""
            ...

        def GetCharactersCharacterIdMail(self, character_id: int, token: Token, labels: Optional[list[Any]] = ..., last_mail_id: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdMailOperation:
            """Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards"""
            ...

        def GetCharactersCharacterIdMailLabels(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdMailLabelsOperation:
            """Return a list of the users mail labels, unread counts for each label and a total unread count."""
            ...

        def GetCharactersCharacterIdMailLists(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdMailListsOperation:
            """Return all mailing lists that the character is subscribed to"""
            ...

        def GetCharactersCharacterIdMailMailId(self, character_id: int, mail_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdMailMailIdOperation:
            """Return the contents of an EVE mail"""
            ...

        def PostCharactersCharacterIdMail(self, body: InlineModel, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdMailOperation:
            """Create and send a new mail"""
            ...

        def PostCharactersCharacterIdMailLabels(self, body: InlineModel, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostCharactersCharacterIdMailLabelsOperation:
            """Create a mail label"""
            ...

        def PutCharactersCharacterIdMailMailId(self, body: InlineModel, character_id: int, mail_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PutCharactersCharacterIdMailMailIdOperation:
            """Update metadata about a mail"""
            ...


    Mail: _Mail = _Mail()

    class _Market:
        def GetCharactersCharacterIdOrders(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdOrdersOperation:
            """List open market orders placed by a character"""
            ...

        def GetCharactersCharacterIdOrdersHistory(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdOrdersHistoryOperation:
            """List cancelled and expired market orders placed by a character up to 90 days in the past."""
            ...

        def GetCorporationsCorporationIdOrders(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdOrdersOperation:
            """List open market orders placed on behalf of a corporation"""
            ...

        def GetCorporationsCorporationIdOrdersHistory(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdOrdersHistoryOperation:
            """List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past."""
            ...

        def GetMarketsGroups(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsGroupsOperation:
            """Get a list of item groups  This route expires daily at 11:05"""
            ...

        def GetMarketsGroupsMarketGroupId(self, market_group_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsGroupsMarketGroupIdOperation:
            """Get information on an item group  This route expires daily at 11:05"""
            ...

        def GetMarketsPrices(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsPricesOperation:
            """Return a list of prices"""
            ...

        def GetMarketsRegionIdHistory(self, region_id: int, type_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsRegionIdHistoryOperation:
            """Return a list of historical market statistics for the specified type in a region  This route expires daily at 11:05"""
            ...

        def GetMarketsRegionIdOrders(self, order_type: str, region_id: int, page: Optional[int] = ..., type_id: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsRegionIdOrdersOperation:
            """Return a list of orders in a region"""
            ...

        def GetMarketsRegionIdTypes(self, region_id: int, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsRegionIdTypesOperation:
            """Return a list of type IDs that have active orders in the region, for efficient market indexing."""
            ...

        def GetMarketsStructuresStructureId(self, structure_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMarketsStructuresStructureIdOperation:
            """Return all orders in a structure"""
            ...


    Market: _Market = _Market()

    class _Meta:
        def GetMetaChangelog(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMetaChangelogOperation:
            """Get the changelog of this API."""
            ...

        def GetMetaCompatibilityDates(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetMetaCompatibilityDatesOperation:
            """Get a list of compatibility dates."""
            ...


    Meta: _Meta = _Meta()

    class _Planetary_Interaction:
        def GetCharactersCharacterIdPlanets(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdPlanetsOperation:
            """Returns a list of all planetary colonies owned by a character."""
            ...

        def GetCharactersCharacterIdPlanetsPlanetId(self, character_id: int, planet_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdPlanetsPlanetIdOperation:
            """Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met."""
            ...

        def GetCorporationsCorporationIdCustomsOffices(self, corporation_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdCustomsOfficesOperation:
            """List customs offices owned by a corporation"""
            ...

        def GetUniverseSchematicsSchematicId(self, schematic_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseSchematicsSchematicIdOperation:
            """Get information on a planetary factory schematic"""
            ...


    Planetary_Interaction: _Planetary_Interaction = _Planetary_Interaction()

    class _Routes:
        def GetRouteOriginDestination(self, destination: int, origin: int, avoid: Optional[list[Any]] = ..., connections: Optional[list[Any]] = ..., flag: Optional[str] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetRouteOriginDestinationOperation:
            """Get the systems between origin and destination"""
            ...


    Routes: _Routes = _Routes()

    class _Search:
        def GetCharactersCharacterIdSearch(self, categories: list[Any], character_id: int, search: str, token: Token, strict: Optional[bool] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdSearchOperation:
            """Search for entities that match a given sub-string."""
            ...


    Search: _Search = _Search()

    class _Skills:
        def GetCharactersCharacterIdAttributes(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdAttributesOperation:
            """Return attributes of a character"""
            ...

        def GetCharactersCharacterIdSkillqueue(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdSkillqueueOperation:
            """List the configured skill queue for the given character"""
            ...

        def GetCharactersCharacterIdSkills(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdSkillsOperation:
            """List all trained skills for the given character"""
            ...


    Skills: _Skills = _Skills()

    class _Sovereignty:
        def GetSovereigntyCampaigns(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetSovereigntyCampaignsOperation:
            """Shows sovereignty data for campaigns."""
            ...

        def GetSovereigntyMap(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetSovereigntyMapOperation:
            """Shows sovereignty information for solar systems"""
            ...

        def GetSovereigntyStructures(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetSovereigntyStructuresOperation:
            """Shows sovereignty data for structures."""
            ...


    Sovereignty: _Sovereignty = _Sovereignty()

    class _Status:
        def GetStatus(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetStatusOperation:
            """EVE Server status"""
            ...


    Status: _Status = _Status()

    class _Universe:
        def GetUniverseAncestries(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseAncestriesOperation:
            """Get all character ancestries  This route expires daily at 11:05"""
            ...

        def GetUniverseAsteroidBeltsAsteroidBeltId(self, asteroid_belt_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseAsteroidBeltsAsteroidBeltIdOperation:
            """Get information on an asteroid belt  This route expires daily at 11:05"""
            ...

        def GetUniverseBloodlines(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseBloodlinesOperation:
            """Get a list of bloodlines  This route expires daily at 11:05"""
            ...

        def GetUniverseCategories(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseCategoriesOperation:
            """Get a list of item categories  This route expires daily at 11:05"""
            ...

        def GetUniverseCategoriesCategoryId(self, category_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseCategoriesCategoryIdOperation:
            """Get information of an item category  This route expires daily at 11:05"""
            ...

        def GetUniverseConstellations(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseConstellationsOperation:
            """Get a list of constellations  This route expires daily at 11:05"""
            ...

        def GetUniverseConstellationsConstellationId(self, constellation_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseConstellationsConstellationIdOperation:
            """Get information on a constellation  This route expires daily at 11:05"""
            ...

        def GetUniverseFactions(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseFactionsOperation:
            """Get a list of factions  This route expires daily at 11:05"""
            ...

        def GetUniverseGraphics(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseGraphicsOperation:
            """Get a list of graphics  This route expires daily at 11:05"""
            ...

        def GetUniverseGraphicsGraphicId(self, graphic_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseGraphicsGraphicIdOperation:
            """Get information on a graphic  This route expires daily at 11:05"""
            ...

        def GetUniverseGroups(self, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseGroupsOperation:
            """Get a list of item groups  This route expires daily at 11:05"""
            ...

        def GetUniverseGroupsGroupId(self, group_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseGroupsGroupIdOperation:
            """Get information on an item group  This route expires daily at 11:05"""
            ...

        def GetUniverseMoonsMoonId(self, moon_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseMoonsMoonIdOperation:
            """Get information on a moon  This route expires daily at 11:05"""
            ...

        def GetUniversePlanetsPlanetId(self, planet_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniversePlanetsPlanetIdOperation:
            """Get information on a planet  This route expires daily at 11:05"""
            ...

        def GetUniverseRaces(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseRacesOperation:
            """Get a list of character races  This route expires daily at 11:05"""
            ...

        def GetUniverseRegions(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseRegionsOperation:
            """Get a list of regions  This route expires daily at 11:05"""
            ...

        def GetUniverseRegionsRegionId(self, region_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseRegionsRegionIdOperation:
            """Get information on a region  This route expires daily at 11:05"""
            ...

        def GetUniverseStargatesStargateId(self, stargate_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseStargatesStargateIdOperation:
            """Get information on a stargate  This route expires daily at 11:05"""
            ...

        def GetUniverseStarsStarId(self, star_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseStarsStarIdOperation:
            """Get information on a star  This route expires daily at 11:05"""
            ...

        def GetUniverseStationsStationId(self, station_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseStationsStationIdOperation:
            """Get information on a station  This route expires daily at 11:05"""
            ...

        def GetUniverseStructures(self, filter: Optional[str] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseStructuresOperation:
            """List all public structures"""
            ...

        def GetUniverseStructuresStructureId(self, structure_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseStructuresStructureIdOperation:
            """Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs."""
            ...

        def GetUniverseSystemJumps(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseSystemJumpsOperation:
            """Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed"""
            ...

        def GetUniverseSystemKills(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseSystemKillsOperation:
            """Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed"""
            ...

        def GetUniverseSystems(self, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseSystemsOperation:
            """Get a list of solar systems  This route expires daily at 11:05"""
            ...

        def GetUniverseSystemsSystemId(self, system_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseSystemsSystemIdOperation:
            """Get information on a solar system.  This route expires daily at 11:05"""
            ...

        def GetUniverseTypes(self, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseTypesOperation:
            """Get a list of type ids  This route expires daily at 11:05"""
            ...

        def GetUniverseTypesTypeId(self, type_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetUniverseTypesTypeIdOperation:
            """Get information on a type  This route expires daily at 11:05"""
            ...

        def PostUniverseIds(self, body: List[str], Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUniverseIdsOperation:
            """Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours"""
            ...

        def PostUniverseNames(self, body: List[int], Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUniverseNamesOperation:
            """Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions"""
            ...


    Universe: _Universe = _Universe()

    class _User_Interface:
        def PostUiAutopilotWaypoint(self, add_to_beginning: bool, clear_other_waypoints: bool, destination_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUiAutopilotWaypointOperation:
            """Set a solar system as autopilot waypoint"""
            ...

        def PostUiOpenwindowContract(self, contract_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUiOpenwindowContractOperation:
            """Open the contract window inside the client"""
            ...

        def PostUiOpenwindowInformation(self, target_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUiOpenwindowInformationOperation:
            """Open the information window for a character, corporation or alliance inside the client"""
            ...

        def PostUiOpenwindowMarketdetails(self, type_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUiOpenwindowMarketdetailsOperation:
            """Open the market details window for a specific typeID inside the client"""
            ...

        def PostUiOpenwindowNewmail(self, body: InlineModel, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> PostUiOpenwindowNewmailOperation:
            """Open the New Mail window, according to settings from the request if applicable"""
            ...


    User_Interface: _User_Interface = _User_Interface()

    class _Wallet:
        def GetCharactersCharacterIdWallet(self, character_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdWalletOperation:
            """Returns a character's wallet balance"""
            ...

        def GetCharactersCharacterIdWalletJournal(self, character_id: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdWalletJournalOperation:
            """Retrieve the given character's wallet journal going 30 days back"""
            ...

        def GetCharactersCharacterIdWalletTransactions(self, character_id: int, token: Token, from_id: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCharactersCharacterIdWalletTransactionsOperation:
            """Get wallet transactions of a character"""
            ...

        def GetCorporationsCorporationIdWallets(self, corporation_id: int, token: Token, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdWalletsOperation:
            """Get a corporation's wallets"""
            ...

        def GetCorporationsCorporationIdWalletsDivisionJournal(self, corporation_id: int, division: int, token: Token, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdWalletsDivisionJournalOperation:
            """Retrieve the given corporation's wallet journal for the given division going 30 days back"""
            ...

        def GetCorporationsCorporationIdWalletsDivisionTransactions(self, corporation_id: int, division: int, token: Token, from_id: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetCorporationsCorporationIdWalletsDivisionTransactionsOperation:
            """Get wallet transactions of a corporation"""
            ...


    Wallet: _Wallet = _Wallet()

    class _Wars:
        def GetWars(self, max_war_id: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetWarsOperation:
            """Return a list of wars"""
            ...

        def GetWarsWarId(self, war_id: int, Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetWarsWarIdOperation:
            """Return details about a war"""
            ...

        def GetWarsWarIdKillmails(self, war_id: int, page: Optional[int] = ..., Accept_Language: Optional[str] = ..., If_None_Match: Optional[str] = ..., X_Compatibility_Date: Optional[str] = ..., X_Tenant: Optional[str] = ..., **kwargs: Any) -> GetWarsWarIdKillmailsOperation:
            """Return a list of kills related to a war"""
            ...


    Wars: _Wars = _Wars()

