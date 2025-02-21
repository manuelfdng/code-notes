# Machine Learning & Statistics Anki Deck Prompt

## Overview
Generate a JSON file containing 200 high-quality Anki flashcards covering Machine Learning (ML) and Statistics concepts.

## Card Structure
```json
[
  {
    "Front": "<Definition or explanation of a term without explicitly stating it>",
    "Back": "<Correct term>"
  }
]
```

## Requirements

### Card Format
- **Front**: Clear, concise definition or explanation of an ML or Statistics term, without mentioning the term itself
- **Back**: The exact term associated with the definition

### Content Coverage
Equal distribution across:

**Machine Learning Topics**:
- Supervised learning
- Unsupervised learning
- Deep learning
- Feature engineering
- Model evaluation
- Bias-variance tradeoff
- Optimization

**Statistics Topics**:
- Probability distributions
- Hypothesis testing
- Regression
- Confidence intervals
- Statistical significance
- Bayesian inference

### Core Focus Areas
- Classification
- Clustering
- Neural networks
- Regularization
- Probability theory
- Data distributions
- Hypothesis testing
- Model evaluation

### Technical Requirements
- JSON must be properly structured for direct Anki import
- All 200 cards must be unique with no duplicates

## Example Entry
```json
{
  "Front": "A type of machine learning algorithm where the model learns to make predictions by being given labeled training data consisting of input-output pairs",
  "Back": "Supervised Learning"
}
```