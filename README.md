

## gpt4all-lora-quantized-ggml

Run locally a quantized GTP4 version with 4096 characters context.

![image](https://user-images.githubusercontent.com/962480/232647090-76b4e64d-f122-4ff4-b0ff-fc024622d619.png)

Also use a langchan agent to use external [tools](https://python.langchain.com/en/latest/modules/agents/tools.html) to help model to answer questions.

![image](https://user-images.githubusercontent.com/962480/233798938-cba77959-6703-45a5-aa9a-4f8a91f20a9f.png)

## Requirements

* [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [mamba](https://github.com/mamba-org/mamba)

## Setup

**Step 1**: Download model fro **[Here](https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized-ggml.bin)**.

**Step 2**: creatae ./models directory and move `gpt4all-lora-quantized-ggml.bin` model file to it. 


**Step 3**

```bash
$ conda env create -f environment.yml
```

**Step 4**

```bash
$ conda activate gpt
```

**Step 5** 

```bash
$ jupyter lab

Jupyter Notebook 6.1.4 is running at:
http://localhost:8888/?token=45efe99607fa6......
```

**Step 6**: Go to jupyter url and run [model.ipynb](https://github.com/adrianmarino/gpt4-quantized/blob/master/model.ipynb) or [agent.ipynb](https://github.com/adrianmarino/gpt4-quantized/blob/master/agent.ipynb)


## References

* [llama.cpp](https://github.com/ggerganov/llama.cpp)
* [LangChain](https://python.langchain.com/en/latest/index.html)
