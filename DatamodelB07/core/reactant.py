import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional
from .chemicalcompound import ChemicalCompound


class Reactant(sdRDM.DataModel):

    """Chemical compound that is involved in the chemical reaction, either as the product, educt, catalyst or cocatalyst."""

    product: Optional[str] = Field(
        description="...",
        default=None,
    )

    educt: Optional[str] = Field(
        description="...",
        default=None,
    )

    catalyst: Optional[str] = Field(
        description="...",
        default=None,
    )

    cocatalyst: Optional[str] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5d48c0ab8715b2bafdb4436122baebae81b78633"
    )
