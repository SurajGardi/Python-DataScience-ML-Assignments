# Marvellous Infosystems — Deep Learning Assignment 73
## Transformers and Self-Attention

---

## Q1. Why were Transformers introduced? What limitations of RNN and LSTM are solved by Transformers?

**Transformers** were introduced to overcome important limitations of traditional sequence models such as **RNNs and LSTMs**, especially their sequential processing nature and difficulty in handling long-range dependencies.

### Limitations of RNN and LSTM

- **Sequential processing:** RNNs process one token at a time, making parallel processing difficult.
- **Long-term dependencies:** RNNs can struggle to retain information from distant words.
- **Vanishing/Exploding gradients:** Training recurrent networks can suffer from gradient-related problems.
- **Slow training:** Because tokens are processed sequentially, training can be slower.
- **Limited scalability:** Sequential computation makes it difficult to efficiently scale RNN/LSTM models to large datasets and models.

### How Transformers solve these problems

Transformers use **Self-Attention**, which allows relationships between tokens to be calculated more directly and supports much more **parallel processing**.

```text id="k4s0k8"
RNN
Token 1 → Token 2 → Token 3 → Token 4
          Sequential Processing

Transformer
Token 1 ─┐
Token 2 ─┤
Token 3 ─┼→ Self-Attention → Context
Token 4 ─┘
          Parallel Processing
```

**Key point:** Transformers replaced sequential recurrence with **attention-based processing**, making them more suitable for large-scale sequence modelling.

---

## Q2. Explain the complete Transformer architecture.

A Transformer consists mainly of **Input Embeddings, Positional Encoding, Encoder, Decoder, Attention mechanisms and Feed Forward Networks**.

### Overall Architecture

```text id="1f8hqp"
Input Tokens
     ↓
Input Embeddings
     ↓
Positional Encoding
     ↓
┌───────────────────┐
│     ENCODER       │
│                   │
│ Self-Attention    │
│       ↓           │
│ Add & Normalize   │
│       ↓           │
│ Feed Forward      │
│       ↓           │
│ Add & Normalize   │
└───────────────────┘
     ↓
Encoded Representation
     ↓
┌───────────────────┐
│     DECODER       │
│                   │
│ Masked Attention  │
│       ↓           │
│ Add & Normalize   │
│       ↓           │
│ Encoder-Decoder   │
│ Attention         │
│       ↓           │
│ Feed Forward      │
│       ↓           │
│ Add & Normalize   │
└───────────────────┘
     ↓
Linear Layer
     ↓
Softmax
     ↓
Output
```

### 1. Input Embeddings

Input tokens are converted into numerical vectors called **embeddings**.

```text id="ytm8n1"
Token → Embedding Vector
```

The embedding represents the semantic information of the token.

---

### 2. Positional Encoding

Transformers do not process tokens sequentially like RNNs. Therefore, they need additional information about the **position/order of tokens**.

Positional encoding is added to the embeddings to provide this positional information.

```text id="c0m1kz"
Token Embedding + Positional Encoding
              ↓
        Transformer Input
```

---

### 3. Encoder

The Encoder processes the input sequence and creates a **context-aware representation**.

Its main components include:

- Multi-Head Self-Attention
- Add & Normalize
- Feed Forward Network
- Add & Normalize

---

### 4. Decoder

The Decoder generates the output sequence.

It contains:

- Masked Self-Attention
- Encoder-Decoder Attention
- Feed Forward Network
- Add & Normalize

---

### 5. Attention Mechanism

Attention determines **which tokens are important to each other** while understanding the context.

---

### 6. Feed Forward Network

The Feed Forward Network processes the output of the attention layer independently for each position and applies a non-linear transformation.

### Key idea

```text id="ez5r72"
Embedding
    +
Position
    ↓
Attention
    ↓
Context
    ↓
Feed Forward
    ↓
Processed Representation
```

---

## Q3. Explain Self-Attention Mechanism in detail. Why is it considered the heart of Transformer architecture?

**Self-Attention** allows each token in a sequence to look at other tokens in the same sequence and determine their importance when creating its representation.

For example:

```text id="rxw3po"
"The animal didn't cross the street because it was too wide."
```

To understand what **"it"** refers to, the model needs to examine the relationship between different words.

Self-attention allows the model to determine these relationships.

### Basic process

