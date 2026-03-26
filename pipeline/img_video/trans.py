from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

REPO = "davidkim205/iris-7b"
model = AutoModelForCausalLM.from_pretrained(REPO, torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(REPO)


def generate(prompt):
    encoding = tokenizer(
        prompt,
        return_tensors="pt",
        return_token_type_ids=False,
    ).to("cuda")
    gen_tokens = model.generate(
        **encoding,
        max_new_tokens=2048,
        temperature=1.0,
        num_beams=5,
    )
    prompt_end_size = encoding.input_ids.shape[1]
    return tokenizer.decode(gen_tokens[0, prompt_end_size:])


def translate_ko2en(text):
    prompt = f"[INST] 다음 문장을 영어로 번역하세요.{text} [/INST]"
    return generate(prompt)


def translate_en2ko(text):
    prompt = f"[INST] 다음 문장을 한글로 번역하세요.{text} [/INST]"
    return generate(prompt)
