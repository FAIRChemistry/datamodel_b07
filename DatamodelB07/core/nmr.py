import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class NMR(sdRDM.DataModel):

    """..."""

    nmr_1h: Optional[str] = Field(
        description="...",
        default=None,
    )

    m_peo: float = Field(
        ...,
        description="Polyethylene oxide",
    )

    zeropointfive_n_po: Optional[float] = Field(
        description="Fraction propylene oxide",
        default=None,
    )

    m_n_in_kg_per_mole: Optional[float] = Field(
        description="Number average molar mass",
        default=None,
    )

    hlb: Optional[str] = Field(
        description="Hydrophilic to lipophilic balance",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6cbc2fdcccadac154f6bbd995d386b893c4f7d2e"
    )
