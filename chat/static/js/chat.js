const webSocket = new WebSocket(`ws://${location.host}/ws/chat/${chatId}/`);
const chat = document.querySelector(".messages");
const messageForm = document.querySelector(".send-message");
const messageInput = document.querySelector(".send-message>input");
const notificationAudio = document.querySelector("#notification");
chat.scroll({ top: chat.scrollHeight });

webSocket.onopen = function (e) {
  console.log("Conectado!");
};

webSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  const { message, senderId } = data;
  const fromMe = senderId == userId;
  const messageElement = document.createElement("div");
  messageElement.classList.add("message");
  if (!fromMe) notificationAudio.play();
  messageElement.classList.add(fromMe ? "sent" : "received");
  messageElement.textContent = `${message}`;
  chat.appendChild(messageElement);
  chat.scroll({ top: chat.scrollHeight, behavior: "smooth" });
};

messageForm.onsubmit = function (e) {
  e.preventDefault();
  const message = messageInput.value;
  if (!message) return;
  webSocket.send(JSON.stringify({ message, origin: true }));
  messageInput.value = "";
};
