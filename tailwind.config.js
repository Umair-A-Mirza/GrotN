/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/js/*.js"],
  theme: {
    extend: {
      fontFamily: {
        custom: ["Poppins", "sans-serif"],
      },
      colors: {
        back_1: "rgba(254, 255, 255, 0.5)",
        lgrey: "rgba(23,37,42,0.50)",
        txt: "rgba(23, 37, 42, 1)",
        bttns: "rgba(58, 175, 169, 1)",
        alternateBlue: "rgba(43, 122, 120, 1)",
        customBrown: "#9B775C",
        darkGreen: "#17252a",
        borderColor: "#def1f2",
      },
    },
  },
  plugins: [],
};
