  const chatBox = document.getElementById("chat");
  const input = document.getElementById("input");

function addMessage(text, sender, userText = null, showFeedback = true) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender);

  // conteudo da mensagem
  const content = document.createElement("div");
  content.classList.add("message-content");
  content.textContent = text;
  msg.appendChild(content);

  // botão feedback bot
  if (sender === "bot" && showFeedback) {
    const feedback = document.createElement("div");
    feedback.classList.add("feedback-buttons");

// botão de refazer a msg
  const redoBtn = document.createElement("button");
  redoBtn.innerHTML = '<i class="fa-solid fa-rotate"></i>'; // ícone de refazer
  redoBtn.classList.add("tooltip");
  redoBtn.setAttribute("data-tooltip", "Refazer!");
  redoBtn.addEventListener("click", () => {
    redoMessage(msg, text);
  });

    // like
    const likeBtn = document.createElement("button");
    likeBtn.innerHTML = '<i class="fa-solid fa-thumbs-up"></i>';
    likeBtn.classList.add("tooltip");
    likeBtn.setAttribute("data-tooltip", "Gostei!");
    likeBtn.addEventListener("click", () => {
      likeBtn.classList.add("active");
            reFeedback("like", text, userText)
      dislikeBtn.classList.remove("active");
    // desabilitar os botão dps de clicar
    likeBtn.disabled = true;
    dislikeBtn.disabled = true;
    });

    // dislike
    const dislikeBtn = document.createElement("button");
    dislikeBtn.innerHTML = '<i class="fa-solid fa-thumbs-down"></i>';
    dislikeBtn.classList.add("tooltip");
    dislikeBtn.setAttribute("data-tooltip", "Não gostei!");
    dislikeBtn.addEventListener("click", () => {
      dislikeBtn.classList.add("active");
            reFeedback("dislike", text, userText)
      likeBtn.classList.remove("active");
    // desabilitar os botão dps de clicar
    likeBtn.disabled = true;
    dislikeBtn.disabled = true;      
    });

    feedback.appendChild(redoBtn);
    feedback.appendChild(likeBtn);
    feedback.appendChild(dislikeBtn);
    msg.appendChild(feedback);
  }

  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;

  return msg;
}

function reFeedback(type, message, umessage) {
  fetch("/feedback", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_message: umessage,
      feedback_type: type,
      bot_message: message,
      timestamp: new Date().toISOString()
    })  
  })
  .then(response => response.json())
  .then(data => {
    console.log("Feedback registrado com sucesso:", data)
  })
  .catch(err => console.error("Erro ao enviar o feedback:", err))
}

async function enviar(predefinedText, isUser = true) {
  const text = predefinedText || input.value.trim();
  if (text === "") return;

  if (isUser && !predefinedText) input.value = "";

  if (isUser) addMessage(text, "user");

  // Mensagem de "digitando..."
  const loading = document.createElement("div");
  loading.classList.add("message", "bot");
  loading.innerHTML = `<div class="message-content">Digitando...</div>`;
  chatBox.appendChild(loading);
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const response = await fetch("/get_response", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    const data = await response.json();

    loading.remove();
    addMessage(data.response, "bot", text);
  } catch (err) {
    loading.remove();
    addMessage("⚠️ Erro ao conectar com o servidor Flask.", "bot");
    console.error(err);
  }
}

input.addEventListener("keypress", e => {
  if (e.key === "Enter") enviar();
});

document.addEventListener('DOMContentLoaded', () => {
  const settingsBtn = document.getElementById('settings-btn');
  const settingsPanel = document.getElementById('settings-panel');
  const fontFamilySelect = document.getElementById('font-family');
  const lightModeBtn = document.getElementById('light-mode-btn');
  const darkModeBtn = document.getElementById('dark-mode-btn');
 
settingsBtn.addEventListener('click', () => {
  settingsPanel.classList.toggle('open');
});


// ===== FONTES =====
fontFamilySelect.addEventListener('change', e => {
  document.body.style.fontFamily = e.target.value;
  localStorage.setItem('fontFamily', e.target.value);
});

// ===== MODO CLARO/ESCURO =====
function setMode(mode) {
  if (mode === 'light') {
    document.body.classList.add('light-mode');
    lightModeBtn.classList.add('active');
    darkModeBtn.classList.remove('active');
  } else {
    document.body.classList.remove('light-mode');
    darkModeBtn.classList.add('active');
    lightModeBtn.classList.remove('active');
  }
  localStorage.setItem('mode', mode);
}

lightModeBtn.addEventListener('click', () => setMode('light'));
darkModeBtn.addEventListener('click', () => setMode('dark'));

// ===== CARREGAR PREFERÊNCIAS =====
const savedFont = localStorage.getItem('fontFamily');
const savedMode = localStorage.getItem('mode') || 'dark';

if (savedFont) {
  document.body.style.fontFamily = savedFont;
  fontFamilySelect.value = savedFont;
}
setMode(savedMode);

// msg de "boas vindas"
addMessage("Olá! Eu sou Whiribot, o chatbot desenvolvido para responder perguntas frequentes da Whirpool. \nVamos começar clicando na barra logo abaixo escrito de 'Digite sua mensagem' e escreva sua pergunta depois clique no botão de 'Enviar' ou aperte o botão Enter do teclado.", "bot", null, false);
});