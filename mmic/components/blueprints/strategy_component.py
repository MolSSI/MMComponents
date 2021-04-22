from ..base.base_component import ProgramHarness
from typing import Dict, List, Set, Optional, Any, Tuple
import importlib
import abc

__all__ = ["StrategyComponent"]


class StrategyComponent(ProgramHarness):
    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        if hasattr(inputs, "component"):
            if inputs.component:
                if not importlib.util.find_spec(inputs.component):
                    raise ModuleNotFoundError(f"{inputs.component} cannot be imported")
                else:
                    comp_mod = importlib.import_module(inputs.component)
                    return True, comp_mod._mainComponent.compute(inputs)

        if not len(self.installed_comps):
            raise ModuleNotFoundError(
                "No supported component is installed. Solve by installing any of the following components:\n"
                + f"{self.supported_comps}"
            )

        comp_mod = importlib.import_module(comp)
        return True, comp_mod._mainComponent.compute(inputs)

    @staticmethod
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
        raise NotImplementedError

    @property
    def installed_comps(self) -> List[str]:
        """Returns module spec if it exists.
        Returns
        -------
        List[str]
            Component names that are installed.
        """
        if self.supported_comps is None:
            raise NotImplementedError
            (
                "No components are available. Solve by registering one via register_comps.add(your_component)."
            )
        return [spec for spec in self.supported_comps if importlib.util.find_spec(spec)]

    @abc.abstractmethod
    def get_version(self) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def supported_comps(self) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        raise NotImplementedError