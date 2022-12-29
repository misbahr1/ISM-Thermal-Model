#!/usr/bin/env python3

from typing import Dict, List, Tuple, Type
import numpy as np

from .nodes import HeatStorageNode, LinkType


class ThermalModel():

    def __init__(self, simulation_duration: int, timestep: float,
                 model_description: List[
                     Tuple[str, Dict, List[
                         Tuple[str, Dict, List[
                             Tuple[str, Tuple[str, str], List[Type[LinkType]], Dict]
                         ]]
                     ]]
                 ]):
        """
        The main ThermalModel incorporating all sub-components.

        Parameters:

            - simulation_duration: int

                The number of seconds the simulation should run for. This does not correspond to real-life seconds.

            - timestep: float

                The number of seconds between each time step. Since the simulation is discrete, we are modelling it using "time steps".

            - model_description

                This one allows for a very high level and transparent definition of the model. The creation of all the nodes, links, and matrices is taken care of through the data passed in here. It is important to understand the structure of the data requested here.

                The data should look as follows (consider this an example demystifying the type hint):

                    [
                        ('Battery', {<HSN parameters>}, [
                            ('top', {<IFN parameters>}, [
                                ('BoardComputerBottom', ('BoardComputer', 'bottom'), [<Link types>], {<link parameters>}),
                                ('ADCTop', ('ADC', 'top'), [<Link types>], {<link parameters>}),
                                ...
                            ])
                            ('bottom', {<IFN parameters>}, [
                                ('Link1-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ('Link2-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ...
                            ])
                            ('front', {<IFN parameters>}, [
                                ('Link1-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ('Link2-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ...
                            ])
                            ...
                        ])
                        ('BoardComputer', {<HSN parameters>}, [
                            ('top', {<IFN parameters>}, [
                                ('Link1-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ('Link2-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ...
                            ])
                            ('bottom', {<IFN parameters>}, [
                                ('Link1-name', (<HSN-name>, <IFN-name>), [<Link types>], {<link parameters>}),
                                ...
                            ])
                            ...
                        ])
                        ('ADC', {<HSN parameters>}, [
                            ('top', {<IFN parameters>}, [
                                ...
                            ])
                            ...
                        ])
                    ]

        Methods:

            - simulate()

        """

        self.duration: int = simulation_duration  # seconds
        self.timestep: float = timestep  # seconds

        self.heatStorageNodes: Dict[str, HeatStorageNode] = {}

        # Arrays are populated later once the number of nodes are known
        self.IFNHeatExchanges: np.ndarray = None
        self.HSNHeatExchanges: np.ndarray = None
        self.LinkHeatExchanges: np.ndarray = None

        self.HSNTemperatureDifferences: np.ndarray = None
        self.HSNTemperatures: np.ndarray = None

    def _createLabelIndex(self) -> dict:
        return {}

    def _createMatrices(self):
        pass

    def _addHeatStorageNodes(self, nodes: List[Tuple[str, Dict]]):
        # TODO: Store key-value (name, HSN) pair in dictionary
        pass

    def _addInterfaceNodes(self, nameHSN: str, nodes: List[Tuple[str, Dict]]):
        # TODO: Use HSN to create IFN
        pass

    def _addInterfaceLinks(self, nameHSN: str, nameIFN: str,
                           links: List[Tuple[str, Dict]]):
        # TODO: Use IFN from HSN to create links
        # TODO: Track missing links in opposite direction (maintain a list)
        # TODO: If link in opposite direction is given, remove it from the list of missing links
        # TODO: following steps in new method? i.e. 'generateMissingLinks()'
        # TODO: Appropriately generate missing links (in opposite direction)
        # TODO: How to make opposite link return negative heat exchange of specified link
        pass

    def simulate(self):
        pass
