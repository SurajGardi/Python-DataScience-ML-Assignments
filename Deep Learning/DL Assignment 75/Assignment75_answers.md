# Assignment 75

## 1. Explain Encoder-Only architecture.
### Examples:
- BERT
- Sentiment analysis

### Why is it good for understanding tasks?

An **Encoder-Only architecture** uses only the Encoder part of the Transformer. It is mainly designed to **understand and represent input text** rather than generate new text.

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

### Common Applications

- Sentiment Analysis
- Text Classification
- Question Answering
- Named Entity Recognition (NER)
- Text Understanding

### Key Point

```text
Encoder-Only
      ↓
Understand the input
      ↓
Produce contextual representation
```

---

## 2. Explain Decoder-Only architecture.
### Examples:
- GPT
- ChatGPT
- Llama

### Why is it suitable for text generation?

A **Decoder-Only architecture** uses only the Decoder part of the Transformer and is mainly designed for **text generation**.

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

### Key Point

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

## 3. Explain Encoder-Decoder architecture.
### Examples:
- Translation systems
- T5

### Why are both encoder and decoder required?

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

### Key Point

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

## 4. Differentiate between Encoder-Only, Decoder-Only and Encoder-Decoder.

| Feature | Encoder-Only | Decoder-Only | Encoder-Decoder |
|---|---|---|---|
| Architecture | Only Encoder | Only Decoder | Encoder + Decoder |
| Main Purpose | Understand input | Generate text | Transform input into output |
| Attention | Self-Attention | Masked Self-Attention | Encoder Self-Attention + Decoder Attention |
| Processing | Understands complete input context | Generates token-by-token | Encoder understands, Decoder generates |
| Output | Representation / prediction | Generated sequence | Generated sequence |
| Examples | BERT | GPT, ChatGPT, Llama | T5, Translation |
| Main Use | Classification, understanding | Text/code generation, chatbots | Translation, sequence-to-sequence tasks |

### Simple Comparison

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

### In Simple Words

```text
Encoder-Only    → "Understand this."

Decoder-Only    → "Generate something."

Encoder-Decoder → "Understand this, then generate something based on it."
```

---

## 5. Which Transformer architecture is used in ChatGPT and why?

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

### Main Characteristics

- Uses **Decoder-style Transformer blocks**.
- Uses **Masked Self-Attention**.
- Generates text autoregressively.
- Can generate responses based on the provided context.
- Well suited for conversational text generation.

### Simple Flow

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

### Key Point

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

---

# Additional Important Questions

## 6. Why is BERT considered a bidirectional Transformer model?
### How does bidirectional context help BERT understand text?

**BERT** is considered bidirectional because it learns contextual information by considering the words **before and after a token** within the input sequence.

### Example

```text
"The bank is near the river."
```

To understand the meaning of **"bank"**, the model can use context from words around it, such as **"river"**.

```text
Previous Context ← Bank → Following Context
```

This helps BERT understand the meaning of a word based on its surrounding context.

### Why is bidirectional context useful?

- Provides context from both directions.
- Helps understand relationships between words.
- Improves contextual representation.
- Makes BERT effective for language-understanding tasks.

### Key Point

```text
BERT
 ↓
Context from both directions
 ↓
Better contextual understanding
 ↓
Understanding Tasks
```

---

## 7. What is Masked Self-Attention in Decoder-Only Transformers?
### Why can a decoder not look at future tokens during text generation?

**Masked Self-Attention** prevents a Decoder from attending to tokens that occur **after the current token**.

This is necessary because during text generation, the model should only use information that would actually be available at that point.

### Example

Suppose the sequence is:

```text
"I love learning Python"
```

When predicting:

```text
"I love learning"
```

the model should not use:

```text
"Python"
```

because it is the future token.

### Masking

```text
Current Token
     ↓
Can attend to:
✓ Previous tokens
✓ Current token

Cannot attend to:
✗ Future tokens
```

### Why is masking required?

Without masking, the model could see the correct future answer during training, which would not represent the real text-generation process.

### Simple Flow

```text
Previous Tokens
      ↓
Masked Self-Attention
      ↓
Next Token Prediction
```

