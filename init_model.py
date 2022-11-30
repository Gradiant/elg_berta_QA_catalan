from transformers import (
    AutoTokenizer,
    pipeline,
    AutoConfig,
    AutoModelForQuestionAnswering,
)


class Initializer:
    def __init__(self):

        tokenizer = AutoTokenizer.from_pretrained("projecte-aina/roberta-base-ca-v2-cased-qa")
        model = AutoModelForQuestionAnswering.from_pretrained(
            "projecte-aina/roberta-base-ca-v2-cased-qa"
        )
        config = AutoConfig.from_pretrained("projecte-aina/roberta-base-ca-v2-cased-qa")
        pipeline_obj = pipeline("question-answering", model=model, tokenizer=tokenizer)
