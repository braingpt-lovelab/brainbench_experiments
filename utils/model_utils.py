import transformers
import torch


def load_model_and_tokenizer(model_fpath, tokenizer_only=False):
    if tokenizer_only:
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            model_fpath,
        )
        return tokenizer
    
    load_in_8bit = False
    torch_dtype = torch.float16

    # Load pretrained model
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_fpath,
        load_in_8bit=load_in_8bit,
        device_map='auto',
        trust_remote_code=True,
        torch_dtype=torch_dtype
    )

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_fpath,
    )

    return model, tokenizer
