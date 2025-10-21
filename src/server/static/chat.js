console.log('Chatbot Fatec Whirlpool')

export class Chat {
  socket = null

  constructor(id) {
    this.id = id

    this.messages = []
    this.messagesDiv = document.getElementById('messages')
    this.messageInput = document.getElementById('message')
    this.sendButton = document.getElementById('send')

    console.log('Chat ID:', this.id)
  }

  start() {
    this.setEvents()

    this.socket = io();

    this.setSocketEvents()
  }

  setSocketEvents() {
    this.socket.on('connect', () => {
      this.socket.emit('my event', { data: 'I\'m connected!' });
    });

    this.socket.on('message', (data) => {
      this.receiveMessage(data.message);
    });
  }

  setEvents() {
    this.sendButton.addEventListener('click', () => this.sendMessage())

    this.messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.sendMessage()
    })
  }

  sendMessage() {
    const message = this.messageInput.value.trim()
    if (message) {
      this.addMessage('user', message)
      this.messageInput.value = ''
      this.socket.emit('message', { chatId: this.id, message: message })
    }
  }

  addMessage(sender, text) {
    const messageDiv = document.createElement('div')
    messageDiv.className = `message ${sender}`
    messageDiv.textContent = `${sender}: ${text}`

    this.messagesDiv.appendChild(messageDiv)
    this.messagesDiv.scrollTop = this.messagesDiv.scrollHeight

    this.messages.push({ sender, text, timestamp: Date.now() })
  }

  receiveMessage(text) {
    this.addMessage('bot', text)
  }
}