```text id="a4j8rh"
Input Tokens
     ↓
Create Q, K, V
     ↓
Calculate Attention Scores
     ↓
Scale Scores
     ↓
Apply Softmax
     ↓
Weighted Sum of V
     ↓
Context-Aware Representation
```

### Why is it the heart of Transformer?

Self-Attention:

- Captures relationships between tokens.
- Helps understand context.
- Allows distant tokens to interact directly.
- Produces context-aware representations.
- Enables parallel processing of sequence information.

Therefore, Self-Attention is one of the **central mechanisms responsible for the power of Transformers**.

---

## Q4. Explain Q = XWq, K = XWk, V = XWv. What are Query, Key and Value? Why are they required?

In Self-Attention, the input representation `X` is transformed into three matrices:

```text id="l5y9qf"
Q = XWq
K = XWk
V = XWv
```

Where:

- `X` → Input embeddings
- `Wq` → Learnable Query weight matrix
- `Wk` → Learnable Key weight matrix
- `Wv` → Learnable Value weight matrix

### Query (Q)

A **Query** represents what the current token is looking for.

It helps determine:

> "What information do I need?"

### Key (K)

A **Key** represents what each token can offer or what information it contains.

It helps determine:

> "What information do I contain?"

### Value (V)

A **Value** contains the actual information that will be used when a token receives attention.

It represents:

> "What information should be passed forward?"

### Simple analogy

Think of a search system:

```text id="6zj6hj"
Query  → What am I looking for?
Key    → What does each item represent?
Value  → What information should I retrieve?
```

### Why are Q, K and V required?

They separate the attention process into:

```text id="9u3h2m"
Query → What am I looking for?
Key   → What matches my query?
Value → What information should I take?
```

This allows the Transformer to calculate **which information is relevant and how much of it should contribute to the output**.

---

## Q5. Explain step-by-step calculation of attention scores.

The attention mechanism calculates how strongly each token should attend to other tokens.

The basic attention formula is:

```text id="5g3x2p"
Attention(Q, K, V)
=
Softmax(QKᵀ / √dk)V
```

### Step 1: Calculate Q × Kᵀ

First, Query is multiplied by the transpose of Key:

```text id="7b0s3e"
Q × Kᵀ
```

This produces **attention scores**.

A higher score means that the corresponding tokens have a stronger relationship.

---

### Step 2: Scale by √dk

The scores are divided by the square root of the Key dimension:

```text id="j8kz0w"
QKᵀ
──────
 √dk
```

where `dk` is the dimension of the Key vectors.

Scaling prevents the values from becoming too large and helps maintain stable Softmax values.

---

### Step 3: Apply Softmax

Softmax converts the scaled scores into **attention weights/probabilities**.

```text id="y7k9k5"
Scaled Scores
     ↓
   Softmax
     ↓
Attention Weights
```

The weights indicate how much importance should be given to each token.

---

### Step 4: Weighted Sum with V

Finally, the attention weights are multiplied with the Value matrix:

```text id="m6qv8d"
Attention Weights × V
```

This produces the final **context-aware representation**.

### Complete flow

```text id="5eqf5b"
Q × Kᵀ
   ↓
Scale by √dk
   ↓
Softmax
   ↓
Attention Weights
   ↓
× V
   ↓
Attention Output
```

### Final formula

```text id="g9x9zt"
Attention(Q,K,V)
= Softmax(QKᵀ / √dk)V
```

---

## Q6. Why do Transformers support parallel processing better than RNN?

RNNs process sequence elements **one after another**.

```text id="4a6l7x"
Token 1 → Token 2 → Token 3 → Token 4
```

Token 2 depends on the processing of Token 1, and so on.

Transformers use **Self-Attention**, allowing relationships between tokens to be calculated without processing the entire sequence strictly step-by-step.

```text id="8u4j4q"
Token 1 ─┐
Token 2 ─┤
Token 3 ─┼→ Self-Attention
Token 4 ─┘
```

### Advantages

- Processes sequence information more efficiently.
- Allows greater parallel computation during training.
- Makes better use of modern GPU hardware.
- Scales more effectively to large models and datasets.

### Comparison

| RNN | Transformer |
|---|---|
| Sequential processing | Parallel-friendly processing |
| Token-by-token dependency | Attention-based relationships |
| Difficult to scale efficiently | More scalable |
| Long-range dependencies can be difficult | Direct attention between tokens |

