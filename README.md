# QuitBit 🚭 - Smoke-Free Companion Chatbot

An AI-powered chatbot designed to support individuals on their journey to quit smoking. Built with Flask and sentiment analysis to provide personalized emotional support, practical advice, and motivation.

![QuitBit Chatbot](https://img.shields.io/badge/Version-1.0.0-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)

## ✨ Features

- **🤖 AI-Powered Support** - Uses Hugging Face sentiment analysis to understand user emotions
- **💬 Context-Aware Conversations** - Smart responses tailored to smoking cessation challenges
- **💪 Motivational System** - Dynamic encouragement and health benefit facts
- **📊 Progress Tracking** - Real-time statistics on money saved, cigarettes avoided, and smoke-free time
- **🎯 Quick Actions** - One-tap responses for common situations like cravings and stress
- **📱 Responsive Design** - Beautiful, mobile-friendly interface with dark/light mode
- **🔒 Privacy Focused** - All processing happens locally; no data stored permanently

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Pavi-NP/QuitBit.git
cd QuitBit
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser** and navigate to `http://localhost:5001`

## 🏗️ Project Structure

```
QuitBit/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── templates/          # Web interface templates
│   └── index.html     # Main chat interface
└── static/            # Static assets
    └── style.css      # CSS styling with Tailwind
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **AI/ML**: Hugging Face Transformers for sentiment analysis
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Styling**: Custom CSS with responsive design
- **Security**: GitHub secret scanning protection

## 💡 How It Works

1. **User Input**: Users share their feelings, challenges, or successes
2. **Sentiment Analysis**: AI model analyzes emotional tone of messages
3. **Context Matching**: Identifies smoking-related keywords and contexts
4. **Personalized Response**: Generates supportive, context-aware responses
5. **Progress Tracking**: Updates real-time statistics on quitting benefits

## 🎮 Usage Examples

- **Share feelings**: "I'm having strong cravings today"
- **Celebrate wins**: "I stayed smoke-free for 3 days!"
- **Seek advice**: "How do I handle stress without smoking?"
- **Get motivation**: "Tell me why quitting is worth it"

## 🌟 Key Benefits

### For Users
- 24/7 emotional support during quitting journey
- Evidence-based coping strategies
- Motivational health facts and progress tracking
- Non-judgmental, always available companion

### For Developers
- Clean, modular Flask architecture
- Easy to extend with new features
- Modern responsive UI components
- Comprehensive error handling

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chat interface |
| `/chat` | POST | Send message and get AI response |
| `/motivation` | GET | Get random motivational fact |
| `/health` | GET | Health check endpoint |

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider using:
- **WSGI Server**: Gunicorn or uWSGI
- **Platform**: Heroku, AWS Elastic Beanstalk, or DigitalOcean
- **Reverse Proxy**: Nginx

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5001 app:app
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests for:
- New features and improvements
- Bug fixes
- Documentation enhancements
- UI/UX improvements

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/Pavi-NP/QuitBit/issues) page
2. Create a new issue with detailed description
3. Contact the maintainers

## 🙏 Acknowledgments

- Hugging Face for the sentiment analysis model
- Tailwind CSS for the beautiful UI components
- Flask community for the excellent web framework
- All contributors and users who help improve QuitBit

---

<div align="center">

**Made with ❤️ to help people live healthier, smoke-free lives**

[⭐ Star this repo](https://github.com/Pavi-NP/QuitBit) if you find it helpful!

</div>
