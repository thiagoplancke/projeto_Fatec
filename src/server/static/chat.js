console.log('Chatbot Fatec Whirlpool')

export class Chat {
  constructor() {
    this.id = null
    this.messages = []
    this.messagesDiv = null
    this.messageInput = null
    this.sendButton = null
  }

  setId(id) {
    this.id = id
    console.log('Chat ID:', this.id)
  }

  start() {
    this.messagesDiv = document.getElementById('messages')
    this.messageInput = document.getElementById('message')
    this.sendButton = document.getElementById('send')

    if (this.sendButton) {
      this.sendButton.addEventListener('click', () => this.sendMessage())
    }

    if (this.messageInput) {
      this.messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
          this.sendMessage()
        }
      })
    }

    console.log('Chat started')
  }

  sendMessage() {
    const message = this.messageInput.value.trim()
    if (message) {
      this.addMessage('user', message)
      this.messageInput.value = ''
      
      // Emit message via socket.io if available
      if (typeof io !== 'undefined' && window.socket) {
        window.socket.emit('message', { chatId: this.id, message: message })
      }
    }
  }

  addMessage(sender, text) {
    const messageDiv = document.createElement('div')
    messageDiv.className = `message ${sender}`
    messageDiv.textContent = `${sender}: ${text}`
    
    if (this.messagesDiv) {
      this.messagesDiv.appendChild(messageDiv)
      this.messagesDiv.scrollTop = this.messagesDiv.scrollHeight
    }
    
    this.messages.push({ sender, text, timestamp: Date.now() })
  }

  receiveMessage(text) {
    this.addMessage('bot', text)
  }
}
