

## gpt4all-lora-quantized-ggml

Run locally a quantized GTP4 version.

![image](https://user-images.githubusercontent.com/962480/232647090-76b4e64d-f122-4ff4-b0ff-fc024622d619.png)

## Requirements

* [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [mamba](https://github.com/mamba-org/mamba)

## Setup

**Step 1**: [Download model](https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized-ggml.bin).

**Step 2**

```bash
$ conda env create -f environment.yml
```

**Step 3**

```bash
$ conda activate gpt
```

**Step 4** 

```bash
$ jupyter lab

Jupyter Notebook 6.1.4 is running at:
http://localhost:8888/?token=45efe99607fa6......```
```

**Step 5**: Go to jupyter url and run [notebook.ipynb](https://github.com/adrianmarino/gpt4-quantized/blob/master/notebook.ipynb)

## References

* [llama.cpp](https://github.com/ggerganov/llama.cpp)
