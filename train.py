from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch

# 1️⃣ Setup
MODEL_NAME = "distilbert-base-uncased"
LABELS = ["Title", "H1", "H2", "H3", "Body"]

# 2️⃣ Load CSV dataset
dataset = load_dataset("csv", data_files="training_data.csv")

# ✅ 2a: Filter out rows with empty labels
dataset = dataset.filter(lambda x: x["label"] is not None and x["label"].strip() != "")

# 3️⃣ Encode text labels to integers
def encode_labels(example):
    example["label"] = LABELS.index(example["label"])
    return example

dataset = dataset.map(encode_labels)

# 4️⃣ Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# 5️⃣ Tokenize text
def tokenize_function(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=64)

tokenized = dataset.map(tokenize_function, batched=True)

# 6️⃣ Create model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=len(LABELS))

# 7️⃣ Training config
training_args = TrainingArguments(
    output_dir="./model_output",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    learning_rate=2e-5,
    evaluation_strategy="no",
    save_strategy="epoch",
)

# 8️⃣ Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    tokenizer=tokenizer,
)

# 9️⃣ Train!
trainer.train()

# 🔟 Save model + tokenizer
model.save_pretrained("my_heading_model")
tokenizer.save_pretrained("my_heading_model")

print("✅ Model training complete! Saved to ./my_heading_model")
