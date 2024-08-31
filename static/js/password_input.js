const show = `
<svg class="password_eye" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M15.5799 11.9999C15.5799 13.9799 13.9799 15.5799 11.9999 15.5799C10.0199 15.5799 8.41992 13.9799 8.41992 11.9999C8.41992 10.0199 10.0199 8.41992 11.9999 8.41992C13.9799 8.41992 15.5799 10.0199 15.5799 11.9999Z" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M11.9998 20.27C15.5298 20.27 18.8198 18.19 21.1098 14.59C22.0098 13.18 22.0098 10.81 21.1098 9.39997C18.8198 5.79997 15.5298 3.71997 11.9998 3.71997C8.46984 3.71997 5.17984 5.79997 2.88984 9.39997C1.98984 10.81 1.98984 13.18 2.88984 14.59C5.17984 18.19 8.46984 20.27 11.9998 20.27Z" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`;

const hide = `
<svg class="password_eye" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14.5299 9.46992L9.46992 14.5299C8.81992 13.8799 8.41992 12.9899 8.41992 11.9999C8.41992 10.0199 10.0199 8.41992 11.9999 8.41992C12.9899 8.41992 13.8799 8.81992 14.5299 9.46992Z" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M17.8198 5.76998C16.0698 4.44998 14.0698 3.72998 11.9998 3.72998C8.46984 3.72998 5.17984 5.80998 2.88984 9.40998C1.98984 10.82 1.98984 13.19 2.88984 14.6C3.67984 15.84 4.59984 16.91 5.59984 17.77" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M8.41992 19.5299C9.55992 20.0099 10.7699 20.2699 11.9999 20.2699C15.5299 20.2699 18.8199 18.1899 21.1099 14.5899C22.0099 13.1799 22.0099 10.8099 21.1099 9.39993C20.7799 8.87993 20.4199 8.38993 20.0499 7.92993" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M15.5099 12.7C15.2499 14.11 14.0999 15.26 12.6899 15.52" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M9.47 14.53L2 22" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M21.9998 2L14.5298 9.47" stroke="#6D6D6D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
`;

document.addEventListener("DOMContentLoaded", () => {
  const passContainers = document.querySelectorAll(".pass_container");
  passContainers.forEach((container) => {
    const input = container.querySelector(".password_input");
    container.insertAdjacentHTML("beforeend", show);
    container.addEventListener("click", (e) => {
      if (e.target.classList.contains("password_eye")) {
        const eye = container.querySelector(".password_eye");
        eye.remove();
        if (input.type === "password") {
          input.type = "text";
          container.insertAdjacentHTML("beforeend", hide);
        } else {
          input.type = "password";
          container.insertAdjacentHTML("beforeend", show);
        }
      }
    });
  });
});
