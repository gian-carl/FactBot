# FactBot – Voice‑Enabled Fact‑Checking Chatbot  
## Detailed Project Documentation

---

## 1. What is FactBot?

**FactBot** is a smart voice‑controlled assistant that helps you quickly check facts. You simply speak a question, and FactBot searches the internet, gathers information from trusted sources, evaluates how reliable each source is, and then tells you the answer in a clear, spoken voice. It can even detect when different sources give conflicting information and will let you know.

FactBot is designed to be:
- **Fast** – it searches multiple sources at the same time.
- **Accurate** – it ranks sources by trustworthiness.
- **Easy to use** – no typing, just speak.
- **Always learning** – it remembers previous conversations so you can ask follow‑up questions.

---

## 2. Key Features Explained

###  Voice Interaction
- **Speak naturally** – FactBot listens to you through your computer’s microphone.
- **“Hey FactBot” wake word** – You can start a question by saying “Hey FactBot” (optional). This makes it feel like a real voice assistant.
- **Spoken answers** – FactBot reads the answer aloud using a natural‑sounding voice.

###  Multi‑Source Fact‑Checking
FactBot doesn’t rely on just one website. It gathers information from:
- **Wikipedia** – a large, well‑known online encyclopedia.
- **News API** – recent news articles from various sources.
- **A fallback** – a simple response if the other sources fail.

By combining multiple sources, FactBot gives you a more complete picture.

###  Parallel Processing
Instead of waiting for one source to finish before starting another, FactBot asks all sources **at the same time**. This means you get your answer much faster.

###  Credibility Scoring
Not all sources are equally trustworthy. FactBot gives each source a score:
- **Wikipedia** – 0.9 (very reliable)
- **News API** – 0.7 (generally reliable, but may contain opinions)
- **Fallback** – 0.5 (used only when nothing else works)

When showing the answer, FactBot prioritises the most credible information.

###  Conflict Detection
If one source says something completely different from another, FactBot notices. It will tell you there’s a conflict and present the differing views so you can decide for yourself.

###  Smart Summarisation
Sometimes the information from sources is long and complicated. FactBot uses advanced language technology to **summarise** everything into a short, easy‑to‑understand answer – just like a friend would explain it.

### 🗣️ Streaming Voice Output
FactBot starts speaking as soon as it has the first part of the answer ready. It doesn’t wait for all sources to finish. This makes the conversation feel more natural and responsive.

###  Context Memory
FactBot remembers the last few questions you asked and the answers it gave. So if you ask “What about its history?” after a previous question, FactBot knows you’re still talking about the same topic.

###  Logging System
Every interaction is saved in a file. This helps developers improve the bot and can be useful for auditing or debugging.

###  Offline Fallback / Caching
If you ask the same question again, FactBot remembers the answer from last time and doesn’t need to search the internet again. If the internet goes down, it can still answer questions that have been asked before.

---

## 3. How FactBot Works (Step by Step)

Here’s what happens when you speak to FactBot:

1. **You speak** – Say something like “Hey FactBot, what is artificial intelligence?” (or just “What is artificial intelligence?” after waking it up).
2. **FactBot listens** – It converts your speech into text using a speech‑to‑text engine.
3. **It checks its memory** – If you’ve asked this question before, FactBot uses the saved answer immediately.
4. **It asks all sources** – If it’s a new question, FactBot simultaneously sends your question to Wikipedia, the News API, and the fallback source.
5. **It scores the results** – Each answer gets a credibility score.
6. **It checks for conflicts** – It compares the answers to see if they contradict each other.
7. **It summarises** – It combines the best information into a short, clear summary.
8. **It speaks the answer** – The summary is spoken out loud, sentence by sentence, so you can hear it as it’s being prepared.
9. **It saves everything** – The question, answer, sources used, and any conflict are saved to a log file.
10. **It remembers** – The conversation is stored in memory so you can ask follow‑up questions.

---

## 4. Technology Behind FactBot

FactBot is built with **Python**, a popular programming language. Here’s the tech stack in simple terms:

