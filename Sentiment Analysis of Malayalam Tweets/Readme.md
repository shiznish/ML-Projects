# Sentiment Analysis of Malayalam Tweets

## Project Description

This project explores sentiment analysis for tweets written in Malayalam, one of the Dravidian languages spoken predominantly in Kerala, India. Sentiment analysis is a key task in natural language processing (NLP) to determine the sentiment polarity (positive, negative, or neutral) expressed in a text. By leveraging two advanced models, **LSTM** and **BERT**, this project aimed to analyze and classify sentiments in Malayalam tweets effectively.

## Dataset

The dataset for this project comprises Malayalam tweets collected from social media platforms. It was preprocessed to clean noise, normalize text, and prepare it for training and evaluation.

## Models Used

### 1. **LSTM (Long Short-Term Memory)**
LSTM networks are a type of recurrent neural network (RNN) capable of learning long-term dependencies in sequential data. It was implemented to capture the sentiment nuances in Malayalam tweets.

### 2. **BERT (Bidirectional Encoder Representations from Transformers)**
BERT, a state-of-the-art transformer-based NLP model, was fine-tuned for sentiment classification. Its bidirectional attention mechanism allowed the model to grasp the context and semantics of the tweets effectively.

## Results

### LSTM Model
- **Training Accuracy**: 99.685%
- **Validation Accuracy**: 95%
- **Test Accuracy**: 93%

### BERT Model
- **Training Accuracy**: 99.84%
- **Validation Accuracy**: 97.5%
- **Test Accuracy**: 96%

BERT outperformed LSTM in all metrics, demonstrating its superiority in handling complex linguistic structures and context.

## Conclusion

Concluding our sentiment analysis journey:
- Both LSTM and BERT models effectively captured sentiment polarity in Malayalam tweets.
- BERT emerged as the more accurate model, setting a benchmark in the domain of sentiment analysis for Malayalam text.

These results not only validate our efforts but also highlight the potential of deep learning models for low-resource languages like Malayalam.

