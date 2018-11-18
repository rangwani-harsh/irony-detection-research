import json
import shutil
import sys

from allennlp.commands import main

config_file = "experiments/alternatinglstmmultitask.json"

# Use overrides to train on CPU.
overrides = json.dumps({"trainer": {"cuda_device": -1}})

serialization_dir = "~/tmp/irony_debug"

# Training will fail if the serialization directory already
# has stuff in it. If you are running the same training loop
# over and over again for debugging purposes, it will.
# Hence we wipe it out in advance.
# BE VERY CAREFUL NOT TO DO THIS FOR ACTUAL TRAINING!
shutil.rmtree(serialization_dir, ignore_errors=True)

# Assemble the command into sys.argv
sys.argv = [
    "python",  # command name, not used by main
    "train",
    config_file,
    "-s", serialization_dir,
    "--include-package", "irony_model",
    "-o", overrides,
]
# archive_path = "~/tmp/medels/irony/model.tar.gz"
# predictor_name = "ironic-predictor"
# package_name = "irony_model"
# field_name = "tweet"

# sys.argv = [
#     "python",
#     "-m",
#     "allenlp.service.server_simple",
#     "--archive-path",
#     archive_path,
#     "--predictor",
#     predictor_name,
#     "--include-package",
#     package_name,
#     "--title",
#     predictor_name,
#     "--field-name",
#     field_name
# ]

main()