---

## Q7. Explain Positional Encoding. Why is it required in Transformers?

**Positional Encoding** provides information about the **position/order of tokens** in a sequence.

Unlike RNNs, Transformers do not naturally process tokens one after another. Therefore, without positional information:

```text id="r0g7be"
"I love Python"
```

and

```text id="0s0h3a"
"Python love I"
```

could be represented without sufficient information about their order.

### Working

Positional information is added to the token embeddings:

```text id="0m4x4c"
Token Embedding
       +
Positional Encoding
       ↓
Transformer Input
```

### Why is it required?

- Provides token position information.
- Helps the model understand word order.
- Helps distinguish sequences with the same words but different ordering.
- Allows attention to use both **meaning and position**.

### Key point

```text id="3d5f6r"
Embedding → What is the token?
Position   → Where is the token?
```

---

## Q8. What is Multi-Head Attention? Why do we use multiple heads?

**Multi-Head Attention** is a mechanism where multiple attention operations, called **heads**, work in parallel.

Each head can learn different types of relationships between tokens.

### Structure

```text id="h7x2xw"
Input
  ↓
┌────────┬────────┬────────┐
│ Head 1 │ Head 2 │ Head 3 │
└────────┴────────┴────────┘
     ↓       ↓       ↓
Different Attention Patterns
          ↓
       Concatenate
          ↓
      Final Output
```

### Why multiple heads?

Different heads can focus on different relationships, such as:

- Grammatical relationships
- Word-to-word relationships
- Semantic relationships
- Long-distance dependencies

### Example

For:

```text id="f6z2u8"
"The boy opened the door because he was late."
```

One attention head may focus on grammatical relationships while another may focus on the relationship between **"he"** and **"boy"**.

### Key point

```text id="z3q9c2"
Single Head
→ One attention perspective

Multiple Heads
→ Multiple attention perspectives
```

This gives the Transformer a richer understanding of the input.

---

## Q9. Explain Add & Normalize layer. What problem does it solve?

**Add & Normalize** consists of two important operations:

1. **Residual/Add connection**
2. **Layer Normalization**

### Add / Residual Connection

The original input of a sub-layer is added to its output.

```text id="e2v9wq"
Input ───────────────┐
                     ↓
                  Add (+)
                     ↑
Input → Sub-layer ───┘
```

This creates a residual connection.

### Layer Normalization

After the addition, **Layer Normalization** is applied to stabilize the activations.

```text id="y3m6o1"
Input
  ↓
Sub-layer
  ↓
Add
  ↓
Layer Normalization
  ↓
Output
```

### What problem does it solve?

- Helps information flow through deeper networks.
- Makes training more stable.
- Helps prevent problems caused by changing activation distributions.
- Makes it easier to train deeper Transformer architectures.

### Simple representation

```text id="w9j2h4"
Sub-layer Output + Original Input
              ↓
       Layer Normalization
              ↓
            Output
```

---

## Q10. Explain Encoder and Decoder in Transformers.

The **Encoder** and **Decoder** are the two major components of the original Transformer architecture.

### Encoder

The Encoder processes the input sequence and creates a **context-aware representation**.

Its main components are:

```text id="8k9w7m"
Input
 ↓
Multi-Head Self-Attention
 ↓
Add & Normalize
 ↓
Feed Forward Network
 ↓
Add & Normalize
 ↓
Encoder Output
```

### Decoder

The Decoder uses the encoded representation and generates the output sequence.

Its main components are:

```text id="8f4v8p"
Output Tokens
      ↓
Masked Self-Attention
      ↓
Add & Normalize
      ↓
Encoder-Decoder Attention
      ↓
Add & Normalize
      ↓
Feed Forward Network
      ↓
Add & Normalize
      ↓
Output
```

### Encoder vs Decoder

| Feature | Encoder | Decoder |
|---|---|---|
| Main purpose | Understand input | Generate output |
| Attention | Self-Attention | Masked Self-Attention + Encoder-Decoder Attention |
| Main output | Context-aware representation | Generated sequence |
| Example | BERT uses encoder architecture | GPT uses decoder architecture |

### Overall Transformer flow

```text id="y5x4qz"
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

**Key point:** The Encoder is primarily responsible for **understanding/representing the input**, while the Decoder is responsible for **generating the output**.