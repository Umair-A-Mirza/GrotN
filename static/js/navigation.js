const guest = `
<nav
  class="font-custom flex justify-between p-6 bg-back_1 font-normal sticky top-0 w-full z-50 box-border backdrop-blur-lg text-lg text-txt mb-6"
>
  <ul class="no-underline flex items-center">
    <li class="mr-6">
      <img
        class="h-12 w-auto cursor-pointer"
        src="/static/images/newlogo.png"
        alt="logo"
      />
    </li>
    <li class="mr-6">
      <a
        class="p-2 rounded-lg transition ease-in duration-500 hover:font-semibold hover:bg-gray-100 hover:text-txt"
        href="../index/index.html"
        >Home</a
      >
    </li>
    <li class="mr-6">
      <div
        class="flex p-2 rounded-lg transition ease-in duration-500 hover:font-semibold hover:bg-gray-100 hover:text-txt relative"
      >
        <div class="cursor-pointer flex" onclick="showResources()">
          <button id="resources">Resources</button>
          <svg
            width="15"
            height="15"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            class="mt-[6px] ml-2"
          >
            <path
              d="M19.9201 8.94995L13.4001 15.47C12.6301 16.24 11.3701 16.24 10.6001 15.47L4.08008 8.94995"
              stroke="#000000"
              stroke-width="1.5"
              stroke-miterlimit="10"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
        <div
          id="resources-dropdown"
          class="hidden flex flex-col min-w-64 bg-back_1 backdrop-blur-lg p-2 absolute top-10 left-0 rounded-lg z-50"
        >
          <a
            class="hover:text-white hover:bg-txt rounded-lg pl-6 py-2"
            href="../index/index.html"
            >Our Code</a
          >
          <a
            class="hover:text-white hover:bg-txt rounded-lg pl-6 py-2"
            href="../index/index.html"
            >Our Site</a
          >
          <a
            class="hover:text-white hover:bg-txt rounded-lg pl-6 py-2"
            href="../index/index.html"
            >Our Plans</a
          >
        </div>
      </div>
    </li>
    <li class="mr-6">
      <a
        class="p-2 rounded-lg transition ease-in duration-500 hover:font-semibold hover:bg-gray-100 hover:text-txt"
        href="../index/index.html"
        >About Us</a
      >
    </li>
    <li class="mr-6">
      <a
        class="p-2 rounded-lg transition ease-in duration-500 hover:font-semibold hover:bg-gray-100 hover:text-txt"
        href="../index/index.html"
        >Real Estate</a
      >
    </li>
  </ul>
  <div class="absolute left-[55%] mt-1 font-bold text-2xl">GrotN</div>
  <div class="flex gap-2">
    <a
      class="p-2 rounded-lg transition ease-in duration-500 hover:font-semibold hover:bg-gray-100 hover:text-txt"
      href="../landlord/landlord_login.html"
      >List your property!</a
    >
    <button
      id="primary"
      class="inline-block h-10 py-1 px-6 rounded-lg flex justify-center items-center bg-txt text-white transition ease-in duration-500 hover:bg-bttns"
      onclick="proceed(event)"
    >
      Log In
    </button>
  </div>
</nav>
`;

/**
 * Adding navbar to the body of the document.
 */
document.addEventListener("DOMContentLoaded", () => {
  const body = document.querySelector("body");
  // Add conditions to check if the user is logged in or not, along with the type of user, and then the version of the navbar to add from the options above.
  body.insertAdjacentHTML("afterbegin", guest);
  if (window.location.href.includes("login")) {
    document.getElementById("primary").innerText = "Sign Up";
  }
});

/**
 * To show/hide the dropdown.
 */
const showResources = () => {
  const dropdown = document.getElementById("resources-dropdown");
  dropdown.classList.toggle("hidden");
};

const proceed = (e) => {
  const button = e.target;
  button.innerText.includes("Log In")
    ? (window.location.href = "/tenant/login")
    : (window.location.href = "/tenant/signup");
};
