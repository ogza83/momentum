document.addEventListener("DOMContentLoaded", function () {
  const startChatButton = document.getElementById("startChat");

  // Make sure the button exists
  if (startChatButton) {
    startChatButton.style.display = "block"; // Show the button if needed

    startChatButton.addEventListener("click", function () {
      window.location.href = "/start-chat"; // Navigate to the Flask route that redirects to Streamlit
    });
  }
});

startTyping(); // Initialize typing effect and UI transitions

function startTyping() {
  typeText(
    "headline",
    "Momentum: The Smart Tool That Grow Your Business",
    0,
    () => {
      typeText(
        "subheading",
        "Streamline your tasks, cut down the busy work, and focus on what matters. Momentum’s AI-powered 'Micro Apps' help you do more, faster.",
        0,
        () => {
          document.getElementById("startButton").style.display = "block";
        }
      );
    }
  );
}

function typeText(elementId, text, index, callback) {
  const element = document.getElementById(elementId);
  if (element && index < text.length) {
    element.innerHTML += text[index];
    setTimeout(() => typeText(elementId, text, index + 1, callback), 30);
  } else if (callback) {
    callback();
  }
}
