import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional
from .filmpreparation import FilmPreparation


class Processing(sdRDM.DataModel):

    """Lorem ipsum"""

    field: Optional[str] = Field(
        description="...",
        default=None,
    )

    film_preparation: Optional[FilmPreparation] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5d48c0ab8715b2bafdb4436122baebae81b78633"
    )