| What it does | How it’s done |
|--------------|---------------|
| **Listening to you** | Uses a library called `speech_recognition` to capture audio and turn it into text. |
| **Speaking back** | Uses `pyttsx3` to convert text to speech – works even without internet. |
| **Fetching from Wikipedia** | Uses the `wikipedia` library to get summaries. |
| **Fetching news** | Uses `requests` to talk to the News API. |
| **Doing multiple tasks at once** | Uses `ThreadPoolExecutor` to run tasks in parallel. |
| **Summarising intelligently** | Uses a **transformer model** (like BART) from Hugging Face to create human‑like summaries. |
| **Detecting conflicts** | Uses **sentence embeddings** to measure how similar two texts are. If they are very different, it flags a conflict. |
| **Remembering conversations** | Stores the last few exchanges in a list. |
| **Logging and caching** | Saves data in simple JSON files on your computer. |

---

## 5. The “Hey FactBot” Wake Word

FactBot can be set to listen continuously for the phrase **“Hey FactBot”**. Once it hears that, it starts recording your question. This makes it feel like a hands‑free assistant – you don’t need to press any buttons.

If you don’t want to use the wake word, FactBot can also be started by pressing a button (if a graphical interface is added) or simply by saying “Hey FactBot” as the first word of your question.

---

## 6. What Makes FactBot Special?

- **It’s a full voice experience** – You talk, it talks back.
- **It’s fast** – By searching all sources at once, you get answers quicker.
- **It’s smart** – It doesn’t just repeat what it finds; it picks the most trustworthy information and presents it clearly.
- **It’s honest** – If sources disagree, it tells you, so you can make up your own mind.
- **It’s private** – All processing (except the speech‑to‑text service) can be done locally, and logs are stored on your own computer.

---

## 7. How to Use FactBot (Plain Instructions)

1. **Install the software** – Follow the installation steps (a developer will set it up for you, or you can follow the included guide).
2. **Make sure your microphone and speakers are working**.
3. **Run FactBot** – It will greet you with “Hello, I am FactBot. Ask me anything!”
4. **Ask a question** – You can say “Hey FactBot, what is climate change?” or just start talking (if you’ve disabled the wake word).
5. **Listen** – FactBot will think for a few seconds, then start speaking the answer.
6. **Ask follow‑ups** – You can ask related questions, like “What are its causes?” and FactBot will remember the previous context.
7. **To exit** – Say “exit”, “quit”, or “stop”.

---

## 8. Example Conversation

> **User:** Hey FactBot, what is quantum computing?
>
> **FactBot:** *Processing...*  
> *Speaking:* According to Wikipedia, quantum computing is a type of computing that uses quantum‑mechanical phenomena like superposition and entanglement to perform operations on data. News sources add that recent advances in quantum computing could revolutionise fields like cryptography and drug discovery. There is no major conflict among the sources.

> **User:** What are the challenges?
>
> **FactBot:** *Speaking:* The main challenges include maintaining qubit stability, error correction, and the need for extremely low temperatures. Wikipedia notes that building a practical quantum computer is still a major engineering hurdle, while news articles mention that companies like Google and IBM are investing heavily in overcoming these obstacles.

---

## 9. Future Plans

- **More sources** – Add fact‑checking websites like Snopes, or specialised databases.
- **Graphical interface** – A simple window with a button to start listening and a text display of answers.
- **Multi‑language support** – Allow questions and answers in different languages.
- **Personalisation** – Learn your interests and tailor answers.
- **Better conflict resolution** – Use more advanced NLP to explain why sources disagree.

---

## 10. Summary

FactBot is a voice‑powered fact‑checking tool that makes getting accurate information quick and effortless. By combining multiple sources, smart summarisation and a natural voice interface, it provides a friendly way to stay informed. Whether you’re a curious individual, a student, or just someone who wants quick answers, FactBot is designed to help.

---

**Ready to try it?** Follow the installation instructions provided in the technical documentation, and start asking questions today!
