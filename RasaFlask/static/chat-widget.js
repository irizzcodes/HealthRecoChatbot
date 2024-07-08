$(document).ready(function() {
  // Initialize chat widget
  $("#chat-widget-input").focus();

  // Handle user input
  $("#chat-widget-input").keyup(function(event) {
    if(event.which === 13) {
      // Get user message
      let userMessage = $("#chat-widget-input").val();

      // Clear input field
      $("#chat-widget-input").val("");

      // Append user message to chat box
      $("#chat-widget-messages").append("<div><strong>You:</strong> " + userMessage + "</div>");

      // Send user message to server and get bot response
      $.ajax({
        type: "POST",
        url: "/webhook",
        contentType: "application/json",
        data: JSON.stringify({ message: userMessage }),
        success: function(data) {
          let botResponse = data.response;

          // Append bot response to chat box
          $("#chat-widget-messages").append("<div><strong>Bot:</strong> " + botResponse + "</div>");

          // Auto-scroll to the bottom of the chat box
          setTimeout(function() {
            $("#chat-widget-messages").scrollTop($("#chat-widget-messages")[0].scrollHeight);
          }, 100);
        },

        error: function() {
          // Handle error
          alert("Error: unable to send message to server");
        }
      });
    }
  });
});

