# 💧 WaterBuddy

A simple yet effective hydration reminder application that helps you stay hydrated throughout the day by sending periodic desktop notifications.

## 🚀 Features

- **Customizable Intervals**: Set your preferred reminder frequency
- **Desktop Notifications**: Cross-platform system notifications that won't interrupt your work
- **Lightweight**: Minimal resource usage, runs quietly in the background
- **Simple Configuration**: Easy-to-modify settings
- **Time Stamps**: Shows current time with each reminder

## 📋 Requirements

- Python 3.6+
- `plyer` library for cross-platform notifications

## 🛠️ Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/CrabbyCodes/waterBuddyV1.git
   cd waterBuddyV1
   ```

2. **Install required dependencies**
   ```bash
   pip install plyer
   ```

## 🎯 Usage

### Basic Usage
Simply run the main script to start receiving hydration reminders:

```bash
python main.py
```

The application will:
- Start running in the background
- Send periodic notifications based on the configured interval
- Display the current time with each reminder
- Continue running until manually stopped (Ctrl+C)

### Configuration

Edit `config.py` to customize your experience:

```python
# Reminder interval in minutes
INTERVAL_MINUTES = 60  # Default: 60 minutes

# Notification title
TITLE = "💧 WaterBuddy"

# Notification message
MESSAGE = "Time to drink WATER MA BOI!!!"
```

## 📁 Project Structure

```
waterBuddyV1/
├── main.py              # Entry point - starts the reminder loop
├── reminder_logic.py    # Core logic for timing and sending reminders
├── notifier.py         # Handles system notifications
├── config.py           # Configuration settings
└── README.md           # This file
```

## 🔧 How It Works

1. **main.py**: Entry point that initiates the reminder system
2. **reminder_logic.py**: Contains the main loop that:
   - Waits for the specified interval
   - Formats the reminder message with current time
   - Triggers notifications
3. **notifier.py**: Handles cross-platform desktop notifications using the `plyer` library
4. **config.py**: Stores customizable settings for intervals and messages

## 💡 Tips

- **For Development/Testing**: Set `INTERVAL_MINUTES = 0.1` (6 seconds) to test notifications quickly
- **For Daily Use**: Set `INTERVAL_MINUTES = 60` (1 hour) or your preferred interval
- **Running in Background**: On Windows, you can run the script minimized or use task scheduler for automatic startup

## 🛑 Stopping the Application

To stop WaterBuddy, simply press `Ctrl+C` in the terminal where it's running.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- GUI interface
- More notification customization options
- Integration with fitness trackers
- Smart scheduling based on time of day

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [plyer](https://github.com/kivy/plyer) for cross-platform notifications
- Inspired by the importance of staying hydrated for health and productivity

---

Stay hydrated! 💧
