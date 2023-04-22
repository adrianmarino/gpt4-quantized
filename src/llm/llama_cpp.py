from llama_cpp import Llama
import logging


def last_words(text, size):
    count = 0
    words = []
    for word in [w for w in text.split(' ')][::-1]:
        words.append(word)
        count += len(word)
        if count >= size:
            break
    return ' '.join(words[::-1])


class LlamaCpp:
    def __init__(
        self,
        model_path,
        n_threads = 8,
        n_ctx     = 4096 
    ):
        self.model = Llama(
            model_path = model_path,
            n_threads  = n_threads,
            n_ctx      = n_ctx
        )

    
    def __call__(
        self, 
        prompt,
        temperature = 0.1, 
        max_len     = 4096,
        window_size = 3500,
        verbose     = True
    ):
        prompt = last_words(prompt.strip(), window_size)
        
        if verbose:
            logging.info(f'Promp({len(prompt)}): {prompt}')

        output = self.model(
            prompt      = prompt,
            max_tokens  = max_len - len(prompt),
            echo        = False,
            temperature = temperature
        )
        output = output['choices'][0]['text'].strip()

        if verbose:
            logging.info(f'Output({len(output)}):')

        return output