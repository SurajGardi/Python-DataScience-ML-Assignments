# Marvellous Infosystems — Deep Learning Assignment 74
## Transformer Architectures — Encoder-Only, Decoder-Only & Encoder-Decoder

---

## Q1. Explain Encoder-Only architecture.

An **Encoder-Only architecture** uses only the **Encoder part of the Transformer**. It is mainly designed to **understand and represent input text** rather than generate new text.

### Architecture

```text
Input Text
    ↓
Tokenization
    ↓
Input Embeddings
    ↓
Positional Encoding
    ↓
Encoder
    ↓
Self-Attention
    ↓
Feed Forward Network
    ↓
Context-Aware Representation
    ↓
Task-Specific Output
```

### Example: BERT

**BERT (Bidirectional Encoder Representations from Transformers)** is an example of an Encoder-Only Transformer.

BERT considers the context of words from **both directions**.

```text
Previous Context ← Word → Following Context
```

### Example: Sentiment Analysis

For:

```text
"The movie was excellent."
```

BERT processes the sentence and creates a contextual representation that can be used to determine:

```text
Positive
```

### Why is it good for understanding tasks?

Encoder-Only models are suitable for understanding because they:

- Analyze the complete input context.
- Capture relationships between words.
- Produce rich contextual representations.
- Are suitable for classification and language-understanding tasks.

### Common applications

- Sentiment Analysis
- Text Classification
- Question Answering
- Named Entity Recognition (NER)
- Text Understanding

### Key point

```text
Encoder-Only
      ↓
Understand the input
      ↓
Produce contextual representation
```

---

## Q2. Explain Decoder-Only architecture.

A **Decoder-Only architecture** uses only the **Decoder part of the Transformer** and is mainly designed for **text generation**.

It uses **Masked Self-Attention**, which prevents the model from looking at future tokens while predicting the current token.

### Architecture

```text
Input Tokens
     ↓
Embeddings
     ↓
Positional Information
     ↓
Masked Self-Attention
     ↓
Feed Forward Network
     ↓
Next Token Prediction
     ↓
Generated Output
```

### Examples

- **GPT**
- **ChatGPT**
- **Llama**

### Example

Suppose the input is:

```text
"Python is"
```

The model predicts the next token:

```text
"programming"
```

Then it uses the newly generated token to predict the next one.

```text
Python is
    ↓
programming
    ↓
language
    ↓
...
```

This process continues until the required response is generated.

### Why is it suitable for text generation?

Decoder-Only models are designed for **autoregressive generation**, where the model predicts the next token based on the tokens that came before it.

They are therefore suitable for:

- Chatbots
- Text Generation
- Code Generation
- Story Generation
- Question Answering
- Conversational AI

### Key point

```text
Decoder-Only
      ↓
Predict next token
      ↓
Generate next token
      ↓
Predict next token
      ↓
Complete text
```

---

## Q3. Explain Encoder-Decoder architecture.

An **Encoder-Decoder architecture** contains both an Encoder and a Decoder.

The **Encoder understands the input**, while the **Decoder uses that information to generate the required output**.

### Architecture

```text
Input Sequence
      ↓
   Encoder
      ↓
Contextual Representation
      ↓
   Decoder
      ↓
Output Sequence
```

### Encoder

The Encoder:

- Processes the input sequence.
- Uses Self-Attention.
- Creates contextual representations.
- Passes this information to the Decoder.

### Decoder

The Decoder:

- Receives information from the Encoder.
- Uses Masked Self-Attention.
- Uses Encoder-Decoder Attention.
- Generates the output sequence.

### Example: Translation

Consider:

```text
English:
"I love Python."
```

The Encoder understands the English sentence.

```text
English Sentence
       ↓
    Encoder
       ↓
Meaning / Context
       ↓
    Decoder
       ↓
Translated Sentence
```

The Decoder can then generate the corresponding sentence in another language.

### Examples

- Machine Translation Systems
- **T5 (Text-to-Text Transfer Transformer)**

### Why are both required?

Translation and similar sequence-to-sequence tasks require two different operations:

```text
Encoder → Understand the input
Decoder → Generate the output
```

Therefore, both components work together.

### Key point

```text
Encoder
   ↓
Understand Input
   ↓
Decoder
   ↓
Generate Output
```

---

## Q4. Differentiate between Encoder-Only, Decoder-Only and Encoder-Decoder.

| Feature | Encoder-Only | Decoder-Only | Encoder-Decoder |
|---|---|---|---|
| Architecture | Only Encoder | Only Decoder | Encoder + Decoder |
| Main purpose | Understand input | Generate text | Transform input into output |
| Attention | Self-Attention | Masked Self-Attention | Encoder Self-Attention + Decoder Attention |
| Processing | Understands complete input context | Generates token-by-token | Encoder understands, Decoder generates |
| Output | Representation / prediction | Generated sequence | Generated sequence |
| Example | BERT | GPT, ChatGPT, Llama | T5, Translation |
| Main use | Classification, understanding | Text/code generation, chatbots | Translation, sequence-to-sequence tasks |

### Simple comparison

```text
Encoder-Only
Input → Understand
        ↓
      Output

Decoder-Only
Input → Generate → Generate → Generate
                  ↓
                Output

Encoder-Decoder
Input → Encoder → Context → Decoder → Output
```

### In simple words

```text
Encoder-Only    → "Understand this."

Decoder-Only    → "Generate something."

Encoder-Decoder → "Understand this, then generate something based on it."
```

---

## Q5. Which Transformer architecture is used in ChatGPT and why?

**ChatGPT uses a Decoder-Only Transformer architecture.**

It is based on the **GPT (Generative Pre-trained Transformer)** family.

### Why Decoder-Only?

ChatGPT needs to generate responses **token by token**.

For example:

```text
User:
"What is Python?"

        ↓

Model predicts:
"What"

        ↓

" is"

        ↓

" Python"

        ↓

"?"
```

The model uses the previously available tokens to predict the next token.

### Main characteristics

- Uses **Decoder-style Transformer blocks**.
- Uses **Masked Self-Attention**.
- Generates text autoregressively.
- Can generate responses based on the provided context.
- Well suited for conversational text generation.

### Simple flow

```text
User Prompt
     ↓
Tokenization
     ↓
Embeddings
     ↓
Decoder-Only Transformer
     ↓
Next Token Prediction
     ↓
Generated Response
```

### Key point

```text
ChatGPT
   ↓
Decoder-Only Transformer
   ↓
Next-Token Prediction
   ↓
Text Generation
   ↓
Conversation
```