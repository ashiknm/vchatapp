from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")

model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum")