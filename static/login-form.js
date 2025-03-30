document
  .getElementById("login-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const loginFormData = {
      username: document.getElementById("username").value,
      password: document.getElementById("password").value,
    };

    if (!loginFormData.username || !loginFormData.password) {
      alert("Please provide both username and password.");
      return;
    }

    try {
      const response = await fetch("/get_user", {
        method: "POST", // Changed to POST for security
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(loginFormData),
      });

      const result = await response.json();

      if (response.ok) {
        alert("Successfully signed in!");
        window.location.href = "/contact"; // Redirect after login
      } else {
        alert("Error: " + result.error);
      }
    } catch (error) {
      console.error("Error during login:", error);
      alert("Could not sign in, check the error log.");
    }
  });
