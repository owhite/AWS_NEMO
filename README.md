# AWS_NEMO

A scratch area for running [NVIDIA NeMo](https://github.com/NVIDIA/NeMo) workloads on AWS.

## Overview

This project provides scripts and configuration for launching and managing NeMo training and inference jobs on AWS infrastructure (EC2, ECS, SageMaker, etc.).

## Prerequisites

- Python 3.8+
- An AWS account with appropriate IAM permissions
- AWS CLI configured (`aws configure`)
- Docker (for containerized workloads)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/owhite/AWS_NEMO.git
   cd AWS_NEMO
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure AWS credentials:
   ```bash
   aws configure
   ```

5. Copy and edit the example configuration:
   ```bash
   cp config/config.example.yaml config/config.yaml
   # Edit config/config.yaml with your settings
   ```

## Project Structure

```
AWS_NEMO/
├── config/                  # Configuration files
│   └── config.example.yaml  # Example configuration
├── scripts/                 # Utility scripts
│   ├── launch_training.py   # Launch a NeMo training job on AWS
│   └── setup_environment.sh # Environment setup helper
├── requirements.txt         # Python dependencies
└── README.md
```

## Usage

### Launch a Training Job

```bash
python scripts/launch_training.py --config config/config.yaml
```

### Environment Setup

```bash
bash scripts/setup_environment.sh
```

## Contributing

Feel free to open issues or submit pull requests.

## License

See [LICENSE](LICENSE) for details.