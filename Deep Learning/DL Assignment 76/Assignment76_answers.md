# Marvellous Infosystems — Deep Learning Assignment 76
## Transformers and Self-Attention 

---

## Q1. Why were Transformers introduced? What limitations of RNN and LSTM are solved by Transformers?

**Transformers** were introduced to overcome important limitations of **RNNs and LSTMs** in processing sequential data.

### Limitations of RNN and LSTM

- **Sequential processing:** RNNs process tokens one after another, which makes parallel processing difficult.
- **Long-term dependencies:** It can be difficult for recurrent models to maintain information from distant parts of a sequence.
- **Vanishing/Exploding gradients:** Recurrent networks can face gradient-related problems during training.
- **Slow training:** Sequential computation makes training less efficient.
- **Limited scalability:** Sequential processing makes it harder to efficiently scale recurrent models to very large datasets and models.

### How Transformers solve these problems

Transformers use **Self-Attention** to directly model relationships between tokens and support much more parallel processing.

```text id="0a2b1c"
RNN / LSTM

Token 1 → Token 2 → Token 3 → Token 4
          Sequential Processing


Transformer

Token 1 ─┐
Token 2 ─┤
Token 3 ─┼──→ Self-Attention
Token 4 ─┘
        Parallel-Friendly Processing
```

**Key point:** Transformers replace sequential recurrence with **attention-based processing**, making them more suitable for large-scale sequence modelling.

---

## Q2. Explain the complete Transformer architecture.

A Transformer consists of **Input Embeddings, Positional Encoding, Encoder, Decoder, Attention Mechanism and Feed Forward Networks**.

### Overall Architecture

```text id="2c3d4e"
Input Tokens
     ↓
Input Embeddings
     ↓
Positional Encoding
     ↓
┌─────────────────────┐
│       ENCODER       │
│                     │
│ Multi-Head          │
│ Self-Attention      │
│        ↓            │
│ Add & Normalize     │
│        ↓            │
│ Feed Forward        │
│        ↓            │
│ Add & Normalize     │
└─────────────────────┘
     ↓
Encoded Representation
     ↓
┌─────────────────────┐
│       DECODER       │
│                     │
│ Masked Self-        │
│ Attention           │
│        ↓            │
│ Add & Normalize     │
│        ↓            │
│ Encoder-Decoder     │
│ Attention           │
│        ↓            │
│ Add & Normalize     │
│        ↓            │
│ Feed Forward        │
│        ↓            │
│ Add & Normalize     │
└─────────────────────┘
     ↓
Linear Layer
     ↓
Softmax
     ↓
Output
```

### 1. Input Embeddings

Input tokens are converted into numerical vectors called **embeddings**.

```text id="5e6f7g"
Token → Embedding Vector
```

These vectors represent the information associated with the input tokens.

### 2. Positional Encoding

Transformers do not naturally process tokens sequentially. Therefore, **positional encoding** provides information about the position of each token.

```text id="8h9i0j"
Token Embedding
      +
Positional Encoding
      ↓
Transformer Input
```

### 3. Encoder

The Encoder processes the input sequence and creates a **context-aware representation**.

Its major components are:

- Multi-Head Self-Attention
- Add & Normalize
- Feed Forward Network
- Add & Normalize

### 4. Decoder

The Decoder generates the output sequence.

It contains:

- Masked Self-Attention
- Encoder-Decoder Attention
- Feed Forward Network
- Add & Normalize

### 5. Attention Mechanism

Attention determines **which tokens are important to each other** while understanding the context.

### 6. Feed Forward Network

The Feed Forward Network further processes the output of the attention layer and applies a non-linear transformation.

### Overall idea

```text id="1k2l3m"
Input
  ↓
Embeddings + Position
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

**Self-Attention** allows each token in a sequence to consider other tokens in the same sequence and determine their importance when creating its representation.

For example:

```text id="4n5o6p"
"The animal didn't cross the street because it was too wide."
```

To understand what **"it"** refers to, the model needs to examine relationships between different words.

Self-Attention helps the model determine these relationships.

### Working of Self-Attention

```text id="7q8r9s"
Input
  ↓
Create Q, K, V
  ↓
Calculate Attention Scores
  ↓
Scale Scores
  ↓
Softmax
  ↓
Weighted Sum with V
  ↓
Context-Aware Representation
```

### Why is it considered the heart of Transformer architecture?

Self-Attention:

- Captures relationships between tokens.
- Helps understand context.
- Allows distant tokens to interact directly.
- Creates context-aware representations.
- Enables parallel-friendly processing.

Therefore, Self-Attention is one of the **central mechanisms of Transformer architecture**.

---

## Q4. Explain Q = XWq, K = XWk, V = XWv. What are Query, Key and Value? Why are they required?

In Self-Attention, the input representation `X` is transformed into three matrices:

```text id="0t1u2v"
Q = XWq
K = XWk
V = XWv
```

Where:

- `X` → Input representation
- `Wq` → Learnable Query weight matrix
- `Wk` → Learnable Key weight matrix
- `Wv` → Learnable Value weight matrix

### Query (Q)

A **Query** represents what the current token is looking for.

```text id="3w4x5y"
"What information am I looking for?"
```

### Key (K)

A **Key** represents the information or characteristics that each token can offer for matching.

```text id="6z7a8b"
"What information do I contain?"
```

### Value (V)

A **Value** contains the actual information that is passed to the output when attention is given to a token.

```text id="9c0d1e"
"What information should be retrieved?"
```

### Simple analogy

```text id="2f3g4h"
Query  → What am I looking for?
Key    → What does this token represent?
Value  → What information should I take?
```

### Why are Q, K and V required?

They separate the attention process into three roles:

```text id="5i6j7k"
Query → Search
Key   → Match
Value → Retrieve Information
```

This allows the model to determine **which tokens are relevant and how much information should be taken from them**.

---

## Q5. Explain step-by-step calculation of attention scores.

The attention mechanism can be represented by:

```text id="8l9m0n"
Attention(Q,K,V)
=
Softmax(QKᵀ / √dk)V
```

### Step 1: Calculate Q × Kᵀ

First, the Query matrix is multiplied by the transpose of the Key matrix.

```text id="1p2q3r"
Q × Kᵀ
```

This produces the **attention scores**.

A higher score indicates a stronger relationship between the corresponding tokens.

---

### Step 2: Scale by √dk

The attention scores are divided by the square root of the Key dimension:

```text id="4s5t6u"
QKᵀ
──────
 √dk
