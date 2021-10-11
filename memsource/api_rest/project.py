from typing import Any, Dict, List, Optional
from memsource import constants, api_rest
from memsource.schemas import Project as ProjectSchema
from memsource.schemas import TranslationMemory as TMSchema
from memsource.schemas import TermBase as TBSchema


class Project(api_rest.BaseApi):
    # Document: https://cloud.memsource.com/web/docs/api#tag/Project

    def create(
        self,
        name: str,
        source_lang: str,
        target_langs: List[str],
        client: int=None,
        domain: int=None,
    ) -> ProjectSchema:
        return ProjectSchema(**self._post("v1/projects", {
            "name": name,
            "sourceLang": source_lang,
            "targetLangs": target_langs,
            "client": client,
            "domain": domain,
        }))

    def get(
        self,
        uid: str
    ) -> ProjectSchema:
        return ProjectSchema(**self._get(f"v1/projects/{uid}"))

    def list(self, **query) -> List[ProjectSchema]:
        projects = self._get("v1/projects", query)
        return [ProjectSchema(**project) for project in projects.get("content", [])]

    def get_trans_memories(self, project_id: int) -> List[TMSchema]:
        translation_memories = self._get(f"v1/projects/{project_id}/transMemories")
        return [
            TMSchema(**tm)
            for tm in translation_memories.get("transMemories", [])
        ]

    def set_trans_memories(
        self,
        project_id: int,
        translation_memories: List[Dict[str, Any]],
        target_lang: str=None,
        workflow_step: Optional[Dict[str, str]]=None,
    ) -> None:
        """You can set translation memory to a project.

        :param project_id: set translation memory to this id of project
        :param translation_memories: Read/Write to these translation memories
        :param target_lang: set translation memories only for the specific project target language
        """
        params = {"transMemories": translation_memories}

        if target_lang is not None:
            params["targetLang"] = target_lang

        if workflow_step is not None:
            params["workflowStep"] = workflow_step

        self._put("v2/projects/{}/transMemories".format(project_id), params)
        return None

    def set_status(self, project_id: int, status: constants.ProjectStatus) -> None:
        """Update project status

        ProjectStatus: New, Emailed, Assigned, Declined_By_Linguist,
                       Completed_By_Linguist, Completed, Cancelled

        :param project_id: id of project you want to update.
        :param status: status of project to update. Acceptable type is ProjectStatus constant.
        """

        self._post("v1/projects/{}/setStatus".format(project_id), {
            "status": status.value.upper()
        })
        return None

    def get_term_bases(self, project_id: int) -> List[TBSchema]:
        """Returns the list of term bases belonging to a project.
        :param project_id: ID of the project containing the term bases
        """
        term_bases = self._get("v1/projects/{}/termBases".format(project_id))
        return [TBSchema(**term_base) for term_base in term_bases.get("termBases", [])]
