import abc
from typing import Any, Dict, List, Optional, Tuple
import sys
sys.path.insert(0, '..')
from models.output import DockingOutput, Affinity
from config import TaskConfig

from base_component.base_component import ProgramHarness

class DockingAffinityComponent(ProgramHarness, abc.ABC):
    
    @classmethod
    @abc.abstractmethod
    def compute(cls, input_data: "DockingOutput", config: "TaskConfig" = None) -> "Affinity":
        pass
        
    @staticmethod
    @abc.abstractmethod
    def found(raise_error: bool = False) -> bool:
        """
        Checks if the program can be found.
        Parameters
        ----------
        raise_error : bool, optional
            If True, raises an error if the program cannot be found.
        Returns
        -------
        bool
            Returns True if the program was found, False otherwise.
        """
    
    ## Computers

    def build_input(
        self, input_model: "DockingOutput", config: "TaskConfig" = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        raise ValueError("build_input is not implemented for {}.", self.__class__)

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        raise ValueError("execute is not implemented for {}.", self.__class__)

    def parse_output(self, outfiles: Dict[str, str], input_model: "DockingOutput") -> "Affinity":
        raise ValueError("parse_output is not implemented for {}.", self.__class__)
