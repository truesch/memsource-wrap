from typing import Any, Dict, List, Optional

from memsource.schemas.base import BaseSchema
from memsource.schemas.user import User
from memsource.schemas.domain import Domain
from memsource.schemas.client import Client
from memsource.schemas.reference import Reference




class Project(BaseSchema):
    uid: str
    internalId: int
    id: str
    name: str
    dateCreated: str
    domain: Optional[Domain]
    subDomain: Optional[Domain]
    owner: User
    sourceLang: str
    targetLangs: List[str]
    references: List[Optional[Reference]]
    mtSettingsPerLanguageList: List[Dict[str, Any]]
    userRole: str
    shared: bool
    progress: Dict[str, int]
    client: Optional[Client]
    costCenter: Optional[Dict[str, str]]
    businessUnit: Optional[Dict[str,str]]
    dateDue: str
    status: str
    purchaseOrder: Optional[str]
    isPublishedOnJobBoard: bool
    note: Optional[str]
    createdBy: User
    qualityAssuranceSettings: Dict[str, Any]
    workflowSteps: List[Dict[str, Any]]
    analyseSettings: Dict[str, Any]
    accessSettings: Dict[str, Any]
    financialSettings: Dict[str, Any]
    archived: bool
    vendorOwner: Optional[Dict[str, Any]]
    vendor: Optional[Dict[str, Any]]
