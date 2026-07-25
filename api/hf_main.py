

from transformers import pipeline

pipe = pipeline("text-generation", model="openbmb/MiniCPM5-1B")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)


# model downlod thay 2 gb na psi outpt mle.
