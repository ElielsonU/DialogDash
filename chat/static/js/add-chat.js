/**@type {Element} */
const addChatButton = document.querySelector('#add-chat');
/**@type {Element} */
const addChatForm = document.querySelector('#add-chat-form');

addChatButton.onclick = () => {
  addChatForm.submit();
}