```

Here, `dk` represents the dimension of the Key vectors.

Scaling helps prevent excessively large values and makes the subsequent Softmax operation more stable.

---

### Step 3: Apply Softmax

Softmax converts the scaled scores into **attention weights**.

```text id="7v8w9x"
Scaled Scores
     ↓
   Softmax
     ↓
Attention Weights
```

These weights represent the relative importance of different tokens.

---

### Step 4: Weighted Sum with V

The attention weights are multiplied with the Value matrix:

```text id="0y1z2a"
Attention Weights × V
```

This produces the final **attention output** or context-aware representation.

### Complete process

```text id="3b4c5d"
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

### Final Formula

```text id="6e7f8g"
Attention(Q,K,V)
= Softmax(QKᵀ / √dk)V
```

---

## Q6. Why do Transformers support parallel processing better than RNN?

RNNs process sequence elements **one after another**.

```text id="9h0i1j"
Token 1 → Token 2 → Token 3 → Token 4
```

The processing of later tokens depends on earlier steps.

Transformers use **Self-Attention**, which allows relationships between tokens to be calculated without processing the sequence strictly one token at a time.

```text id="2k3l4m"
Token 1 ─┐
Token 2 ─┤
Token 3 ─┼──→ Self-Attention
Token 4 ─┘
```

### Advantages

- More parallel computation during training.
- Better utilization of GPUs and other parallel hardware.
- Faster processing for large datasets.
- Better scalability for large models.

### Comparison

| RNN | Transformer |
|---|---|
| Sequential processing | Parallel-friendly processing |
| Token-by-token dependency | Attention-based relationships |
| Difficult to parallelize across sequence positions | More parallelizable |
| Less scalable for very large models | Highly scalable |

**Key point:** Transformers can process relationships between many tokens simultaneously, whereas RNNs inherently depend on sequential processing.

---

## Q7. Explain Positional Encoding. Why is it required in Transformers?

**Positional Encoding** provides information about the **position and order of tokens** in a sequence.

Transformers do not inherently process tokens one after another like RNNs. Therefore, they need additional information to understand token order.

### Example

Consider:

```text id="5n6o7p"
"I love Python"
```

and

```text id="8q9r0s"
"Python love I"
```

The words are similar, but their order is different.

Positional Encoding helps the Transformer distinguish their positions.

### Working

```text id="1t2u3v"
Token Embedding
       +
Positional Encoding
       ↓
Transformer Input
```

### Why is it required?

- Provides token position information.
- Helps the model understand word order.
- Helps distinguish sequences with different token arrangements.
- Adds positional information to attention-based processing.

### Simple idea

```text id="4w5x6y"
Embedding → What is the token?
Position   → Where is the token?
```

---

## Q8. What is Multi-Head Attention? Why do we use multiple heads?

**Multi-Head Attention** uses multiple attention mechanisms, called **heads**, that operate in parallel.

Each head can learn different relationships between tokens.

### Structure

```text id="7z8a9b"
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
       Output
```

### Why multiple heads?

Different heads can focus on different relationships, such as:

- Grammatical relationships
- Semantic relationships
- Word-to-word relationships
- Long-distance dependencies

### Example

For:

```text id="0c1d2e"
"The boy opened the door because he was late."
```

One attention head may focus on grammatical relationships, while another may learn the relationship between **"he"** and **"boy"**.

### Key point

```text id="3f4g5h"
Single Head
→ One attention perspective

Multiple Heads
→ Multiple attention perspectives
```

Using multiple heads gives the model a richer representation of relationships within the input.

---

## Q9. Explain Add & Normalize layer. What problem does it solve?

**Add & Normalize** consists of:

1. **Residual/Add Connection**
2. **Layer Normalization**

### 1. Add / Residual Connection

The input to a sub-layer is added to the output of that sub-layer.

```text id="6i7j8k"
Input ─────────────────┐
                       ↓
                    Add (+)
                       ↑
Input → Sub-layer ─────┘
```

This is called a **residual connection**.

### 2. Layer Normalization

After the addition, **Layer Normalization** is applied to stabilize the representation.

```text id="9l0m1n"
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

Add & Normalize helps:

- Improve information flow through deep networks.
- Make training more stable.
- Support the training of deeper Transformer architectures.
- Reduce problems caused by unstable activation distributions.

### Simple representation

```text id="2o3p4q"
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

### Encoder structure

```text id="5r6s7t"
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

### Decoder structure

```text id="8u9v0w"
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
| Main purpose | Understand/process input | Generate output |
| Attention | Self-Attention | Masked Self-Attention + Encoder-Decoder Attention |
| Main output | Context-aware representation | Generated sequence |
| Example | BERT uses Encoder-only architecture | GPT uses Decoder-only architecture |

### Overall Transformer flow

```text id="1x2y3z"
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

**Key point:** The Encoder primarily **understands and represents the input**, while the Decoder primarily **uses that information to generate the output**.