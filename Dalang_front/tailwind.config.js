/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#115583',
        secondary: '#44AAE2',
        'text-primary': '#4A524D',
        'text-secondary': '#92B3B5',
      },
    },
  },
  plugins: [],
}