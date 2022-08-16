import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class Stoichiometry(sdRDM.DataModel):

    """Stoichiometric information about the compound."""

    equivalents: Optional[float] = Field(
        description="Used equivalents in relation to the reference compound",
        default=None,
    )

    amount_of_substance: Optional[float] = Field(
        description="Amount of substance n in mmol",
        default=None,
    )

    mass: Optional[float] = Field(
        description="Used mass of the compound in g",
        default=None,
    )

    volume: Optional[float] = Field(
        description="Volume of the compound",
        default=None,
    )

    molar_mass: Optional[float] = Field(
        description="Molar mass of the compound in g per mol",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6cbc2fdcccadac154f6bbd995d386b893c4f7d2e"
    )
