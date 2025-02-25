"""``JSONDataSet`` saves data to a JSON file using an underlying
filesystem (e.g.: local, S3, GCS). It uses native json to handle the JSON file.
The ``JSONDataSet`` is part of Kedro Experiment Tracking. The dataset is versioned by default.
"""
from typing import NoReturn

from kedro.extras.datasets.json import JSONDataSet as JDS
from kedro.io.core import DataSetError

# NOTE: kedro.extras.datasets will be removed in Kedro 0.19.0.
# Any contribution to datasets should be made in kedro-datasets
# in kedro-plugins (https://github.com/kedro-org/kedro-plugins)


class JSONDataSet(JDS):
    """``JSONDataSet`` saves data to a JSON file using an underlying
    filesystem (e.g.: local, S3, GCS). It uses native json to handle the JSON file.
    The ``JSONDataSet`` is part of Kedro Experiment Tracking.
    The dataset is write-only and it is versioned by default.

        Example:
        ::

        >>> from kedro.extras.datasets.tracking import JSONDataSet
        >>>
        >>> data = {'col1': 1, 'col2': 0.23, 'col3': 0.002}
        >>>
        >>> # data_set = JSONDataSet(filepath="gcs://bucket/test.json")
        >>> data_set = JSONDataSet(filepath="test.json")
        >>> data_set.save(data)

    """

    versioned = True

    def _load(self) -> NoReturn:
        raise DataSetError(f"Loading not supported for '{self.__class__.__name__}'")
