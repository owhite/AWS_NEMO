#!/usr/bin/env python3
"""Launch a NeMo training job on an AWS EC2 instance."""

import argparse
import logging
import sys

import boto3
from botocore.exceptions import ClientError
import yaml


def load_config(path: str) -> dict:
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"ERROR: Configuration file not found at '{path}'.", file=sys.stderr)
        print("Copy config/config.example.yaml to config/config.yaml and fill in your values.", file=sys.stderr)
        sys.exit(1)


def launch_instance(cfg: dict) -> str:
    """Launch an EC2 instance and return its instance ID."""
    ec2 = boto3.client("ec2", region_name=cfg["aws"]["region"])
    ec2_cfg = cfg["ec2"]
    nemo_cfg = cfg["nemo"]

    user_data = f"""#!/bin/bash
set -e
docker pull {nemo_cfg['docker_image']}
docker run --gpus all --rm \\
    -v /tmp/nemo:/workspace \\
    {nemo_cfg['docker_image']} \\
    python -m nemo.collections.nlp.models.language_modeling.megatron_gpt_model \\
    --config-path /workspace \\
    --config-name training.yaml
"""

    try:
        response = ec2.run_instances(
            ImageId=ec2_cfg["ami_id"],
            InstanceType=ec2_cfg["instance_type"],
            KeyName=ec2_cfg["key_name"],
            SecurityGroupIds=ec2_cfg["security_group_ids"],
            SubnetId=ec2_cfg["subnet_id"],
            IamInstanceProfile={"Name": ec2_cfg["iam_instance_profile"]},
            UserData=user_data,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [{"Key": "Name", "Value": "nemo-training"}],
                }
            ],
        )
    except ClientError as exc:
        error_code = exc.response["Error"]["Code"]
        error_msg = exc.response["Error"]["Message"]
        print(f"ERROR: AWS API call failed ({error_code}): {error_msg}", file=sys.stderr)
        sys.exit(1)

    instance_id = response["Instances"][0]["InstanceId"]
    return instance_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch a NeMo training job on AWS.")
    parser.add_argument(
        "--config",
        default="config/config.yaml",
        help="Path to the YAML configuration file (default: config/config.yaml)",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)

    log_level_str = cfg.get("logging", {}).get("level", "INFO").upper()
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    if log_level_str not in valid_levels:
        log_level_str = "INFO"
    logging.basicConfig(level=getattr(logging, log_level_str), format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Launching NeMo training instance...")
    instance_id = launch_instance(cfg)
    logger.info("Instance launched: %s", instance_id)
    print(instance_id)


if __name__ == "__main__":
    main()