### Key Point

**Masked Self-Attention maintains the autoregressive nature of Decoder-Only Transformers by preventing access to future tokens.**

---

## 8. Explain Autoregressive Text Generation in Decoder-Only Transformers.
### How does the model generate text one token at a time?

**Autoregressive text generation** means that the model generates each new token using the tokens that have already been generated.

### Example

```text
Input:
"Machine Learning"

        ↓
Predict:
"is"

        ↓
Predict:
"a"

        ↓
Predict:
"field"

        ↓
Predict:
"of"

        ↓
...
```

Each newly generated token becomes part of the input for the next prediction.

### Working

```text
Existing Tokens
      ↓
Transformer
      ↓
Predict Next Token
      ↓
Add New Token
      ↓
Transformer
      ↓
Predict Next Token
      ↓
Repeat
```

### Example

```text
"Python is"
     ↓
"Python is powerful"
     ↓
"Python is powerful and"
     ↓
"Python is powerful and easy"
```

### Key Point

```text
Previous Tokens
      ↓
Next Token Prediction
      ↓
New Token
      ↓
Previous + New Token
      ↓
Next Token Prediction
```

This process continues until the model reaches an appropriate stopping condition.

---

## 9. What is Encoder-Decoder Attention?
### How does the Decoder use information produced by the Encoder?

**Encoder-Decoder Attention**, also called **Cross-Attention**, allows the Decoder to use information generated by the Encoder.

It is especially important in **Encoder-Decoder architectures** such as translation systems.

### Working

```text
Input
  ↓
Encoder
  ↓
Encoded Representation
  ↓
Encoder-Decoder Attention
  ↑
Decoder
  ↓
Output
```

The Decoder uses the Encoder's representation to determine which parts of the input are relevant while generating each output token.

### Example: Translation

```text
English Sentence
      ↓
   Encoder
      ↓
English Context
      ↓
Cross-Attention
      ↓
   Decoder
      ↓
Translated Sentence
```

### Why is it required?

It allows the Decoder to:

- Access information from the input.
- Focus on relevant parts of the encoded input.
- Generate output based on the input context.
- Perform sequence-to-sequence tasks such as translation.

### Key Point

```text
Encoder → Understand Input
              ↓
        Cross-Attention
              ↓
Decoder → Generate Output
```

---

## 10. Compare BERT, GPT, and T5 based on their Transformer architecture, working, and primary applications.

| Feature | BERT | GPT | T5 |
|---|---|---|---|
| Architecture | Encoder-Only | Decoder-Only | Encoder-Decoder |
| Main Purpose | Language Understanding | Text Generation | Text-to-Text |
| Context | Bidirectional | Previous-token context | Encoder understands input, Decoder generates output |
| Generation | Not primarily designed for free-form generation | Autoregressive generation | Autoregressive output generation |
| Main Attention | Self-Attention | Masked Self-Attention | Encoder Self-Attention + Decoder Attention |
| Common Applications | Classification, NER, Sentiment Analysis | Chatbots, Text Generation, Code Generation | Translation, Summarization, Question Answering |
| Basic Idea | Understand | Generate | Understand → Generate |

### Simple Comparison

```text
BERT
 ↓
Encoder-Only
 ↓
Understand Text


GPT
 ↓
Decoder-Only
 ↓
Generate Text


T5
 ↓
Encoder-Decoder
 ↓
Understand Input → Generate Output
```

### Key Point

```text
BERT → Best suited for understanding tasks
GPT  → Best suited for autoregressive generation
T5   → Best suited for sequence-to-sequence text transformation
```

---

## Summary

The three major Transformer architectures can be understood as:

```text
┌───────────────────────────────────────────┐
│              Transformer                  │
└───────────────────────────────────────────┘
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
 Encoder-Only   Decoder-Only  Encoder-Decoder
       ↓            ↓            ↓
    BERT          GPT           T5
       ↓            ↓            ↓
 Understand       Generate    Understand
    Text            Text          ↓
                              Generate
                                Output
```

This completes Assignment 75 while keeping the **first five questions consistent with Assignment 74** and using the additional five questions to cover the important concepts that were not directly addressed there.