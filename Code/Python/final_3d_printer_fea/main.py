import sys
from typing import List

from fea import analyzers, feeders, runners
import keras


def main(args: List[str]):
    analyzer = analyzers.Analyzer(
        img_feeder=feeders.ManualFeederTerminal(img_root_dir="test"),
        img_model=keras.models.load_model(
            'test/New_specimen_with_prosity_and_long_gap_v6.hdf5', compile=False),
        fea_runner=runners.DummyRunner(pkl_export_dir="test/pkl_outputs"),
        n_layers=10)
    analyzer.analyze()


if __name__ == "__main__":
    main(sys.argv[1:])
