"""Pipeline module for local TFX pipeline."""

import os
from typing import Text

from absl import logging
from tfx.orchestration import metadata, pipeline
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner

PIPELINE_NAME = "jericho_luthfi_ihFK-pipeline"

# pipeline inputs
DATA_ROOT = "data"
TRANSFORM_MODULE_FILE = "modules/transform.py"
TUNER_MODULE_FILE = "modules/tuner.py"
TRAINER_MODULE_FILE = "modules/trainer.py"

# pipeline outputs
OUTPUT_BASE = "output"
serving_model_dir = os.path.join(OUTPUT_BASE, 'serving_model')
pipeline_root = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
metadata_path = os.path.join(pipeline_root, "metadata.sqlite")


def init_local_pipeline(
    components, pipeline_root: Text
) -> pipeline.Pipeline:
    """Initiate local TFX pipeline.

    Args:
        components (dict): TFX components.
        pipeline_root (Text): Path to pipeline directory.

    Returns:
        pipeline.Pipeline: Pipeline orchestration.
    """
    logging.info(f"Pipeline root set to: {pipeline_root}")
    beam_args = [
        "--direct_running_mode=multi_processing",
        "--direct_num_workers=0"
    ]

    return pipeline.Pipeline(
        pipeline_name=PIPELINE_NAME,
        pipeline_root=pipeline_root,
        components=components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            metadata_path
        ),
        eam_pipeline_args=beam_args
    )


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)

    from modules.components import init_components

    components = init_components(
        DATA_ROOT,
        transform_module=TRANSFORM_MODULE_FILE,
        tuner_module=TUNER_MODULE_FILE,
        training_module=TRAINER_MODULE_FILE,
        training_steps=5000,
        eval_steps=1000,
        serving_model_dir=serving_model_dir,
    )

    pipeline = init_local_pipeline(components, pipeline_root)
    BeamDagRunner().run(pipeline=pipeline)