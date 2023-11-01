/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*"],
  theme: {
    extend: {
      fontFamily: {
        mullish: ["Mulish", "sans-serif"],
      },
      colors: {
        bg1: "linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);",
        whitefaint: "rgba(219, 226, 239, 0.5)",
        whitefaint2: "rgba(255, 255, 255, 0.7)",
        deepBlue: "#02042a",
        lightBlue: "#2b84ea",
        lightBlue300: "#4b94ed",
        lightBlue500: "#0b72e7",
        greenLight: "#61cea6",
        grayText: "#818597",
        lightGray: "#e2e2e2",
        grayBlue: "#344a6c",
        deepBlueHead: "#162f56",
        gray2: "#525a76",
      },},
  },
  plugins: [],
}
