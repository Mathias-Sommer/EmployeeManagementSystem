document
  .getElementById("register-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const registerFormData = {
      username: document.getElementById("username").value,
      firstname: document.getElementById("firstname").value,
      lastname: document.getElementById("lastname").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value,
      password_confirm: document.getElementById("password_confirm").value,
    };

    if (registerFormData.password !== registerFormData.password_confirm) {
      alert("Passwords does not match, please re-enter passwords.");
      return;
    }

    try {
      const response = await fetch("/create_user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: registerFormData.username,
          firstname: registerFormData.firstname,
          lastname: registerFormData.lastname,
          email: registerFormData.email,
          password: registerFormData.password,
        }),
      });

      const result = await response.json();

      if (response.ok) {
        alert("User registration completed.");
        window.location.href = "/login";
      } else {
        alert("Error:", result.error);
      }
    } catch (error) {
      console.error("Error while registering user:", error);
      alert("Could not register user. Check the log.");
    }
  });
