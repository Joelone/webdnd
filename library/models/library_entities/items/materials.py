from django.db import models

from library.config import STND_CHAR_LIMIT, STND_ID_CHAR_LIMIT, STND_DECIMAL_PLACES
from library.models.abstract import AbstractLibraryEntity

class Material(AbstractLibraryEntity):
    price = models.PositiveIntegerField(blank=False, null=False)
    hardness = models.PositiveIntegerField(
        default=10,
        blank=True,
        null=False)
    density = models.DecimalField(
        max_length=6,
        decimal_place=STND_DECIMAL_PLACES,
        default=7.874,
        blank=True,
        null=False)
    hp_per_thickness = models.DecimalField(
        max_length=6,
        decimal_place=STND_DECIMAL_PLACES,
        default=30,
        blank=True,
        null=False)

    # TODO: add bonuses
    # For weapons and Armor use *Info.proficiency_group to filter
    """
    main_bonuses = 
    melee_thrown_bonuses = 
    ranged_bonuses = 
    armor_bonuses = 
    ammunition_bonuses = 
    """